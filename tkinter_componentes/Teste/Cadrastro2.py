import tkinter as tk
from tkinter import messagebox

# Dicionário simples em memória para simular um banco de dados
usuarios_db = {}

def centralizar_janela(janela, largura, altura):
    # Obtém a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição x e y para centralizar a janela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    
    # Define a geometria da janela
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def mostrar_tela(frame_desejado):
    # Esconde todos os frames
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    
    # Mostra o frame desejado
    frame_desejado.pack(pady=50)

def cadastrar_usuario():
    usuario = entry_cad_usuario.get()
    senha = entry_cad_senha.get()
    
    if not usuario or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
        
    if usuario in usuarios_db:
        messagebox.showwarning("Aviso", "Usuário já existe.")
    else:
        usuarios_db[usuario] = senha
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        limpar_campos(entry_cad_usuario, entry_cad_senha)
        mostrar_tela(frame_login) # Volta para o login após cadastrar

def fazer_login():
    usuario = entry_log_usuario.get()
    senha = entry_log_senha.get()
    
    if usuarios_db.get(usuario) == senha:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def limpar_campos(*entries):
    for entry in entries:
        entry.delete(0, tk.END)

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Login e Cadastro")
janela.configure(bg="#f0f0f0")

# Chama a função para centralizar a janela de 600x500
centralizar_janela(janela, 600, 500)

# --- FRAME DE LOGIN ---
frame_login = tk.Frame(janela, bg="#f0f0f0")
frame_login.pack(pady=50)

tk.Label(frame_login, text="Tela de Login", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

tk.Label(frame_login, text="Usuário:", font=("Arial", 14), bg="#f0f0f0").pack()
entry_log_usuario = tk.Entry(frame_login, font=("Arial", 14), width=30)
entry_log_usuario.pack(pady=5)

tk.Label(frame_login, text="Senha:", font=("Arial", 14), bg="#f0f0f0").pack()
entry_log_senha = tk.Entry(frame_login, font=("Arial", 14), show="*", width=30)
entry_log_senha.pack(pady=5)

tk.Button(frame_login, text="Entrar", font=("Arial", 14), command=fazer_login, bg="#4CAF50", fg="white", width=15).pack(pady=20)

# Botão abaixo do Entrar para ir para o Cadastro
tk.Label(frame_login, text="Ainda não tem uma conta?", font=("Arial", 10), bg="#f0f0f0").pack()
tk.Button(frame_login, text="Cadastre-se", font=("Arial", 10, "italic"), fg="blue", bg="#f0f0f0", bd=0, 
          command=lambda: mostrar_tela(frame_cadastro)).pack()

# --- FRAME DE CADASTRO ---
frame_cadastro = tk.Frame(janela, bg="#f0f0f0")

tk.Label(frame_cadastro, text="Cadastro de Conta", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

tk.Label(frame_cadastro, text="Novo Usuário:", font=("Arial", 14), bg="#f0f0f0").pack()
entry_cad_usuario = tk.Entry(frame_cadastro, font=("Arial", 14), width=30)
entry_cad_usuario.pack(pady=5)

tk.Label(frame_cadastro, text="Nova Senha:", font=("Arial", 14), bg="#f0f0f0").pack()
entry_cad_senha = tk.Entry(frame_cadastro, font=("Arial", 14), show="*", width=30)
entry_cad_senha.pack(pady=5)

tk.Button(frame_cadastro, text="Cadastrar", font=("Arial", 14), command=cadastrar_usuario, bg="#2196F3", fg="white", width=15).pack(pady=20)

# Botão abaixo do Cadastrar para ir para o Login
tk.Label(frame_cadastro, text="Já possui uma conta?", font=("Arial", 10), bg="#f0f0f0").pack()
tk.Button(frame_cadastro, text="Ir para o Login", font=("Arial", 10, "italic"), fg="blue", bg="#f0f0f0", bd=0, 
          command=lambda: mostrar_tela(frame_login)).pack()

# Inicia mostrando a tela de login
mostrar_tela(frame_login)

janela.mainloop()
