from tkinter import *
from klasa import *


root=Tk()
root.title("Posiljke")
def dodaj_posiljku():
    t=Toplevel(root)

    Label(t,text="Posiljalac").grid(row=0,column=0)
    Label(t,text="Primalac").grid(row=1,column=0)
   
    e1_t=Entry(t)
    e1_t.grid(row=0,column=1,columnspan=2)
    e2_t=Entry(t)
    e2_t.grid(row=1,column=1,columnspan=2)
    
    b_t=Button(t,text="Dodaj posiljku",command=lambda:p.dodaj_posiljku(e1_t.get(),e2_t.get()))
    b_t.grid(row=2,column=0,columnspan=2)

def promeni_status():
    t=Toplevel(root)
    
    var1 = StringVar(t) 
    var1.set("poslato") 
    r1=Radiobutton(t, text="poslato", variable=var1, value="poslato")
    r2=Radiobutton(t, text="otpremljeno", variable=var1, value="otpremljeno")
    r3=Radiobutton(t, text="dostavljeno", variable=var1, value="dostavljeno")

    r1.grid(row=0,column=0)
    r2.grid(row=1,column=0)
    r3.grid(row=2,column=0)

    b_e=Button(t,text="Promeni status",command=lambda:p.promeni_status(var1.get()))
    b_e.grid(row=3,column=0)
    
def export():
    t=Toplevel(root)
    
    b_t1=Button(t,text="Excel",command=lambda:p.export_excel())
    b_t1.grid(row=0,column=1)
    
    b_t2=Button(t,text="CSV",command=lambda:p.export_csv())
    b_t2.grid(row=0,column=2)

# list=p.listbox()
# list=pd.DataFrame(list)
listbox=Listbox(root)
# for i in range(len(list)):
#     listbox.insert(i+1,list.loc[0:len(list),('broj_posiljke','posiljalac','primalac','status')])
#     i+=1
listbox.grid(row=0,column=0,rowspan=9) 



b_dodaj=Button(root,text="Dodaj posiljku",height=3,command=lambda:dodaj_posiljku())
b_dodaj.grid(row=0,column=1,rowspan=3)

b_promeni=Button(root,text="Promeni status",height=3,command=lambda:promeni_status())
b_promeni.grid(row=3,column=1,rowspan=3)

b_export=Button(root,text="Export",height=3,command=lambda:export())
b_export.grid(row=6,column=1,rowspan=3)


mainloop()