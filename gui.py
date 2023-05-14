from klasa import *
from tkinter import *



root=Tk()




def dodaj_posiljku():
    t=Toplevel()
    Label(t,text='posiljalac').grid(row=0,column=0)
    Label(t,text='primalac').grid(row=1,column=0)
    
    posiljalac=Entry(t)
    posiljalac.grid(row=0,column=1,columnspan=2)
    primalac=Entry(t)
    primalac.grid(row=1,column=1,columnspan=2)
    status='poslato'

    button_dodaj=Button(t,text='Dodaj',command=lambda:P.dodaj_posiljku(posiljalac.get(),primalac.get(),status))
    button_dodaj.grid(row=2,column=0,columnspan=2)

def promeni_status():
    t=Toplevel()
    var2=StringVar(t)
    var2.set('poslato') # u zagradi treba da stoji aktivan status izabramne posiljke
    r1=Radiobutton(t,text='poslato',variable=var2,value='poslato')
    r1.grid(row=0,column=0)
    r2=Radiobutton(t,text='otpremljeno',variable=var2,value='otpremljeno')
    r2.grid(row=0,column=1)
    r3=Radiobutton(t,text='dostavljeno',variable=var2,value='dostavljeno')
    r3.grid(row=0,column=2)

    button_promeni=Button(t,text='Promeni status',command=lambda:P.promeni_status(var2.get()))
    button_promeni.grid(row=1,column=1)

def export():
    t=Toplevel()
    var2=StringVar(t)
    var2.set('excel') 
    r1=Radiobutton(t,text='excel',variable=var2,value='excel')
    r1.grid(row=0,column=0)
    r2=Radiobutton(t,text='csv',variable=var2,value='csv')
    r2.grid(row=0,column=1)

    button_export=Button(t,text='Export',command=lambda:P.export(var2.get())) # P.export(excel/csv) treba funcija da prima jednu od dve opcije
    button_export.grid(row=0,column=2)

button_dodaj=Button(root,text='Dodaj posiljku',height=3,command=lambda:dodaj_posiljku())
button_promeni=Button(root,text='Promeni status',height=3,command=lambda:promeni_status())
button_export=Button(root,text='Export',height=3,command=lambda:export())

button_dodaj.grid(row=0,column=1,rowspan=3)
button_promeni.grid(row=2,column=1,rowspan=3)
button_export.grid(row=6,column=1,rowspan=3)


listbox=Listbox(root)
listbox.grid(row=0,column=0,rowspan=9) # columnspan=len(posiljke)=koliko ima redova u db iz postgresa

mainloop()