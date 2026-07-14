import os
import tkinter as tk
from tkinter import messagebox
from filme import abrir_filme  # Importação ajustada para corresponder ao nome do arquivo 'filmes.py'

ARQUIVO_DB = "UsuariosSalvos.txt"
usuarios_db = {}

TICKETS_COMPRADOS = []

# Variáveis globais dos elementos gráficos (definidas como None inicialmente)
janela = None
frame_login = None
frame_cadastro = None
entry_log_usuario = None
entry_log_senha = None
entry_cad_usuario = None
entry_cad_senha = None


def carregar_usuarios():
    if os.path.exists(ARQUIVO_DB):
        with open(ARQUIVO_DB, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    usuario, senha = linha.split(":", 1)
                    usuarios_db[usuario] = senha


def centralizar_janela(janela_obj, largura, altura):
    largura_tela = janela_obj.winfo_screenwidth()
    altura_tela = janela_obj.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela_obj.geometry(f"{largura}x{altura}+{x}+{y}")


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
        
        janela.destroy()
        abrir_menu_principal(usuario)
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")


def limpar_campos(*entries):
    for entry in entries:
        entry.delete(0, tk.END)


def abrir_menu_principal(nome_usuario):
    janela_menu = tk.Tk()
    janela_menu.title("PobreFlix - Menu Principal")
    janela_menu.configure(bg="#141414")
    
    largura = janela_menu.winfo_screenwidth()
    altura = janela_menu.winfo_screenheight()
    janela_menu.geometry(f"{largura}x{altura}+0+0")

    filmes = [
        {
            "nome": "Invocação da Inteligência",
            "ano": "2025",
            "genero": "Terror, suspense",
            "descricao": "Um jovem de info2m que invoca a inteligência.",
            "imagem": "fotos poo/invocacao.png",
            "dias": ["Quarta-feira (20:30)", "Quinta-feira (18:00)"]
        },
        {
            "nome": "Death Note: O Último Domingo à Noite",
            "ano": "2020",
            "genero": "Ação, suspense",
            "descricao": "Onde Kira enfrenta o lobo pidão.",
            "imagem": "fotos poo/deathnote.png",
            "dias": ["Sexta-feira (21:00)", "Domingo (19:30)"]
        },
        {
            "nome": "Piscininha Amor",
            "ano": "2026",
            "genero": "Terror psicológico, suspense, drama",
            "descricao": "Apenas uma confraternização entre alunos, o que pode dar errado?.",
            "imagem": "fotos poo/Party at the bottom of the pool.png",
            "dias": ["Quinta-feira (16:00)", "Sábado (22:00)"]
        },
        {
            "nome": "Duas Noites com o Alfredo",
            "ano": "2009",
            "genero": "Ficção científica, comédia",
            "descricao": "Um salário bom e apenas duas noites de turno... parece um sonho.",
            "imagem": "fotos poo/usdh.png",
            "dias": ["Segunda-feira (19:00)", "Terça-feira (19:00)"]
        },
        {
            "nome": "Lobo Pidão: A Origem",
            "ano": "2999",
            "genero": "Baseado em fatos reais",
            "descricao": "Cansado do domingo a noite, o lobo pidão enfrenta a segunda-feira.",
            "imagem": "fotos poo/pidao.png",
            "dias": ["Quarta-feira (15:00)", "Sexta-feira (17:30)"]
        },
        {
            "nome": "Homem Aranha: Deu Ruim na Volta Pra Casa",
            "ano": "2018",
            "genero": "Ação",
            "descricao": "Peter Parker enfrenta o multiverso caprichado.",
            "imagem": "fotos poo/download.png",
            "dias": ["Sábado (14:00)", "Domingo (16:00)"]
        }
    ]

    topo = tk.Frame(janela_menu, bg="#141414")
    topo.pack(fill="x", padx=40, pady=10)

    titulo = tk.Label(topo, text="POBREFLIX", fg="#E50914", bg="#141414", font=("Arial", 30, "bold"))
    titulo.pack(side="left")

    lbl_usuario = tk.Label(topo, text=f"Olá, {nome_usuario}", fg="white", bg="#141414", font=("Arial", 16))
    lbl_usuario.pack(side="right")

    def atualizar_mural_tickets():
        pass

    frame_pesquisa = tk.Frame(janela_menu, bg="#141414")
    frame_pesquisa.pack(fill="x", padx=40, pady=10)

    sub_pesquisa = tk.Frame(frame_pesquisa, bg="#141414")
    sub_pesquisa.pack(anchor="center")

    entrada = tk.Entry(sub_pesquisa, font=("Arial", 14), width=40)
    entrada.pack(side="left", padx=10)
    frame_container = tk.Frame(janela_menu, bg="#141414")
    frame_container.pack(fill="both", expand=True, padx=40, pady=10)

    canvas = tk.Canvas(frame_container, bg="#141414", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
    frame_rolavel = tk.Frame(canvas, bg="#141414")

    frame_rolavel.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((largura // 2 - 60, 0), window=frame_rolavel, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def mostrar_filmes(lista):
        for widget in frame_rolavel.winfo_children():
            widget.destroy()

        if not lista:
            tk.Label(frame_rolavel, text="Nenhum filme encontrado.", fg="white", bg="#141414", font=("Arial", 14)).pack(pady=20)
            return

        linha = 0
        coluna = 0

        for filme in lista:
            card = tk.Frame(frame_rolavel, bg="#222222", padx=15, pady=15)
            card.grid(row=linha, column=coluna, padx=20, pady=20)

            imagem_tkinter = None
            if filme["imagem"] and os.path.exists(filme["imagem"]):
                try:
                    imagem_tkinter = tk.PhotoImage(file=filme["imagem"])
                    imagem_tkinter = imagem_tkinter.subsample(6, 6)
                    filme["_foto_referencia"] = imagem_tkinter
                except Exception as e:
                    print(f"Erro na imagem: {e}")

            if imagem_tkinter:
                botao = tk.Button(card, image=imagem_tkinter, width=130, height=160, bg="#333333", relief="flat", command=lambda f=filme: intermediario_abrir_filme(f))
            else:
                botao = tk.Button(card, text="Sem Imagem", width=16, height=9, bg="#333333", fg="white", font=("Arial", 10, "bold"), relief="flat", command=lambda f=filme: intermediario_abrir_filme(f))
            botao.pack()

            tk.Label(card, text=filme["nome"], bg="#222222", fg="white", font=("Arial", 12, "bold"), wraplength=160, justify="center").pack(pady=(10, 2))
            tk.Label(card, text=f"{filme['ano']} • {filme['genero']}", bg="#222222", fg="#E50914", font=("Arial", 10, "bold"), wraplength=160).pack()
            tk.Label(card, text=filme["descricao"], bg="#222222", fg="#AAAAAA", font=("Arial", 9), wraplength=160, justify="center", height=3).pack(pady=5)

            coluna += 1
            if coluna == 3:
                coluna = 0
                linha += 1

    def intermediario_abrir_filme(f):
        # Repassando a lista TICKETS_COMPRADOS como parâmetro
        abrir_filme(f, nome_usuario, atualizar_mural_tickets, TICKETS_COMPRADOS)

    def pesquisar():
        texto = entrada.get().lower()
        encontrados = [filme for filme in filmes if texto in filme["nome"].lower()]
        mostrar_filmes(encontrados)

    tk.Button(sub_pesquisa, text="Pesquisar", bg="#E50914", fg="white", font=("Arial", 11, "bold"), padx=15, command=pesquisar, relief="flat").pack(side="left")

    mostrar_filmes(filmes)
    janela_menu.mainloop()


def iniciar_sistema():
    global janela, frame_login, frame_cadastro
    global entry_log_usuario, entry_log_senha, entry_cad_usuario, entry_cad_senha

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


if __name__ == "__main__":
    iniciar_sistema()