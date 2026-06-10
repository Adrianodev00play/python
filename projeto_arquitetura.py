import os
import tkinter as tk

def criar():
    with open("meu arquivo.py", "w"):
        pass

janela=tk.Tk()
janela.geometry("500x300")
janela.config(bg="gray")

botao=tk.Button(janela, text="botão", command=criar)
botao.pack()

for item in os.listdir():
    arquivo=tk.Label(janela, text=item)
    arquivo.pack(pady=1)
janela.mainloop()