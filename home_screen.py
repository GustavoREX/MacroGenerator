"""Menu inicial com vila em pixel art e alternativa simples acessível por teclado."""
import math
from pathlib import Path
import time
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from core.paths import ROOT
from interface_settings import HomeOptions
from village_hero import VillageHero


DESTINATIONS = (
    ('macro', 'Criação de Macros', 'Ataques, perícias e macros do Roll20.', '#477cbb'),
    ('token', 'Criação de Tokens', 'Tokens, bordas e edição de imagens.', '#876bb1'),
    ('weapons', 'Forja de Armas', 'Monte armas, melhorias e encantamentos.', '#bb6a47'),
    ('armor', 'Forja de Armaduras', 'Prepare armaduras, escudos e proteções.', '#658b9d'),
    ('apothecary', 'Boticário Arcano', 'Poções, pergaminhos e Oficina Geral.', '#54876a'),
    ('shopping', 'SHOPING', 'Compras, itens e inventário.', '#b88e3f'),
)

# Centros e regiões das seis construções na ilustração original.
BUILDINGS = {
    'macro': (.32,.24,.36,.42,.455),
    'token': (.72,.26,.36,.42,.455),
    'weapons': (.15,.67,.24,.31,.84),
    'armor': (.40,.68,.23,.29,.85),
    'apothecary': (.63,.68,.21,.29,.85),
    'shopping': (.85,.66,.22,.31,.84),
}


class VillageEffectsSwitch(tk.Canvas):
    """Chavinha compacta dos efeitos, acessível por mouse, espaço e Enter."""

    def __init__(self, parent, variable, command):
        super().__init__(parent, width=38, height=22, bg='#20382f', bd=0,
                         highlightthickness=1, highlightbackground='#20382f',
                         highlightcolor='#ffe4a3', takefocus=True, cursor='hand2')
        self.variable, self.command = variable, command
        self.bind('<Button-1>', self._activate)
        self.bind('<space>', self._activate)
        self.bind('<Return>', self._activate)
        self._trace = variable.trace_add('write', self._draw)
        self.bind('<Destroy>', self._destroy)
        self._draw()

    def _draw(self, *_):
        self.delete('all')
        enabled = self.variable.get()
        color = '#78986c' if enabled else '#62706a'
        self.create_oval(2, 3, 18, 19, fill=color, outline='')
        self.create_rectangle(10, 3, 28, 19, fill=color, outline='')
        self.create_oval(20, 3, 36, 19, fill=color, outline='')
        center = 28 if enabled else 10
        self.create_oval(center-6, 5, center+6, 17, fill='#f3f1e8', outline='')

    def invoke(self):
        if str(self.cget('state')) != 'disabled':
            self.variable.set(not self.variable.get())
            self.command()

    def _activate(self, _event=None):
        self.focus_set()
        self.invoke()
        return 'break'

    def _destroy(self, event):
        if event.widget == self:
            self.variable.trace_remove('write', self._trace)


