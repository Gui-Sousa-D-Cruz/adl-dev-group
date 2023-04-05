from tkinter import *

def semComando():
    print('')

#Configurações da tela
app=Tk()
app.title('ADL sistemas')
app.geometry('400x200')

lb1= Label(app, text='Codigo do sistema:')
lb1.pack(pady=5)

inp1= Entry(app)
inp1.pack(ipadx=50)

lb2= Label(app, text='Nome do perfil:')
lb2.pack(pady=5)

inp2= Entry(app)
inp2.pack(ipadx=50)

lb3= Label(app, text='Descrição do perfil:')
lb3.pack(pady=5)

inp3= Entry(app)
inp3.pack(ipadx=50)



btn1= Button(text='Cadastrar', command=semComando)
btn1.pack(pady=10)

#Loop principal do app
app.mainloop()