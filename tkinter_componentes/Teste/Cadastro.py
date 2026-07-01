import tkinter as tk
from tkinter import ttk

def centralizar_janela(janela, largura, altura):
    # Obtém a resolução da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição central ($X$ e $Y$)
    posicao_x = int((largura_tela / 2) - (largura / 2))
    posicao_y = int((altura_tela / 2) - (altura / 2))
    
    # Define a geometria da janela
    janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

# Configuração da Janela Principal
root = tk.Tk()
root.title("Sistema de Login e Cadastro")

# Tela um pouco grande (ex: 800x600)
largura_janela = 800
altura_janela = 600
centralizar_janela(root, largura_janela, altura_janela)

# Criação de um Notebook (abas) para separar Login e Cadastro
abas = ttk.Notebook(root)
abas.pack(fill="both", expand=True, padx=20, pady=20)

# --- Aba de Login ---
aba_login = ttk.Frame(abas)
abas.add(aba_login, text="Login")

tk.Label(aba_login, text="Entre na sua conta", font=("Arial", 16)).pack(pady=20)
tk.Label(aba_login, text="E-mail:").pack(pady=5)
tk.Entry(aba_login, width=40).pack(pady=5)
tk.Label(aba_login, text="Senha:").pack(pady=5)
tk.Entry(aba_login, show="*", width=40).pack(pady=5)
tk.Button(aba_login, text="Entrar", width=15).pack(pady=20)

# --- Aba de Cadastro ---
aba_cadastro = ttk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro")

tk.Label(aba_cadastro, text="Crie um novo usuário", font=("Arial", 16)).pack(pady=20)
tk.Label(aba_cadastro, text="Nome Completo:").pack(pady=5)
tk.Entry(aba_cadastro, width=40).pack(pady=5)
tk.Label(aba_cadastro, text="E-mail:").pack(pady=5)
tk.Entry(aba_cadastro, width=40).pack(pady=5)
tk.Label(aba_cadastro, text="Senha:").pack(pady=5)
tk.Entry(aba_cadastro, show="*", width=40).pack(pady=5)
tk.Button(aba_cadastro, text="Cadastrar", width=15).pack(pady=20)

# Inicia o loop da aplicação
root.mainloop()
