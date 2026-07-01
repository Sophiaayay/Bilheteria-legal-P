import tkinter as tk
from tkinter import ttk

janela = None

def main():
    janela = tk.Tk()
    janela.title("Meu primeiro aneurisma")
    janela.geometry("980x680")
    janela.minsize(820, 560)

    conteudo = ttk.Frame(janela, padding=16)
    conteudo.pack(fill="both", expand=True)
    ttk.Button(conteudo, text="aiaiaiaiai", command=abrir_janela).pack(anchor="w")


    janela.mainloop()

def abrir_janela():
    janela2 = tk.Toplevel(janela)
    janela2.title("janela safe")
    janela2.transient(janela)
    janela2.minsize(560, 380)

if __name__ == "__main__":
    main()