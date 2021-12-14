#importamos tk
try:
    import tkinter as tk
    import wikipedia #pip install wikipedia
except Exception as e:print(f'[!] e: {e}')

def inf(n):
    print(n)
    n = int(n) if n!= '' else 0
    return 'par' if n%2==0 else 'impar'
    
def wikiSearch(q):
    try:
        wikipedia.set_lang('es')
        p = wikipedia.page(f'numero {q}')
        text = p.content
        
        text_widget.delete((1.0),tk.END)
        text_widget.insert(tk.END,text)
        text_widget.pack()

    except Exception as e:
        print(f'[!] e: {e}')

def save():
    pass
 
def settings():
    window = tk.Toplevel()
    window.geometry('150x150')
    newlabel = tk.Label(window, text = "Settings Window")
    newlabel.pack()  

def search():
    number = entry_num.get()
    info = tk.Label(basicinfo_frame,text=inf(number))
    info.pack()
    wikiSearch(number)

def number_info():
    #creamos y configuramos la ventana principal
    root = tk.Tk()
    root.geometry("400x250")

    #menu
    frame = tk.Frame(root)
    frame.pack()
    
    mainmenu = tk.Menu(frame)
    mainmenu.add_command(label = "Save", command= save)  
    mainmenu.add_command(label = "Settings", command= settings)
    mainmenu.add_command(label = "Exit", command= root.destroy)
    root.config(menu = mainmenu)

    #variable que contiene el numero seleccionado
    number = tk.StringVar()   

    #creamos una scrolbar
    myscroll = tk.Scrollbar(root) 
    myscroll.pack(side = 'right', fill = 'y') 

    #textwidget para alojar texto de wikipedia
    global text_widget
    text_widget = tk.Text(root,width=200, height=30,yscrollcommand=myscroll.set,autoseparators=True)
    myscroll.config(command = text_widget.yview)

    #search num widgets
    enternum_frame = tk.LabelFrame(root,text="Enter a num",padx=35,pady=25)
    global entry_num
    entry_num = tk.Entry(enternum_frame,textvariable=number,relief='sunken')
    entry_num.pack()

    submit_button= tk.Button(enternum_frame,command=search,text='continue',relief='raised')
    submit_button.pack()

    #basic info
    global basicinfo_frame
    basicinfo_frame = tk.LabelFrame(root,text="Basic info",padx=35)

    enternum_frame.pack()
    basicinfo_frame.pack()

    #finalizamos con un bucle infinito
    root.mainloop()

def tributar():
    global anos, ingresos, ww,t
    ww = tk.Tk()
    ww.geometry('200x250')
    
    edad_frame = tk.LabelFrame(ww,text="Edad",padx=35,pady=25)
    anos = tk.Entry(edad_frame)
    anos.pack()
    ent_frame = tk.LabelFrame(ww,text="Ingresos (mensuales)",padx=35,pady=25)
    ingresos = tk.Entry(ent_frame)
    ingresos.pack()
    bb = tk.Button(ww,text='Comprobar',command=getText)

    edad_frame.pack()
    ent_frame.pack()
    bb.pack()
    t =tk.Text(ww)
    ww.mainloop()


def getText():
    text = 'debe' if int(anos.get()) >= 16 and int(ingresos.get())>=1000 else 'no debe'
    t.delete((1.0),tk.END)
    t.insert(tk.END,f'Usted {text} tributar.')
    t.pack()

def number_operations():
    global widget
    widget = tk.Tk()
    widget.geometry('600x100')
    global fnum,snum
    fnum = tk.Entry(widget);fnum.grid(row=0,column=1)
    snum = tk.Entry(widget);snum.grid(row=0,column=3)
    bb = tk.Button(widget,text='Comprobar',command=operate);bb.grid(row=1)
    global control_variable
    control_variable = tk.StringVar(widget)
    OPTION_TUPLE = ("Sumar", "Restar", "Dividir",'Multiplicar') 
    optionmenu_widget = tk.OptionMenu(widget,control_variable, *OPTION_TUPLE)
    optionmenu_widget.grid(row=0,column=2)
    tk.Label(widget,text=' = ').grid(row=0,column=4)
    widget.mainloop()

def operate():
    n=fnum.get()
    m=snum.get()
    print('controlvariable: ',control_variable)
    o = control_variable.get()
    op = '+' if o=='Sumar' else '-' if o=='Restar' else '*' if o=='Multiplicar' else '/'
    tk.Label(widget,text=eval(str(n)+op+str(m))).grid(row=0,column=6)
        

def main():
    w = tk.Tk()
    tk.Button(w,text='Informacion sobre numeros',command=number_info).pack()
    tk.Button(w,text='Operaciones con numeros',command=number_operations).pack()
    tk.Button(w,text='Tributar',command=tributar).pack()
    tk.Button(w,text='Cerrar',command=w.destroy).pack()
    w.mainloop()

if __name__ == '__main__':
    main()
