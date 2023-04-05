from tkinter import *

def semComando():
    print('')


#Configurações da tela
app=Tk()
app.title('ADL sistemas')
app.geometry('400x200')

#Definição de menu
menus = Menu(app)
app.config(menu=menus)

#Menu de cadastro
menuCadastro = Menu(menus,tearoff=0)
menuCadastro.add_command(label='Cadastro de sistema',command=semComando)
menuCadastro.add_command(label='Cadastro de perfil',command=semComando)
menuCadastro.add_command(label='Cadastro de Matriz SoD',command=semComando)

#Menu de consulta
menuConsulta = Menu(menus, tearoff=0)
menuConsulta.add_command(label='Consulta de sistema',command=semComando)
menuConsulta.add_command(label='Consulta de perfil',command=semComando)
menuConsulta.add_command(label='Consulta de Matriz SoD',command=semComando)

#Menus
menus.add_cascade(label='Cadastro',menu=menuCadastro)
menus.add_cascade(label='Consulta',menu=menuConsulta)

lb1= Label(app, text='Menus',bg='#dde',fg='#009',anchor=W,)
lb1.pack()

#Loop principal do app
app.mainloop()