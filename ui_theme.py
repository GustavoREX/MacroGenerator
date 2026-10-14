"""Shared desktop theme using only the standard Tk/ttk widgets."""


def configure_theme(root, style):
    background = "#eef2f8"
    surface = "#ffffff"
    ink = "#24324b"
    muted = "#65748b"
    accent = "#315ee7"
    root.configure(background=background)
    import tkinter.font as tkfont
    tkfont.nametofont("TkDefaultFont", root=root).configure(family="Segoe UI", size=10)
    root.option_add("*Canvas.background", surface)
    root.option_add("*Text.background", "#f4f7fc")
    root.option_add("*Text.foreground", ink)
    root.option_add("*Text.relief", "flat")
    style.configure(".", font=("Segoe UI", 10), background=surface, foreground=ink)
    style.configure("TFrame", background=surface)
    style.configure("App.TFrame", background=background)
    style.configure("Card.TFrame", background=surface, relief="flat", borderwidth=0)
    style.configure("TLabel", background=surface, foreground=ink)
    style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground=ink)
    style.configure("Section.TLabel", font=("Segoe UI", 11, "bold"), foreground=ink)
    style.configure("Small.TLabel", font=("Segoe UI", 9), foreground=muted)
    style.configure("TButton", padding=(10, 7), background="#edf1f9", foreground=ink, borderwidth=0)
    style.map("TButton", background=[("pressed", "#dce5f8"), ("active", "#e1e9fa")], foreground=[("disabled", "#8c97a8")])
    style.configure("TEntry", padding=7, fieldbackground=surface, bordercolor="#d4ddeb", lightcolor=surface, darkcolor=surface)
    style.map("TEntry", bordercolor=[("focus", accent)])
    style.configure("TSpinbox", padding=5, fieldbackground=surface)
    style.configure("TCheckbutton", padding=(2, 5), background=surface)
    style.configure("TRadiobutton", padding=(2, 5), background=surface)
    style.configure("Nav.TRadiobutton", padding=(12, 8), background="#edf1f9", indicatoron=False)
    style.layout("Nav.TRadiobutton", [("Radiobutton.padding", {"children": [("Radiobutton.label", {"sticky": "nswe"})], "sticky": "nswe"})])
    style.map("Nav.TRadiobutton", background=[("selected", accent), ("active", "#e1e9fa")], foreground=[("selected", "white")])
    style.configure("TScrollbar", background="#c7d2e5", troughcolor="#f4f7fc", borderwidth=0, arrowsize=12)
    for name in ("Primary.TButton", "Selected.TButton", "SpecialistSelected.TButton", "EffectActive.TButton"):
        style.configure(name, background=accent, foreground="white")
        style.map(name, background=[("disabled", "#8197dd"), ("active", "#254bc3"), ("!disabled", accent)], foreground=[("!disabled", "white"), ("disabled", "#edf1f9")])

    style.configure("DamageStep.TButton", font=("Segoe UI", 18, "bold"), padding=(18, 12))
    style.configure("DamageDie.TButton", padding=(4, 5))
    for name, base, active, foreground in (
        ("Pride.TButton", "#f2c94c", "#e0b83f", "#3d3000"),
        ("PrideActive.TButton", "#f2c94c", "#e0b83f", "#3d3000"),
        ("PrideInactive.TButton", "#fff4cc", "#f5e7ad", "#765600"),
        ("EffectInactive.TButton", "#dceeff", "#c8e1fc", "#174a75"),
        ("EditorSave.TButton", "#26734d", "#1b593a", "white"),
        ("EditorCancel.TButton", "#b63543", "#922b36", "white"),
    ):
        style.configure(name, background=base, foreground=foreground)
        style.map(name, background=[("disabled", base), ("active", active)], foreground=[("disabled", foreground), ("active", foreground)])
    style.configure("Modified.TButton", foreground="#b3261e")
    style.map("Modified.TButton", foreground=[("active", "#b3261e")])
    style.configure("SpecialistDisabled.TButton", background="#e5e9f0", foreground="#777777")
    style.map("SpecialistDisabled.TButton", background=[("disabled", "#e5e9f0")], foreground=[("disabled", "#777777")])


def set_responsive_window_geometry(
    window,
    width,
    height,
    minimum_width=360,
    minimum_height=240,
):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    available_width = max(320, screen_width - 40)
    available_height = max(240, screen_height - 80)
    width = min(width, available_width)
    height = min(height, available_height)
    window.geometry(f"{width}x{height}")
    window.minsize(
        min(minimum_width, width, available_width),
        min(minimum_height, height, available_height),
    )
    window.maxsize(available_width, available_height)




def update_canvas_scroll_region(canvas, scrollbar):
    bounds = canvas.bbox("all")
    content_height = bounds[3] if bounds else 0
    viewport_height = canvas.winfo_height()
    canvas.configure(
        scrollregion=(
            0,
            0,
            max(canvas.winfo_width(), bounds[2] if bounds else 0),
            max(content_height, viewport_height),
        )
    )
    if content_height > viewport_height + 1:
        scrollbar.state(["!disabled"])
    else:
        scrollbar.state(["disabled"])
        canvas.yview_moveto(0)
