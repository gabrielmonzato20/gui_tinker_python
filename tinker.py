from tkinter import *
from tkinter import messagebox
from db import Db
db = Db('location.db') 

def index():
   part_list.delete(0,END)
   for linha in db.index():
       part_list.insert(END,linha)

def update_item():
    db.update(selected_item[0],text_costumer.get(),text_retail.get(),text_part.get(),text_price.get())
    index()



def add_item():
    if text_price.get() == '' or text_retail.get() == '' or text_costumer == '' or text_part.get() == '' or text_price.get() == '':
        messagebox.showerror("Campos obrigatorios",'Por favor Preencha todos')
        return 

    db.inserir(text_price.get(),text_retail.get(),text_costumer.get(),text_part.get())
    part_list.delete(0,END)
    part_list.insert(END,(text_price.get(),text_retail.get(),text_costumer.get(),text_part.get()))
    index()
    
def clear_list():    
    form_part.delete(0,END)
    form_retail.delete(0,END)
    form_costumer.delete(0,END)
    form_price.delete(0,END)



def remove_item():
    db.destroy(selected_item[0])
    index()
    clear_list()
    


def select_item(event):
    try:
        global selected_item
        index = part_list.curselection()[0]
        selected_item = part_list.get(index)
        print(selected_item)
        form_part.delete(0,END)
        form_part.insert(END,selected_item[4])

        form_retail.delete(0,END)
        form_retail.insert(END,selected_item[2])
        
        form_costumer.delete(0,END)
        form_costumer.insert(END,selected_item[3])
        
        form_price.delete(0,END)
        form_price.insert(END,selected_item[1])
    except  IndexError:
        pass



ap = Tk()
text_part = StringVar()

label_part = Label(ap,text = 'Texto ', font = ('bold',17),pady=20)
label_part.grid(row=0,column=0,sticky=W)
form_part = Entry(ap,textvariable=text_part)
form_part.grid(row=0,column=1)



text_costumer = StringVar()
label_costumer = Label(ap,text = 'Cliente ', font = ('bold',17))
label_costumer.grid(row=0,column=2,sticky=W)
form_costumer = Entry(ap,textvariable=text_costumer)
form_costumer.grid(row=0,column=3)


text_retail = StringVar()
label_retail= Label(ap,text = 'Aluguel ', font = ('bold',17),pady=20)
label_retail.grid(row=1,column=0,sticky=W)
form_retail = Entry(ap,textvariable=text_retail)
form_retail.grid(row=1,column=1)


text_price = StringVar()
label_price  = Label(ap,text = 'Preço ', font = ('bold',17))
label_price.grid(row=1,column=2,sticky=W)
form_price  = Entry(ap,textvariable=text_price)
form_price.grid(row=1,column=3)
#parts
part_list = Listbox(ap,height=4,width=120)
part_list.grid(row=3,column=0,columnspan=6,rowspan=6,pady=10,padx=10)
#scrool bar 
scrollbar = Scrollbar(ap)
scrollbar.grid(row=3,column=0)
part_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command =part_list.yview)
#bind select 
part_list.bind('<<ListboxSelect>>',select_item)
#btn
add_btn = Button(ap,text='Adicionar',width=12,command=add_item)
add_btn.grid(row=2, column=0,pady=20)

clear_btn = Button(ap,text='Limpar',width=12,command=clear_list)
clear_btn.grid(row=2, column=1)

remove_btn = Button(ap,text='Remover',width=12,command=remove_item)
remove_btn.grid(row=2, column=2)

update_btn = Button(ap,text='Atualizar',width=12,command=update_item)
update_btn.grid(row=2, column=3)

ap.title('Gerenciamento')
ap.geometry('750x750')
index()
ap.mainloop()