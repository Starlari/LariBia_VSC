import tkinter as tk

def clicar(botao):
    atual = entrada.get()
    if botao == "=":
        try:
            resultado = str(eval(atual))
            entrada.delete(0, tk.END)
            entrada.insert(0, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, botao)

janela = tk.Tk()
janela.title("LariBia calculator's")

entrada = tk.Entry(janela, width=20, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0)
]

for (texto, linha, coluna) in botoes:
    tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18),
              command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna, padx=5, pady=5, columnspan=1)

janela.mainloop()