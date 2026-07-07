import os
import tkinter as tk
from tkinter import messagebox

ARQUIVO_DB = "UsuariosSalvos.txt"
usuarios_db = {}


def carregar_usuarios():
    if os.path.exists(ARQUIVO_DB):
        with open(ARQUIVO_DB, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    usuario, senha = linha.split(":", 1)
                    usuarios_db[usuario] = senha


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def mostrar_tela(frame_desejado):
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_desejado.pack(fill="both", expand=True, pady=20)


def cadastrar_usuario():
    usuario = entry_cad_usuario.get().strip()
    senha = entry_cad_senha.get().strip()

    if not usuario or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    if ":" in usuario:
        messagebox.showerror("Erro", "O nome de usuário não pode conter o caractere ':'.")
        return

    if usuario in usuarios_db:
        messagebox.showwarning("Aviso", "Usuário já existe.")
    else:
        usuarios_db[usuario] = senha
        with open(ARQUIVO_DB, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{usuario}:{senha}\n")

        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        limpar_campos(entry_cad_usuario, entry_cad_senha)
        mostrar_tela(frame_login)


def fazer_login():
    usuario = entry_log_usuario.get().strip()
    senha = entry_log_senha.get().strip()

    if usuarios_db.get(usuario) == senha:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        limpar_campos(entry_log_usuario, entry_log_senha)
        
        janela.withdraw()
        abrir_menu_principal(usuario)
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")


def limpar_campos(*entries):
    for entry in entries:
        entry.delete(0, tk.END)


def abrir_menu_principal(nome_usuario):
    janela_menu = tk.Toplevel()
    janela_menu.title("PobreFlix - Menu Principal")
    janela_menu.configure(bg="#141414")
    centralizar_janela(janela_menu, 500, 400)

    janela_menu.protocol("WM_DELETE_WINDOW", janela.destroy)

    tk.Label(
        janela_menu, 
        text=f"Olá, {nome_usuario}!", 
        font=("Arial", 20, "bold"), 
        bg="#141414", 
        fg="#E50914" 
    ).pack(pady=30)

    tk.Label(
        janela_menu, 
        text="O que você deseja fazer hoje?", 
        font=("Arial", 12), 
        bg="#141414", 
        fg="white"
    ).pack(pady=10)

    def acao_ver_filmes():
        messagebox.showinfo("Ver Filmes", "Abrindo o catálogo de filmes...")

    def acao_pesquisar():
        messagebox.showinfo("Pesquisar", "Abrindo a barra de pesquisa de títulos...")

    btn_filmes = tk.Button(
        janela_menu,
        text="🎬 Ver Filmes",
        font=("Arial", 14, "bold"),
        bg="#E50914",
        fg="white",
        width=20,
        height=2,
        bd=0,
        cursor="hand2",
        command=acao_ver_filmes
    )
    btn_filmes.pack(pady=15)

    btn_pesquisar = tk.Button(
        janela_menu,
        text="🔍 Pesquisar",
        font=("Arial", 14, "bold"),
        bg="#333333",
        fg="white",
        width=20,
        height=2,
        bd=0,
        cursor="hand2",
        command=acao_pesquisar
    )
    btn_pesquisar.pack(pady=15)


janela = tk.Tk()
janela.title("Login e Cadastro")
janela.configure(bg="#f0f0f0")
centralizar_janela(janela, 450, 450)

carregar_usuarios()

frame_login = tk.Frame(janela, bg="#f0f0f0")
tk.Label(frame_login, text="Tela de Login", font=("Arial", 22, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)
tk.Label(frame_login, text="Usuário:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=50)
entry_log_usuario = tk.Entry(frame_login, font=("Arial", 12), width=28)
entry_log_usuario.pack(pady=5)
tk.Label(frame_login, text="Senha:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=50)
entry_log_senha = tk.Entry(frame_login, font=("Arial", 12), show="*", width=28)
entry_log_senha.pack(pady=5)
tk.Button(frame_login, text="Entrar", font=("Arial", 12, "bold"), command=fazer_login, bg="#4CAF50", fg="white", width=15, cursor="hand2").pack(pady=20)
tk.Label(frame_login, text="Ainda não tem uma conta?", font=("Arial", 10), bg="#f0f0f0", fg="#666").pack()
tk.Button(frame_login, text="Cadastre-se", font=("Arial", 10, "underline"), fg="#2196F3", bg="#f0f0f0", bd=0, command=lambda: [limpar_campos(entry_log_usuario, entry_log_senha), mostrar_tela(frame_cadastro)], cursor="hand2").pack()


frame_cadastro = tk.Frame(janela, bg="#f0f0f0")
tk.Label(frame_cadastro, text="Cadastro de Conta", font=("Arial", 22, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)
tk.Label(frame_cadastro, text="Novo Usuário:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=50)
entry_cad_usuario = tk.Entry(frame_cadastro, font=("Arial", 12), width=28)
entry_cad_usuario.pack(pady=5)
tk.Label(frame_cadastro, text="Nova Senha:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=50)
entry_cad_senha = tk.Entry(frame_cadastro, font=("Arial", 12), show="*", width=28)
entry_cad_senha.pack(pady=5)
tk.Button(frame_cadastro, text="Cadastrar", font=("Arial", 12, "bold"), command=cadastrar_usuario, bg="#2196F3", fg="white", width=15, cursor="hand2").pack(pady=20)
tk.Label(frame_cadastro, text="Já possui uma conta?", font=("Arial", 10), bg="#f0f0f0", fg="#666").pack()
tk.Button(frame_cadastro, text="Ir para o Login", font=("Arial", 10, "underline"), fg="#4CAF50", bg="#f0f0f0", bd=0, command=lambda: [limpar_campos(entry_cad_usuario, entry_cad_senha), mostrar_tela(frame_login)], cursor="hand2").pack()

mostrar_tela(frame_login)
janela.mainloop()