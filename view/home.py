from tkinter import *

def semComando():
    print('')

#Configurações da tela
app=Tk()
app.title('ADL Sistemas - Home')
app.geometry('1000x500')

btn1= Button(text='Sistemas', command=semComando, height= 18, width=20, fg='white', bg='black', font='Helvetica 14')
btn2= Button(text='Perfis', command=semComando, height= 18, width=20, fg='white', bg='black', font='Helvetica 14')
btn3= Button(text='Matriz', command=semComando, height= 18, width=20, fg='white', bg='black', font='Helvetica 14')
btn4= Button(text='Usuários', command=semComando, height= 18, width=20, fg='white', bg='black', font='Helvetica 14')

btn1.grid(row=0, column=2, padx=10, pady=10)
btn2.grid(row=0, column=3, padx=10, pady=10)
btn3.grid(row=0, column=4 , padx=10, pady=10)
btn4.grid(row=0, column=5, padx=10, pady=10)



#Loop principal do app
app.mainloop()