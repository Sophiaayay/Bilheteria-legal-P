import Cadastro3
import os
import tkinter as tk
from tkinter import messagebox


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")



def abrir_menu_principal(nome_usuario):
    janela_menu = tk.Toplevel()
    janela_menu.title("PobreFlix - Menu Principal")
    janela_menu.configure(bg="#141414")
    centralizar_janela(janela_menu, 1920, 1080)

    janela_menu.protocol("WM_DELETE_WINDOW")

    tk.Label(
        janela_menu, 
        text=f"Olá, {nome_usuario}!", 
        font=("Arial", 20, "bold"), 
        bg="#141414", 
        fg="#E50914"
    ).pack(pady=30, padx=10, anchor="nw")

    tk.Label(
        janela_menu, 
        text="O que você deseja fazer hoje?", 
        font=("Arial", 12), 
        bg="#141414", 
        fg="white"
    ).pack(pady=10,padx=10, anchor="nw")


    def acao_pesquisar():
        messagebox.showinfo("Pesquisar", "Abrindo a barra de pesquisa de títulos...")

    btn_pesquisar = tk.Button(
        janela_menu,
        text="🔍 Pesquisar",
        font=("Arial", 14, "bold"),
        bg="#333333",
        fg="white",
        width=20,
        height=2,
        bd=3,
        cursor="hand2",
        command=acao_pesquisar
    )
    btn_pesquisar.pack(pady=15, padx=10, anchor="nw")