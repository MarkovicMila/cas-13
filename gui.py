from klasa import *
from tkinter import *
root=Tk()
root.title('Posta')
def dodaj_osobu():
    t=Toplevel(root)
    Label(t,text='Posiljalac').grid(row=0,column=0)
    Label(t,text='Primalac').grid(row=1,column=0)
    
    e1_t=Entry(t)
    e1_t.grid(row=0,column=1,columnspan=2)
    e2_t=Entry(t)
    e2_t.grid(row=1,column=1,columnspan=2)
    

    b_t=Button(t,text='Dodaj',command=lambda:P.dodaj_posiljku(e1_t.get(),e2_t.get()))
    b_t.grid(row=2,column=0,columnspan=3)

def export():
    t=Toplevel(root)
    button_excel=Button(t,text='Excel',command=lambda:P.export_excel())
    button_excel.grid(row=0,column=1)

    button_csv=Button(t,text='CSV',command=lambda:P.export_csv())
    button_csv.grid(row=0,column=2)

def promeni_status():
    t=Toplevel(root)

    var2=StringVar(t)
    var2.set('poslato')
    r1=Radiobutton(t,text='poslato',variable=var2,value='poslato')
    r2=Radiobutton(t,text='na isporuci',variable=var2,value='na isporuci')
    r3=Radiobutton(t,text='primljeno',variable=var2,value='primljeno')
    r1.grid(row=4,column=1)
    r2.grid(row=4,column=2)
    r3.grid(row=4,column=3)

# def export_table(upit,naziv):
#     L.kreiraj_upit(upit)
#     L.get_sql()
#     L.export_excel(naziv)

button_export=Button(root,text='Export',command=lambda:export())
button_export.grid(row=0,column=2,rowspan=2)

button_dodaj=Button(root,text='Dodaj',command=lambda:dodaj_osobu())
button_dodaj.grid(row=2,column=2,rowspan=2)

button_promeni_status=Button(root,text='Promeni status',command=lambda:promeni_status())
button_promeni_status.grid(row=4,column=2,rowspan=2)

listbox=Listbox(root)
listbox.grid(row=0,column=1,rowspan=6)

# menubar=Menu(root)
# dodaj_menu=Menu(menubar,tearoff=0)
# dodaj_menu.add_command(label='Dodaj coveka',command=lambda:dodaj_osobu())
# menubar.add_cascade(label='Dodaj',menu=dodaj_menu)

# m="SELECT * FROM LJUDI WHERE POL='M' "
# b_m=Button(root,text='Export M',height=3,command=lambda:export_table(m,'MUSKARCI'))
# b_m.grid(row=0,column=0,rowspan=2)

# z="SELECT * FROM LJUDI WHERE POL='Z' "
# b_z=Button(root,text='Export Z',height=3,command=lambda:export_table(z,'ZENE'))
# b_z.grid(row=3,column=0,rowspan=2)


# var1=StringVar()
# var1.set('ORDER BY JMBG ASC')
# r1=Radiobutton(root,text='Ime',variable=var1,value='ORDER BY IME ASC')
# r2=Radiobutton(root,text='Prezime',variable=var1,value='ORDER BY PREZIME ASC')
# r3=Radiobutton(root,text='Godine',variable=var1,value='ORDER BY GODINE ASC')

# r1.grid(row=0,column=1)
# r2.grid(row=1,column=1)
# r3.grid(row=2,column=1)

# b_e=Button(root,text="Export",command=lambda:export_table("SELECT * FROM LJUDI {}".format(var1.get()),"Ljudi_Sort"))
# b_e.grid(row=3,column=1)

# root.config(menu=menubar)

mainloop()