class HomeScreen(ttk.Frame):
    BACKGROUND = '#f3f1e8'
    INK = '#243e45'

    def __init__(self, master, navigate, settings, *, artwork=None):
        super().__init__(master, padding=16, style='Home.TFrame')
        ttk.Style(self).configure('Home.TFrame', background=self.BACKGROUND)
        self.navigate, self.settings = navigate, settings
        self._render_job = self._animation_job = self._pointer_job = None
        self._photo = None
        self._image_size = None
        self._bounds = {}
        self._hovered = None
        self._source = None
        self._village_cursor = None
        self._current_cursor = None
        self._pointer_active = False
        path = Path(artwork) if artwork is not None else ROOT/'assets'/'home'/'village.png'
        try:
            with Image.open(path) as source:
                self._source = source.convert('RGB')
        except (OSError, ValueError):
            pass
        self.simple_var = tk.BooleanVar(self, not settings.options.village or self._source is None)
        self.effects_var = tk.BooleanVar(self, settings.options.effects)

        header = tk.Frame(self, bg=self.BACKGROUND)
        header.pack(fill='x', pady=(0,10))
        self.intro = tk.Frame(header, bg=self.BACKGROUND)
        self.title_var = tk.StringVar(self, 'O que vamos criar hoje?')
        self.subtitle_var = tk.StringVar(self, 'Todas as ferramentas, em um só lugar.')
        tk.Label(self.intro,textvariable=self.title_var,font=('Segoe UI',22,'bold'),fg=self.INK,
                 bg=self.BACKGROUND,anchor='center').pack(fill='x')
        tk.Label(self.intro,textvariable=self.subtitle_var,font=('Segoe UI',10),fg='#647675',
                 bg=self.BACKGROUND,anchor='center').pack(fill='x',pady=(3,8))
        self.controls = tk.Frame(header,bg=self.BACKGROUND)
        self.controls.pack(fill='x')
        self.simple_check = ttk.Checkbutton(self.controls,text='Modo simples',variable=self.simple_var,command=self._change_options)
        self.simple_check.pack(side='left',padx=(0,18))
        if self._source is None:
            self.simple_check.configure(state='disabled')

        self.footer = tk.Frame(self,bg=self.BACKGROUND)
        self.status_var = tk.StringVar(self,'Escolha uma ferramenta para começar.')
        self.status_label = tk.Label(self.footer,textvariable=self.status_var,bg=self.BACKGROUND,
                                    fg='#526966',font=('Segoe UI',10),anchor='center',wraplength=800)
        self.status_label.pack(fill='x')
        tk.Label(self.footer,text='Você pode voltar a esta tela pelo botão Início.',bg=self.BACKGROUND,
                 fg='#7a8983',font=('Segoe UI',9)).pack(pady=(4,0))

        self.stage = tk.Frame(self,bg=self.BACKGROUND)
        self.stage.pack(fill='both',expand=True)
        self.canvas = tk.Canvas(self.stage,bg='#20382f',highlightthickness=0)
        # O cursor pertence somente à vila; as demais telas usam seus próprios cursores.
        cursor_path = ROOT/'assets'/'home'/'hero.cur'
        if cursor_path.is_file():
            try:
                # A lista Tcl preserva espaços; barras normais evitam escapes no caminho.
                cursor = ('@'+cursor_path.as_posix(),)
                self.canvas.configure(cursor=cursor)
                self._village_cursor = cursor
            except tk.TclError:
                pass  # Outros sistemas podem não oferecer suporte ao formato CUR do Windows.
        self.hero = VillageHero(self, ROOT/'assets'/'home'/'animations')
        self.canvas.bind('<Configure>',self._schedule_render)
        self.canvas.bind('<Enter>',self._motion)
        self.canvas.bind('<Motion>',self._motion)
        self.canvas.bind('<Leave>',self._leave_map)
        self.canvas.bind('<Button-1>',self._click)
        self.effect_controls = tk.Frame(self.stage,bg='#20382f',padx=5,pady=3)
        tk.Label(self.effect_controls,text='Efeitos',bg='#20382f',fg='#bdc8b8',
                 font=('Segoe UI',8)).pack(side='left',padx=(0,3))
        self.effects_check = VillageEffectsSwitch(self.effect_controls,self.effects_var,self._change_options)
        self.effects_check.pack(side='left')
        self.map_buttons = {}
        for key,label,description,color in DESTINATIONS:
            button = tk.Button(self.canvas,text=label,command=lambda k=key: self.navigate(k),
                bg='#31463a',fg='#ece9cf',activebackground='#455a43',activeforeground='white',
                relief='flat',bd=0,padx=5,pady=2,cursor=self._village_cursor or 'hand2',font=('Segoe UI',9),
                highlightthickness=1,highlightbackground='#31463a',highlightcolor='#ffe4a3')
            button.bind('<Enter>',lambda event,k=key: self._button_motion(event,k))
            button.bind('<Motion>',lambda event,k=key: self._button_motion(event,k))
            button.bind('<FocusIn>',lambda _,k=key: self._highlight(k))
            button.bind('<Leave>',self._leave_map)
            button.bind('<FocusOut>',lambda _: self._highlight(None))
            self.map_buttons[key] = button

        self.simple_host = tk.Frame(self.stage,bg=self.BACKGROUND)
        self.simple_grid = tk.Frame(self.simple_host,bg=self.BACKGROUND)
        self.simple_grid.place(relx=.5,rely=.5,anchor='center')
        self.simple_buttons = {}
        for index,(key,label,description,color) in enumerate(DESTINATIONS):
            button = tk.Button(self.simple_grid,text=label+('\n\n'+description if index<2 else ''),
                command=lambda k=key: self.navigate(k),font=('Segoe UI',12 if index<2 else 10,'bold'),
                bg='white',fg=self.INK,activebackground='#e5ebe5',activeforeground=self.INK,
                relief='flat',bd=0,padx=16,pady=22 if index<2 else 16,cursor='hand2',
                highlightthickness=2,highlightbackground=color,highlightcolor='#315ee7',wraplength=300)
            button.bind('<Enter>',lambda _,text=description: self.status_var.set(text))
            button.bind('<FocusIn>',lambda _,text=description: self.status_var.set(text))
            self.simple_buttons[key] = button
        self.simple_host.bind('<Configure>',self._layout_simple)
        self.bind('<Map>',self._on_map,add='+')
        self.bind('<Unmap>',self._on_unmap,add='+')
        self.bind('<Configure>',lambda e: self.status_label.configure(wraplength=max(260,e.width-40)) if e.widget==self else None,add='+')
        self._apply_mode()

    def _layout_simple(self,event):
        if event.width<2:
            return
        width = min(920,max(280,event.width-24))
        self.simple_grid.place_configure(width=width)
        columns = 4 if width>=760 else 2
        for col in range(4):
            self.simple_grid.columnconfigure(col,weight=1 if col<columns else 0,uniform='home' if col<columns else '')
        for index,(key,*_) in enumerate(DESTINATIONS):
            button = self.simple_buttons[key]
            if index<2:
                row,col,span = 0,index*(columns//2),columns//2
            else:
                row,col,span = 1+(index-2)//columns,(index-2)%columns,1
            button.grid(row=row,column=col,columnspan=span,sticky='nsew',padx=7,pady=7)
            button.configure(wraplength=max(110,width*(span/columns)-48))

    def _change_options(self):
        self._apply_mode()
        try:
            self.settings.save(HomeOptions(village=not self.simple_var.get(),effects=self.effects_var.get()))
        except OSError:
            self.status_var.set('Preferência aplicada nesta sessão; não foi possível salvá-la.')

    def _apply_mode(self):
        self._stop_animation()
        village = not self.simple_var.get() and self._source is not None
        self.canvas.pack_forget()
        self.simple_host.pack_forget()
        self.effects_check.configure(state='normal' if village else 'disabled')
        self.intro.pack_forget()
        self.footer.pack_forget()
        self.effect_controls.place_forget()
        if village:
            self.canvas.pack(fill='both',expand=True)
            self.effect_controls.place(relx=1,x=-8,y=8,anchor='ne')
            self.effect_controls.lift()
            self._schedule_render()
        else:
            self.intro.pack(fill='x',before=self.controls)
            self.footer.pack(side='bottom',fill='x',pady=(10,0),before=self.stage)
            self.simple_host.pack(fill='both',expand=True)
            self.canvas.delete('effect')

    def _schedule_render(self,_event=None):
        if self._render_job is None:
            self._render_job = self.after_idle(self._render)

    def _render(self):
        self._render_job = None
        if self.simple_var.get() or self._source is None:
            return
        width,height = self.canvas.winfo_width(),self.canvas.winfo_height()
        if min(width,height)<10:
            return
        scale = min(width/self._source.width,height/self._source.height)
        iw,ih = max(1,round(self._source.width*scale)),max(1,round(self._source.height*scale))
        x,y = (width-iw)//2,(height-ih)//2
        if self._image_size != (iw,ih):
            self._photo = ImageTk.PhotoImage(self._source.resize((iw,ih),Image.Resampling.NEAREST),master=self)
            self._image_size = iw,ih
        self.canvas.delete('all')
        self.canvas.create_image(x,y,image=self._photo,anchor='nw')
        self._bounds = {}
        for key,label,description,color in DESTINATIONS:
            cx,cy,bw,bh,label_y = BUILDINGS[key]
            box = (x+(cx-bw/2)*iw,y+(cy-bh/2)*ih,x+(cx+bw/2)*iw,y+(cy+bh/2)*ih)
            self._bounds[key] = box
            self.canvas.create_rectangle(*box,outline='',width=2,tags=('highlight',key))
            button = self.map_buttons[key]
            button.configure(font=('Segoe UI',9 if iw>=650 else 8),
                             wraplength=max(80,round(iw*bw)-12))
            self.canvas.create_window(x+cx*iw,y+label_y*ih,window=button,anchor='n')
        self._scene = x,y,iw,ih
        self._highlight(self._hovered)
        self._start_animation()

    def _hit(self,x,y):
        return next((key for key,(left,top,right,bottom) in self._bounds.items() if left<=x<=right and top<=y<=bottom),None)

    def _motion(self,event):
        self._highlight(self._hit(event.x,event.y))
        self._show_hero(self.canvas.winfo_rootx()+event.x,self.canvas.winfo_rooty()+event.y)

    def _button_motion(self,event,key):
        self._highlight(key)
        button = self.map_buttons[key]
        self._show_hero(button.winfo_rootx()+event.x,button.winfo_rooty()+event.y)

    def _show_hero(self,x,y):
        if self.simple_var.get() or not self.winfo_ismapped():
            return
        self._pointer_active = True
        self.hero.show(x,y,self._hovered or 'idle',self.effects_var.get())

    def _leave_map(self,_event=None):
        self._pointer_active = False
        self.hero.hide()
        self._highlight(None)

    def _pointer_target(self,x,y):
        """Confere a janela sob o ponteiro, inclusive sobre as plaquinhas nativas."""
        widget = self.winfo_containing(x,y)
        if widget == self.canvas:
            return True,self._hit(x-self.canvas.winfo_rootx(),y-self.canvas.winfo_rooty())
        for key,button in self.map_buttons.items():
            if widget == button:
                return True,key
        return False,None

    def _poll_pointer(self):
        self._pointer_job = None
        if self.simple_var.get() or not self.winfo_ismapped():
            self._leave_map()
            return
        x,y = self.winfo_pointerxy()
        inside,key = self._pointer_target(x,y)
        if inside:
            self._highlight(key)
            self._show_hero(x,y)
        elif self._pointer_active:
            self._leave_map()
        self._pointer_job = self.after(40,self._poll_pointer)

    def _click(self,event):
        key = self._hit(event.x,event.y)
        if key:
            self.navigate(key)

    def _highlight(self,key):
        self._hovered = key
        self._refresh_cursor()
        for destination,*_ in DESTINATIONS:
            for item in self.canvas.find_withtag(destination):
                self.canvas.itemconfigure(item,outline='#ffe6a6' if destination==key else '')
        if key:
            self.status_var.set(next(description for destination,label,description,color in DESTINATIONS if destination==key))
        else:
            self.status_var.set('Escolha uma ferramenta para começar.')

    def _set_cursor(self, cursor):
        if cursor == self._current_cursor:
            return
        self.canvas.configure(cursor=cursor)
        for button in self.map_buttons.values():
            button.configure(cursor=cursor or 'hand2')
        self._current_cursor = cursor

    def _refresh_cursor(self):
        cursor = self._village_cursor or ('hand2' if self._hovered else '')
        if self.hero.available:
            cursor = 'none'
        self._set_cursor(cursor)

    def _start_animation(self):
        if not self.simple_var.get() and self.winfo_ismapped() and self._pointer_job is None:
            self._poll_pointer()
        if self._animation_job is None and self.effects_var.get() and not self.simple_var.get() and self.winfo_ismapped():
            self._refresh_cursor()
            self._animate()

    def _animate(self):
        self._animation_job = None
        if not self.effects_var.get() or self.simple_var.get() or not self.winfo_ismapped():
            return
        self.canvas.delete('effect')
        if hasattr(self,'_scene'):
            x,y,w,h = self._scene
            clock = time.monotonic()
            for i in range(14):
                px = x+(.09+(i*.137)% .82)*w+math.sin(clock*.6+i)*3
                py = y+(.18+(i*.193)% .65)*h+math.sin(clock*.8+i*2)*5
                color = '#fff1b0' if math.sin(clock*1.3+i)>0 else '#bed79b'
                self.canvas.create_rectangle(px,py,px+2,py+2,fill=color,outline='',tags='effect')
        self._animation_job = self.after(120,self._animate)

    def _stop_animation(self):
        if self._pointer_job is not None:
            self.after_cancel(self._pointer_job)
            self._pointer_job = None
        self._pointer_active = False
        self.hero.hide()
        if self._animation_job is not None:
            self.after_cancel(self._animation_job)
            self._animation_job = None
        self.canvas.delete('effect')
        self._set_cursor(self._village_cursor or '')

    def _on_map(self,event):
        if event.widget==self:
            self._schedule_render()
            self._start_animation()

    def _on_unmap(self,event):
        if event.widget==self:
            self._stop_animation()

    def destroy(self):
        self._stop_animation()
        self.hero.destroy()
        if self._render_job is not None:
            self.after_cancel(self._render_job)
        super().destroy()
