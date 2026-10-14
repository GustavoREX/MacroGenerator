"""eu diria que trabalhar com programação e edição de imagens é pedir para ficar insano"""
from dataclasses import dataclass, field
from functools import lru_cache
from PIL import Image, ImageChops, ImageDraw, ImageOps
import numpy as np


@dataclass
class Slice:
    start_trim: float = 0.0
    end_trim: float = 0.0
    visible: bool = True


@dataclass
class TokenSettings:
    advanced: bool = False
    image_zoom: float = 1.0
    border_zoom: float = 0.9
    offset_x: float = 0.0  # fraction of the exported square
    offset_y: float = 0.0
    crop: str = 'circle'
    crop_scale: float = 0.9
    fit: str = 'cover'
    trim_transparent: bool = True
    background: str | None = None
    rotation: float = 0.0  # clockwise, zero starts at twelve o'clock
    slices: list[Slice] = field(default_factory=lambda: [Slice() for _ in range(4)])


def read_image(path):
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert('RGBA')


def place_image(image, size, zoom=1.0, offset=(0.0, 0.0), fit='contain', trim=False):
    """Sample directly into the square; huge zooms don't allocate huge images."""
    source = image if image.mode == 'RGBA' else image.convert('RGBA')
    if trim:
        bounds = source.getbbox(alpha_only=True)
        if bounds:
            source = source.crop(bounds)
    ratio = (max if fit == 'cover' else min)(size / source.width, size / source.height)
    scale = max(0.001, ratio * zoom)
    x = (size - source.width * scale) / 2 + offset[0] * size
    y = (size - source.height * scale) / 2 + offset[1] * size
    return source.transform((size, size), Image.Transform.AFFINE,
                            (1 / scale, 0, -x / scale, 0, 1 / scale, -y / scale),
                            resample=Image.Resampling.BICUBIC)


@lru_cache(maxsize=8)
def circle_mask(size, diameter):
    factor = 2
    mask = Image.new('L', (size * factor, size * factor))
    margin = size * factor * (1 - diameter) / 2
    ImageDraw.Draw(mask).ellipse((margin, margin, size * factor - margin - 1,
                                 size * factor - margin - 1), fill=255)
    return mask.resize((size, size), Image.Resampling.LANCZOS)


@lru_cache(maxsize=2)
def polar_grid(size):
    # Pixel-centred coordinates keep odd and even output sizes centred alike.
    y, x = np.ogrid[:size, :size]
    x = x.astype(np.float32) + 0.5 - size / 2
    y = y.astype(np.float32) + 0.5 - size / 2
    angle = (np.degrees(np.arctan2(x, -y)) + 360) % 360
    radius = np.hypot(x, y)
    return angle, radius


def slice_mask(size, index, part, rotation=0):
    if not part.visible or part.start_trim + part.end_trim >= 90:
        return Image.new('L', (size, size))
    angle, radius = polar_grid(size)
    start = rotation + index * 90 + max(0, part.start_trim)
    extent = max(0, 90 - max(0, part.start_trim) - max(0, part.end_trim))
    local = (angle - start + 180) % 360 - 180
    # Signed distance to both radial edges, with a one-pixel antialias band.
    distance = np.minimum(local, extent - local)
    coverage = np.clip(np.radians(distance) * radius + 0.5, 0, 1)
    return Image.fromarray(np.uint8(np.rint(coverage * 255)))


def render_token(source, border, size, settings):
    size = int(size)
    if not 64 <= size <= 4096:
        raise ValueError('O tamanho deve estar entre 64 e 4096 pixels.')
    if len(settings.slices) != 4:
        raise ValueError('A borda avançada precisa de quatro fatias.')
    base = Image.new('RGBA', (size, size), settings.background or (0, 0, 0, 0))
    ring = place_image(border, size, settings.border_zoom) if border is not None else None
    # Fixed stack: complete border, imported image, four clipped border layers.
    if settings.advanced and ring is not None:
        base.alpha_composite(ring)
    if source is not None:
        layer = place_image(source, size, settings.image_zoom,
                            (settings.offset_x, settings.offset_y), settings.fit,
                            settings.trim_transparent)
        if settings.crop == 'circle':
            layer.putalpha(ImageChops.multiply(layer.getchannel('A'), circle_mask(size, settings.crop_scale)))
        base.alpha_composite(layer)
    if ring is not None:
        if settings.advanced:
            # Sum the disjoint angular masks before composition to avoid seams
            # and double-opacity where adjacent antialiased edges meet.
            if all(p.visible and p.start_trim == 0 and p.end_trim == 0 for p in settings.slices):
                mask = Image.new('L', (size, size), 255)
            else:
                mask = Image.new('L', (size, size))
                for index, part in enumerate(settings.slices):
                    mask = ImageChops.add(mask, slice_mask(size, index, part, settings.rotation))
            ring.putalpha(ImageChops.multiply(ring.getchannel('A'), mask))
        base.alpha_composite(ring)
    return base


@lru_cache(maxsize=4)
def checkerboard(size):
    image = Image.new('RGB', (size, size), '#eef1f6')
    draw = ImageDraw.Draw(image)
    step = 16
    for y in range(0, size, step):
        for x in range(0, size, step):
            if (x // step + y // step) % 2:
                draw.rectangle((x, y, x + step - 1, y + step - 1), fill='#dce3ed')
    return image.convert('RGBA')


def square_pad(image):
    size = max(image.size)
    square = Image.new('RGBA', (size, size))
    square.alpha_composite(image, ((size - image.width) // 2, (size - image.height) // 2))
    return square
