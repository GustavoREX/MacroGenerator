"""Elementos visuais compartilhados pelos orçamentos de fabricação."""
import tkinter as tk
from tkinter import ttk

from crafting_core import format_money


GENERAL_FABRICATION_RULE = (
    'Ofício — regra geral de fabricação\n\n'
    'A matéria-prima custa um terço do preço do item. Faça um teste do Ofício correspondente: '
    'CD 15 para itens simples ou CD 20 para itens complexos.\n\n'
    'Tempo: um dia para consumíveis, uma semana para itens comuns não consumíveis '
    'e um mês para itens superiores ou mágicos não consumíveis. Itens muito grandes '
    'ou complexos podem exigir mais tempo, a critério do mestre.\n\n'
    'Consumíveis: é possível produzir duas unidades no mesmo tempo com –5 no teste, '
    'pagando a matéria-prima de ambas. Sem os instrumentos de ofício, o teste também sofre –5.\n\n'
    'Tormenta20 — Jogo do Ano, p. 121–122.'
)


def set_visible(widget, visible):
    """Reabre um campo na sua posição original entre os controles empacotados."""
    if not visible:
        widget.pack_forget()
    elif not widget.winfo_manager():
        siblings = widget.master.winfo_children()
        following = next((w for w in siblings[siblings.index(widget)+1:]
                          if w.winfo_manager() == 'pack'), None)
        widget.pack(fill='x', **({'before': following} if following else {}))


class InfoPopup:
    def __init__(self, owner):
        self.owner, self.window = owner, None
        owner.bind('<Destroy>', self._close_owner, add='+')
        owner.bind('<Unmap>', self._close_owner, add='+')

    def _close_owner(self, event):
        if event.widget == self.owner:
            self.hide()

    def attach(self, widget, title, description):
        # Atualiza os dados sem registrar novos comandos Tcl a cada orçamento.
        widget._forge_info = self, title, description
        if getattr(widget, '_forge_info_bound', False):
            return
        widget._forge_info_bound = True
        def show(_event=None):
            popup, current_title, current_description = widget._forge_info
            popup.show(widget, current_title, current_description)
        def hide(_event=None):
            widget._forge_info[0].hide()
        widget.configure(command=show)
        widget.bind('<Enter>', show)
        widget.bind('<Leave>', hide)
        widget.bind('<FocusIn>', show)
        widget.bind('<FocusOut>', hide)
        widget.bind('<Destroy>', hide, add='+')
        widget.bind('<Escape>', hide)

    def hide(self):
        if self.window is not None:
            self.window.destroy()
            self.window = None

    def show(self, widget, title, description):
        self.hide()
        if not widget.winfo_exists():
            return
        popup = self.window = tk.Toplevel(self.owner)
        popup.withdraw()
        popup.overrideredirect(True)
        popup.transient(self.owner.winfo_toplevel())
        width = min(440, popup.winfo_screenwidth()-32)
        card = tk.Frame(popup, background='#f4f7fc', highlightbackground='#bdcce7', highlightthickness=1, padx=14, pady=12)
        card.pack(fill='both', expand=True)
        for text, font in ((title, ('Segoe UI',11,'bold')), (description, ('Segoe UI',10))):
            tk.Label(card, text=text, font=font, background='#f4f7fc', foreground='#24324b',
                     wraplength=width-32, justify='left', anchor='w').pack(fill='x', pady=3)
        popup.update_idletasks()
        x = min(widget.winfo_rootx(), popup.winfo_screenwidth()-popup.winfo_reqwidth()-12)
        y = min(widget.winfo_rooty()+widget.winfo_height()+5, popup.winfo_screenheight()-popup.winfo_reqheight()-12)
        popup.geometry(f'+{max(8,x)}+{max(8,y)}')
        popup.deiconify()


def info_button(parent, popup, title, description):
    icon = ttk.Button(parent, text='ⓘ', width=3, cursor='question_arrow', padding=(2,2))
    popup.attach(icon, title, description)
    return icon


class ModeSwitch(tk.Canvas):
    """Interruptor desenhado em Tk, com acionamento por mouse e teclado."""
    def __init__(self, parent, variable):
        background = ttk.Style(parent).lookup('TFrame', 'background') or '#f0f0f0'
        super().__init__(parent, width=68, height=36, bg=background, bd=0,
                         highlightthickness=2, highlightbackground=background,
                         highlightcolor='#315ee7', takefocus=True, cursor='hand2')
        self.variable = variable
        self.bind('<Button-1>', self._click)
        self.bind('<space>', self._activate)
        self.bind('<Return>', self._activate)
        self.bind('<Left>', lambda _: self.variable.set(False))
        self.bind('<Right>', lambda _: self.variable.set(True))
        self._trace = variable.trace_add('write', self._draw)
        self.bind('<Destroy>', self._destroy)
        self._draw()

    def _draw(self, *_):
        self.delete('all')
        on = self.variable.get()
        color = '#315ee7' if on else '#69788e'
        self.create_oval(3, 4, 31, 32, fill=color, outline='')
        self.create_rectangle(17, 4, 51, 32, fill=color, outline='')
        self.create_oval(37, 4, 65, 32, fill=color, outline='')
        center = 51 if on else 17
        self.create_oval(center-11, 7, center+11, 29, fill='white', outline='')

    def invoke(self):
        self.variable.set(not self.variable.get())

    def _activate(self, _event):
        self.invoke()
        return 'break'

    def _click(self, event):
        self.focus_set()
        return self._activate(event)

    def _destroy(self, event):
        if event.widget == self:
            self.variable.trace_remove('write', self._trace)


