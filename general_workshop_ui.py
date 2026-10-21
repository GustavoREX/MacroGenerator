"""Oficina Geral: consulta de receitas, CD, matéria-prima e tempo."""
import tkinter as tk
from tkinter import ttk

from crafting_core import money, format_money
from fabrication import Creator
from fabrication_ui import CreatorPanel
from forge_ui import QuoteCards, InfoPopup, info_button, ModeToggle, set_visible
from general_workshop_core import (ITEMS, ORNITHOPTER_MODS, GeneralDesign, find_general_items,
    quote_general, general_item, item_rules)


class GeneralWorkshopPanel(ttk.Frame):
    def __init__(self,master,app):
        super().__init__(master,padding=(0,6))
        self.app,self.result,self._job,self._building=app,None,None,True
        self.item_id=''
        self.info=InfoPopup(self)
        self.vars={}
        self.fabricate_var=tk.BooleanVar(self,True)
        self.fabrication_widgets=[]
        self.modification_vars={}
        self.innovation_vars={}
        body=ttk.Panedwindow(self,orient='horizontal')
        body.pack(fill='both',expand=True)
        left,right=ttk.Frame(body,width=300),ttk.Frame(body)
        body.add(left,weight=1)
        body.add(right,weight=3)
        self.settings_tabs=ttk.Notebook(left)
        self.settings_tabs.pack(fill='both',expand=True)
        recipe=ttk.Frame(self.settings_tabs)
        self.settings_tabs.add(recipe,text='Receita')
        self.creator_panel=CreatorPanel(self.settings_tabs,app,self.schedule,scope='general')
        self.settings_tabs.add(self.creator_panel,text='Modificadores')
        content=app.create_scrollable_panel(recipe,padx=5,pady=6)
        def field(key,label,value='',values=None):
            ttk.Label(content,text=label,wraplength=260).pack(anchor='w',pady=(8,3))
            var=self.vars[key]=tk.StringVar(self,value)
            widget=ttk.Combobox(content,textvariable=var,values=values,state='readonly') if values else ttk.Entry(content,textvariable=var)
            widget.pack(fill='x')
            return widget
        field('quantity','Quantidade de unidades / pacotes','1')
        field('price','Preço de mercado ajustado (T$; opcional)')
        self.fabrication_widgets.append(field('dc','CD ajustada (opcional)'))
        self.fabrication_widgets.append(field('days','Tempo-base por unidade (dias; opcional)'))
        field('extra','Gasto adicional por unidade (T$)','0')
        self.vars['double']=tk.BooleanVar(self,False)
        row=ttk.Frame(content)
        row.pack(fill='x',pady=8)
        batch=ttk.Checkbutton(row,text='Produzir em lote (–5)',variable=self.vars['double'])
        batch.pack(side='left')
        ttk.Style(self).configure('Penalty.TCheckbutton',foreground='#b3261e')
        self.vars['double'].trace_add('write',lambda *_: batch.configure(style='Penalty.TCheckbutton' if self.vars['double'].get() else 'TCheckbutton'))
        self.fabrication_widgets.append(batch)
        info_button(row,self.info,'Produção em lote','Consumíveis: duas unidades no mesmo tempo com –5 no teste. Pratos especiais: até cinco por hora com –5. Paga a matéria-prima de todas as unidades. T20, p. 122 e 162. Itens não consumíveis mantêm seu tempo por unidade.').pack(side='right')
        dish_names=[r['name'] for r in ITEMS.values() if r['category']=='Alimentos e bebidas' and item_rules(r)[4]==5]
        self.dish_host=self.creator_panel.distinction_fields['À Moda da Casa']
        ttk.Label(self.dish_host,text='Segundo prato',wraplength=260).pack(anchor='w',pady=(6,2))
        self.vars['dish']=tk.StringVar(self,'Nenhum')
        self.dish_combo=ttk.Combobox(self.dish_host,textvariable=self.vars['dish'],values=('Nenhum',*dish_names),state='readonly')
        self.dish_combo.pack(fill='x')
        self.creator_panel.distinction_vars['À Moda da Casa'].trace_add('write',
            lambda *_: set_visible(self.dish_host,self.creator_panel.distinction_vars['À Moda da Casa'].get()))
        self.mode_toggle=ModeToggle(self,self.fabricate_var)
        self.mode_toggle.pack(fill='x',before=body)
        self.cards=QuoteCards(self)
        self.cards.pack(fill='x',pady=(0,8),before=body)
        self.comparison_var=tk.StringVar(self)
        comparison=ttk.Label(self,textvariable=self.comparison_var,style='Small.TLabel',wraplength=900)
        comparison.pack(anchor='w',pady=(0,7),before=body)
        self.bind('<Configure>',lambda e: comparison.configure(wraplength=max(240,e.width-24)) if e.widget==self else None,add='+')
        filters=ttk.Frame(right)
        filters.pack(fill='x',pady=(0,6))
        self.search=tk.StringVar(self)
        ttk.Entry(filters,textvariable=self.search).pack(side='left',fill='x',expand=True,padx=(0,5))
        self.category=tk.StringVar(self,'Todos')
        ttk.Combobox(filters,textvariable=self.category,values=('Todos',*sorted({r['category'] for r in ITEMS.values()})),state='readonly',width=24).pack(side='right')
        catalog=ttk.Panedwindow(right,orient='horizontal')
        catalog.pack(fill='both',expand=True)
        list_host,detail_host=ttk.Frame(catalog,width=230),ttk.Frame(catalog)
        catalog.add(list_host,weight=1)
        catalog.add(detail_host,weight=3)
        self.tree=ttk.Treeview(list_host,show='tree',selectmode='browse')
        bar=ttk.Scrollbar(list_host,command=self.tree.yview)
        self.tree.configure(yscrollcommand=bar.set)
        bar.pack(side='right',fill='y')
        self.tree.pack(fill='both',expand=True)
        self.details=app.create_scrollable_panel(detail_host,padx=12,pady=5)
        footer=ttk.Frame(self,padding=(0,6))
        footer.pack(side='bottom',fill='x',before=body)
        footer_details=ttk.Frame(footer)
        footer_details.pack(fill='x')
        self.summary_var,self.error_var,self.status_var=(tk.StringVar(self) for _ in range(3))
        self.summary_label=ttk.Label(footer_details,textvariable=self.summary_var,wraplength=1100)
        self.error_label=ttk.Label(footer_details,textvariable=self.error_var,foreground='#b3261e',wraplength=1100)
        self.add_button=ttk.Button(footer,text='Adicionar ao inventário',style='Primary.TButton',command=self.add_inventory)
        self.add_button.pack(side='right')
        ttk.Label(footer,textvariable=self.status_var,wraplength=700).pack(side='left')
        self.tree.bind('<<TreeviewSelect>>',self.select_item)
        for var in (self.search,self.category):
            var.trace_add('write',self.filter_items)
        for var in self.vars.values():
            var.trace_add('write',self.schedule)
        self.fabricate_var.trace_add('write',self.schedule)
        self._building=False
        self.filter_items()

    def filter_items(self,*_):
        rows=find_general_items(self.search.get(),self.category.get())
        old=self.tree.selection()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert('', 'end', iid=row['id'],text=row['name'])
        selected=old[0] if old and self.tree.exists(old[0]) else rows[0]['id'] if rows else ''
        if selected:
            self.tree.selection_set(selected)
            self.select_item()
        else:
            self.item_id=''
            for w in self.details.winfo_children():
                w.destroy()
            self.refresh()

    def select_item(self,_event=None):
        selected=self.tree.selection()
        if not selected or selected[0]==self.item_id:
            return
        self.item_id=selected[0]
        item=ITEMS[self.item_id]
        for w in self.details.winfo_children():
            w.destroy()
        self.modification_vars={}
        self.innovation_vars={}
        self.vars['price'].set('')
        self.vars['dc'].set('')
        self.vars['days'].set('')
        self.vars['double'].set(False)
        self.vars['extra'].set('0')
        def label(text,style='TLabel'):
            w=ttk.Label(self.details,text=text,wraplength=500,justify='left',style=style)
            w.pack(fill='x',anchor='w',pady=6)
            w.bind('<Configure>',lambda e:w.configure(wraplength=max(120,e.width-10)))
        label(item['name'],'Section.TLabel')
        label(item['category']+' · '+item.get('group',''),'Small.TLabel')
        label(item['description'])
        label(item.get('source',''),'Small.TLabel')
        if self.item_id=='recipe:ornitoptero':
            label('Engenharia Aeronáutica · Melhorias','Section.TLabel')
            for name,description in ORNITHOPTER_MODS.items():
                row=ttk.Frame(self.details)
                row.pack(fill='x',pady=3)
                var=self.modification_vars[name]=tk.BooleanVar(self,False)
                ttk.Checkbutton(row,text=name,variable=var).pack(side='left')
                info_button(row,self.info,name,description+' Heróis de Arton, p. 108.').pack(side='right')
                var.trace_add('write',self.schedule)
        if item['category']=='Munições' and 'Balas' in item['name']:
            from innovation_data import INNOVATIONS
            label('Mestre de Armearia · Inovações','Section.TLabel')
            for name,entry in INNOVATIONS.items():
                if entry['target']!='ammunition':
                    continue
                row=ttk.Frame(self.details)
                row.pack(fill='x',pady=3)
                var=self.innovation_vars[name]=tk.BooleanVar(self,False)
                ttk.Checkbutton(row,text=name,variable=var).pack(side='left')
                info_button(row,self.info,name,entry['description']+' Deuses de Arton, p. 110–111.').pack(side='right')
                var.trace_add('write',self.schedule)
        self.schedule()

    def get_design(self):
        v=self.vars
        try:
            quantity=int(v['quantity'].get())
            dc=int(v['dc'].get()) if self.fabricate_var.get() and v['dc'].get().strip() else None
        except ValueError:
            raise ValueError('Quantidade e CD devem ser números inteiros.') from None
        second=next((r['id'] for r in ITEMS.values() if r['name']==v['dish'].get()),'') if self.creator_panel.distinction_vars['À Moda da Casa'].get() else ''
        return GeneralDesign(self.item_id,quantity,v['double'].get() if self.fabricate_var.get() else False,
            money(v['price'].get()) if v['price'].get().strip() else None,dc,money(v['extra'].get()),second,
            tuple(n for n,var in self.modification_vars.items() if var.get()),
            tuple(n for n,var in self.innovation_vars.items() if var.get()),
            money(v['days'].get()) if self.fabricate_var.get() and v['days'].get().strip() else None)

    def schedule(self,*_):
        if not self._building and self._job is None:
            self._job=self.after_idle(self.refresh)

    def refresh(self):
        if self._job is not None:
            self.after_cancel(self._job)
            self._job=None
        self.result=None
        fabricating=self.fabricate_var.get()
        self.cards.set_mode(fabricating)
        if not fabricating:
            self.settings_tabs.select(0)
        self.settings_tabs.tab(self.creator_panel,state='normal' if fabricating else 'disabled')
        self.settings_tabs.tab(0,text='Receita' if fabricating else 'Item')
        for widget in self.fabrication_widgets:
            widget.configure(state='normal' if fabricating else 'disabled')
        try:
            if not self.item_id:
                raise ValueError('Nenhum item corresponde aos filtros.')
            d=self.get_design()
            c=self.creator_panel.get_creator() if fabricating else Creator()
            q=quote_general(d,c,purchase=not fabricating)
            item=q.item
            stats=item['category']
            if item.get('group'):
                stats+='\n'+item['group']
            stats+='\nEspaços: '+str(item.get('spaces') or 'Não informado')
            if fabricating:
                self.cards.show_quote(q.fabrication,q.unit_cost,q.market_price,d.quantity)
                self.cards.set_characteristics(stats,q.description,stats_hint=item.get('source',''))
                self.summary_var.set('Fabricando · Lote: '+format_money(q.fabrication.cost)+'\n'+'\n'.join(q.fabrication.notes))
                from dataclasses import replace
                base=quote_general(replace(d,second_dish=''),Creator())
                self.comparison_var.set('Sem modificadores: '+format_money(base.unit_cost)+
                    f' / unidade · CD {base.fabrication.dc_label} · {base.fabrication.time_label}')
            else:
                self.cards.show_purchase(q.market_price,stats,q.description,quantity=d.quantity,
                    stats_hint=item.get('source',''))
                self.comparison_var.set('')
                self.summary_var.set('Comprando · Total: '+format_money(q.market_price*d.quantity) if q.market_price is not None
                                     else 'Sem preço de compra para esta configuração. Informe uma cotação quando o item permitir comercialização.')
            self.error_var.set('')
            self.result=d,c,q
        except ValueError as error:
            self.result=None
            self.cards.clear()
            self.comparison_var.set('')
            self.summary_var.set('')
            self.error_var.set(str(error))
        self.summary_label.pack_forget()
        self.error_label.pack_forget()
        if not fabricating:
            self.summary_label.pack(anchor='w')
        if self.error_var.get():
            self.error_label.pack(anchor='w',pady=3)
        self.add_button.configure(state='normal' if self.result and (fabricating or self.result[2].market_price is not None) else 'disabled')

    def add_inventory(self):
        self.refresh()
        if self.result:
            d,c,q=self.result
            try:
                self.app.add_inventory_item(general_item(d,c,q,purchase=not self.fabricate_var.get()),d.quantity)
                self.status_var.set(f'{d.quantity}× {q.item["name"]}: inventário salvo.')
            except (ValueError,OSError) as error:
                self.status_var.set(str(error))

    def destroy(self):
        if self._job is not None:
            self.after_cancel(self._job)
        self.info.hide()
        super().destroy()
