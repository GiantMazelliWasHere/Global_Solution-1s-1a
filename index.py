from tkinter import *

def caixa_de_cadastro():
    pacientes = []
    
    nome = nome_tf.get()
    idade = idade_tf.get()
    cid = cid_tf.get()
    
    paciente = {'Nome':nome, 'Idade':idade, 'Cid':cid}
    pacientes.append(paciente)
    
    disp_tf.insert(0, f'{paciente["Nome"]}; {paciente["Idade"]} anos; {paciente["Cid"]}')
    disp_msg.insert(0, f'Cadastro realizado com sucesso!')
    
ws = Tk()
ws.title("Cadastro de Pacientes")
ws.geometry('400x300')
ws.config(bg='#de923e')

nome_tf = Entry(ws)
idade_tf = Entry(ws)
cid_tf = Entry(ws)

nome_lbl = Label(ws, text='Nome', bg='#de923e', fg='white')
idade_lbl = Label(ws, text='Idade', bg='#de923e', fg='white')
cid_lbl = Label(ws, text='CID', bg='#de923e', fg='white')

nome_lbl.pack()
nome_tf.pack()
idade_lbl.pack()
idade_tf.pack()
cid_lbl.pack()
cid_tf.pack()

btn = Button(ws, text='Cadastrar', relief=SOLID, command=caixa_de_cadastro)
btn.pack(pady=10)

disp_tf = Entry(ws, width=38, font=('Arial', '12'))
disp_tf.pack(pady=5)

disp_msg = Entry(ws, width=38, font=('Arial', '12'), bg='#de923e')
disp_msg.pack(pady=5)

ws.mainloop()