class ModeToggle(ttk.Frame):
    """Uma única escolha governa o orçamento exibido e o inventário."""
    def __init__(self, parent, variable):
        super().__init__(parent, padding=(0, 0, 0, 6))
        ttk.Label(self, text='Como obter o item?', style='Small.TLabel').pack(side='left', padx=(0, 12))
        self.buy_label = ttk.Label(self, text='Comprando', cursor='hand2')
        self.buy_label.pack(side='left', padx=(0,6))
        self.switch = ModeSwitch(self, variable)
        self.switch.pack(side='left')
        self.craft_label = ttk.Label(self, text='Fabricando', cursor='hand2')
        self.craft_label.pack(side='left', padx=(6,0))
        self.info = InfoPopup(self)
        self.info_button = info_button(self, self.info, 'Fabricação com Ofício', GENERAL_FABRICATION_RULE)
        self.info_button.pack(side='left', padx=(8,0))
        self.buy_label.bind('<Button-1>', lambda _: variable.set(False))
        self.craft_label.bind('<Button-1>', lambda _: variable.set(True))
        self._variable = variable
        self._trace = variable.trace_add('write', self._update_labels)
        self.bind('<Destroy>', self._destroy)
        self._update_labels()

    def _update_labels(self, *_):
        for label, active in ((self.buy_label, not self._variable.get()),
                              (self.craft_label, self._variable.get())):
            label.configure(foreground='#244cc0' if active else '#69788e',
                            font=('Segoe UI',10,'bold' if active else 'normal'))

    def _destroy(self, event):
        if event.widget == self:
            self._variable.trace_remove('write', self._trace)


