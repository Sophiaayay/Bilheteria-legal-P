import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from filme import abrir_filme

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
    janela_menu.title("PobreFlix")
    janela_menu.configure(bg="#141414")
    largura = janela_menu.winfo_screenwidth()
    altura = janela_menu.winfo_screenheight()
    janela_menu.geometry(f"{largura}x{altura}+0+0")

   
    filmes = [
        {
            "nome": "invocação da inteligencia",
            "ano": "2025",
            "genero": "Terror, suspense",
            "descricao": "Um jovem de info2m que invoca a inteligência.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\invocacao.png"
        },
        {
            "nome": "Death note: o último domingo à noite",
            "ano": "2020",
            "genero": "Ação, suspense",
            "descricao": "onde Kira enfrenta o lobo pidão.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\deathnote.png"
        },
        {
            "nome": "Piscininha amor",
            "ano": "2026",
            "genero": "Terror psicológico, suspense, drama",
            "descricao": "Apenas uma confraternização entre alunos, oq pode dar errado?.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\party at the bottom of the pool.png"
        },
        {
            "nome": "Duas Noites com o Alfredo",
            "ano": "2009",
            "genero": "Ficção científica, comédia",
            "descricao": "Um salário bom e apenas duas noites de turno... parece um sonho.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\usdh.png"
        },
        {
            "nome": "Lobo pidão: A origem",
            "ano": "2999",
            "genero": "baseado em fatos reais",
            "descricao": "Cansado do domingo a noite, o lobo pidão enfrenta seu maior inimigo: segunda-feira.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\pidao.png"
        },
        {
            "nome": "homem aranha: Deu ruim na volta pra casa",
            "ano": "2018",
            "genero": "Ação",
            "descricao": "Peter Parker enfrenta o multiverso.",
            "imagem": "C:\\Users\\Usuario\\Documents\\GitHub\\Bilheteria-legal-P\\fotos poo\\download.png"
        }
    ]


    topo = tk.Frame(janela_menu, bg="#141414")
    topo.pack(fill="x")

    titulo = tk.Label(
        topo,
        text="POBREFLIX",
        fg="#E50914",
        bg="#141414",
        font=("Arial", 30, "bold")
    )
    titulo.pack(side="left", padx=20, pady=20)

    usuario = tk.Label(
        topo,
        text=f"Olá, {nome_usuario}",
        fg="white",
        bg="#141414",
        font=("Arial",16)
    )
    usuario.pack(side="right", padx=20)



    frame_pesquisa = tk.Frame(janela_menu,bg="#141414")
    frame_pesquisa.pack(fill="x", pady=10)

    entrada = tk.Entry(frame_pesquisa,font=("Arial",14),width=40)
    entrada.pack(side="left", padx=20)

    frame_filmes = tk.Frame(janela_menu,bg="#141414")
    frame_filmes.pack(fill="both", expand=True)

    def mostrar_filmes(lista):

        for widget in frame_filmes.winfo_children():
            widget.destroy()

        linha = 0
        coluna = 0

        for filme in lista:

            card = tk.Frame(
                frame_filmes,
                bg="#222222",
                padx=10,
                pady=10,
                relief="raised",
                bd=2
            )

            card.grid(row=linha, column=coluna, padx=20, pady=20)

            imagem_tkinter = None
            if filme["imagem"] and os.path.exists(filme["imagem"]):
                try:
                    imagem_tkinter = tk.PhotoImage(file=filme["imagem"])
                
                    imagem_tkinter = imagem_tkinter.subsample(6, 6) 

                    filme["_foto_referencia"] = imagem_tkinter
                except Exception as e:
                    print(f"Erro ao carregar a imagem de {filme['nome']}: {e}")

            if imagem_tkinter:
                botao = tk.Button(
                    card,
                    image=imagem_tkinter,
                    width=110,  
                    height=130, 
                    bg="#555555",
                    command=lambda f=filme: abrir_filme(f, nome_usuario)
                )
            else:
                botao = tk.Button(
                    card,
                    text="Sem Imagem",
                    width=15, 
                    height=8,   
                    bg="#555555",
                    fg="white",
                    command=lambda f=filme: abrir_filme(f, nome_usuario)
                )

            botao.pack()

            tk.Label(
                card,
                text=filme["nome"],
                bg="#222222",
                fg="white",
                font=("Arial", 12, "bold"),
                wraplength=160
            ).pack(pady=5)

            tk.Label(
                card,
                text=f"{filme['ano']} • {filme['genero']}",
                bg="#222222",
                fg="#AAAAAA",
                font=("Arial", 10),
                wraplength=160
            ).pack()

            tk.Label(
                card,
                text=filme["descricao"],
                bg="#222222",
                fg="white",
                font=("Arial", 10),
                wraplength=160,
                justify="left",
                height=3 
            ).pack(pady=5)

            coluna += 1

            if coluna == 3:
                coluna = 0
                linha += 1

    def pesquisar():

        texto = entrada.get().lower()

        encontrados = []

        for filme in filmes:
            if texto in filme["nome"].lower():
                encontrados.append(filme)

        mostrar_filmes(encontrados)

    tk.Button(
        frame_pesquisa,
        text="Pesquisar",
        bg="#E50914",
        fg="white",
        font=("Arial",12,"bold"),
        command=pesquisar
    ).pack(side="left")

    mostrar_filmes(filmes)


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