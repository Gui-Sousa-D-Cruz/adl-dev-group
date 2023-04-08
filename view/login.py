from tkinter import *

def semComando():
    print('clicou')

#Configurações da tela
app=Tk()
app.title('ADL Sistemas - Login')
app.geometry('400x400')

lb_nome = Label(app, text='ADL Sistemas - Login', font='Helvetica 20', fg='white', bg='red')
lb_nome.pack(pady=20, ipady=20, ipadx=10)

lb1= Label(app, text='Usuário:', font='Helvetica 14')
lb1.pack()

inp1= Entry(app)
inp1.pack(ipadx=50, ipady=5)

spacer = Label(app, text='', font='Helvetica 14')
spacer.pack()

lb2= Label(app, text='Senha:', font='Helvetica 14')
lb2.pack()

inp2= Entry(app, show="*")
inp2.pack(ipadx=50, ipady=5)

spacer1 = Label(app, text='', font='Helvetica 14')
spacer1.pack()

btn1= Button(text='Entrar', command=semComando, font='Helvetiva 10', bg='black', fg='white' )
btn1.pack(pady=10, ipady=5, ipadx=5)

#Loop principal do app
app.mainloop()