class QuoteCards(ttk.Frame):
    def __init__(self, parent, *, expandable=True, characteristics_only=False):
        super().__init__(parent)
        self._fabricating = True
        self._characteristics = None
        self.characteristics_cards = None
        self.expanded = False
        self.characteristics_button = None
        self.values, self.hints, self.titles, self.labels, self.captions = [], [], [], [], []
        self.info = InfoPopup(self)
        for i, title in enumerate(('CUSTO DE FABRICAÇÃO', 'CD DE FABRICAÇÃO', 'TEMPO DE FABRICAÇÃO')):
            self.columnconfigure(i, weight=1, uniform='metrics')
            card = tk.Frame(self, bg='#eef3ff', padx=12, pady=10)
            card.grid(row=0, column=i, sticky='nsew', padx=(0 if i == 0 else 4,0 if i == 2 else 4))
            if characteristics_only and i == 0:
                card.grid_remove()
                self.columnconfigure(0, weight=0, uniform='')
            title_var = tk.StringVar(self, title)
            self.titles.append(title_var)
            tk.Label(card, textvariable=title_var, bg='#eef3ff', fg='#52678e', font=('Segoe UI',8,'bold'), anchor='w').pack(fill='x')
            value, hint = tk.StringVar(self, '—'), tk.StringVar(self)
            self.values.append(value)
            self.hints.append(hint)
            main = tk.Label(card, textvariable=value, bg='#eef3ff', fg='#244cc0', font=('Segoe UI',15,'bold'), anchor='w', justify='left', wraplength=200)
            main.pack(fill='both', expand=True, pady=4)
            self.labels.append(main)
            caption = tk.Label(card, textvariable=hint, bg='#eef3ff', fg='#52678e', font=('Segoe UI',9), anchor='w', justify='left', wraplength=200)
            caption.pack(fill='x')
            self.captions.append(caption)
            card.bind('<Configure>', lambda e, a=main,b=caption: (a.configure(wraplength=max(70,e.width-24)),b.configure(wraplength=max(70,e.width-24))))
        self.effects_host = ttk.Frame(card)
        self.effects = tk.Text(self.effects_host, height=5, width=20, wrap='word', relief='flat',
                               bg='#eef3ff', fg='#24324b', font=('Segoe UI',9), cursor='arrow')
        bar = ttk.Scrollbar(self.effects_host, command=self.effects.yview)
        self.effects.configure(yscrollcommand=bar.set, state='disabled')
        bar.pack(side='right', fill='y')
        self.effects.pack(fill='both', expand=True)
        self.effects_button = info_button(self.effects_host, self.info, 'Efeitos do item', '')
        self.effects_button.pack(anchor='e')
        if expandable:
            self.characteristics_button = ttk.Button(self, text='Mostrar características',
                                                     command=self.toggle_characteristics)
            self.characteristics_button.grid(row=1, column=0, columnspan=3, sticky='w', pady=(6,0))
            self.characteristics_button.configure(state='disabled')

    def toggle_characteristics(self):
        self.expanded = not self.expanded
        self._sync_characteristics()

    def set_characteristics(self, characteristics, effects, *, stats_hint=''):
        self._characteristics = characteristics, effects, stats_hint
        self._sync_characteristics()

    def _sync_characteristics(self):
        if self.characteristics_button is None:
            return
        if self._fabricating:
            self.characteristics_button.grid()
            self.characteristics_button.configure(text='Ocultar características' if self.expanded else 'Mostrar características',
                                                   state='normal' if self._characteristics else 'disabled')
        else:
            self.characteristics_button.grid_remove()
        if self._fabricating and self.expanded and self._characteristics:
            if self.characteristics_cards is None:
                self.characteristics_cards = QuoteCards(self, expandable=False, characteristics_only=True)
            stats, effects, hint = self._characteristics
            self.characteristics_cards.show_purchase(None, stats, effects, stats_hint=hint)
            self.characteristics_cards.grid(row=2, column=0, columnspan=3, sticky='ew', pady=(6,0))
        elif self.characteristics_cards is not None:
            self.characteristics_cards.info.hide()
            self.characteristics_cards.grid_remove()

    def set_mode(self, fabricating):
        self._fabricating = fabricating
        self.info.hide()
        titles = (('CUSTO DE FABRICAÇÃO', 'CD DE FABRICAÇÃO', 'TEMPO DE FABRICAÇÃO') if fabricating
                  else ('PREÇO DE COMPRA', 'CARACTERÍSTICAS DO ITEM', 'EFEITOS EXTRAS / USO'))
        for title, value in zip(self.titles, titles):
            title.set(value)
        for i, label in enumerate(self.labels):
            label.configure(font=('Segoe UI',15 if fabricating or i == 0 else 10,'bold'), fg='#244cc0')
            self.captions[i].configure(fg='#52678e')
        self.effects_host.pack_forget()
        self._sync_characteristics()

    def clear(self):
        self._characteristics = None
        self.info.hide()
        self.effects_host.pack_forget()
        for var in self.values:
            var.set('—')
        for var in self.hints:
            var.set('')
        if self.characteristics_cards is not None:
            self.characteristics_cards.clear()
        self._sync_characteristics()

    def show_quote(self, fabrication, unit_cost=None, market_price=None, quantity=1):
        self.set_mode(True)
        self.values[0].set(format_money(fabrication.cost))
        self.values[1].set(fabrication.dc_label)
        self.values[2].set(fabrication.time_label)
        unit = fabrication.cost / quantity if unit_cost is None else unit_cost
        self.hints[0].set(f'Unitário: {format_money(unit)} · {quantity} unidade(s)')
        self.hints[1].set(f'Penalidade do lote {fabrication.penalty:+d}' if fabrication.penalty else 'Teste de Ofício' if fabrication.dc is not None else 'Método sem teste')
        self.hints[2].set(f'{fabrication.units_per_day} unidade(s) por lote' if fabrication.days else fabrication.temporary or 'Método especial')
        if fabrication.penalty < 0:
            self.captions[1].configure(fg='#b3261e')

    def highlight_dc_increase(self, increase):
        if increase > 0:
            self.labels[1].configure(fg='#b3261e')
            self.captions[1].configure(fg='#b3261e')
            self.hints[1].set(self.hints[1].get()+f' · CD +{increase} pelos modificadores')

    def show_purchase(self, price, characteristics, effects, *, quantity=1, price_hint='', stats_hint=''):
        self.set_mode(False)
        self.values[0].set(format_money(price*quantity) if price is not None else 'Sem cotação')
        if price is not None:
            self.hints[0].set(f'Unitário: {format_money(price)} · {quantity} unidade(s)'
                              + ('\n'+price_hint if price_hint else ''))
        else:
            self.hints[0].set(price_hint or 'Informe uma cotação de mercado')
        self.values[1].set(characteristics)
        self.hints[1].set(stats_hint)
        self.values[2].set('Efeitos do item pronto')
        self.hints[2].set('Role para ler os efeitos completos')
        self.effects.configure(state='normal')
        self.effects.delete('1.0', 'end')
        self.effects.insert('1.0', effects or 'Sem efeitos extras nesta configuração.')
        self.effects.configure(state='disabled')
        description = effects or 'Sem efeitos extras nesta configuração.'
        if len(description) > 1000:
            description = description[:1000].rsplit(' ', 1)[0]+'…\n\nContinue a leitura na área rolável do cartão.'
        self.info.attach(self.effects_button, 'Efeitos do item pronto', description)
        self.effects_host.pack(fill='both', expand=True, pady=(6,0))
