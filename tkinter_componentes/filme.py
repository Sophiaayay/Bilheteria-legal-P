import os
import tkinter as tk
from tkinter import messagebox

ARQUIVO_ASSENTOS = "assentos_ocupados.txt"


def carregar_assentos_ocupados():
    assentos_reservados = {}
    if os.path.exists(ARQUIVO_ASSENTOS):
        with open(ARQUIVO_ASSENTOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    chave, usuario = linha.split(":", 1)
                    assentos_reservados[chave.strip()] = usuario.strip()
    return assentos_reservados


def salvar_assento_ocupado(chave_reserva, usuario):
    with open(ARQUIVO_ASSENTOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{chave_reserva}:{usuario}\n")


def abrir_filme(filme, nome_usuario):
    janela_filme = tk.Toplevel()
    janela_filme.title(f"PobreFlix - {filme['nome']}")
    janela_filme.configure(bg="#141414")
    janela_filme.geometry("800x650")
    janela_filme.resizable(False, False)

    frame_info = tk.Frame(janela_filme, bg="#141414", padx=20, pady=20)
    frame_info.pack(fill="x")

    lbl_imagem = tk.Label(
        frame_info,
        text="[imagem]",
        bg="#333333",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=8
    )
    lbl_imagem.pack(side="left", padx=(0, 20))

    frame_texto = tk.Frame(frame_info, bg="#141414")
    frame_texto.pack(side="left", fill="both", expand=True)

    tk.Label(frame_texto, text=filme["nome"], fg="white", bg="#141414", font=("Arial", 22, "bold")).pack(anchor="w")
    tk.Label(frame_texto, text=f"Ano: {filme['ano']} | Gênero: {filme['genero']}", fg="#AAAAAA", bg="#141414", font=("Arial", 12)).pack(anchor="w", pady=5)
    
    lbl_desc = tk.Label(frame_texto, text=filme["descricao"], fg="white", bg="#141414", font=("Arial", 11), wrap=450, justify="left")
    lbl_desc.pack(anchor="w", pady=10)

    tk.Label(janela_filme, text="Escolha um dia para assistir:", fg="white", bg="#141414", font=("Arial", 14, "bold")).pack(pady=10)

    frame_botoes_dias = tk.Frame(janela_filme, bg="#141414")
    frame_botoes_dias.pack()

    dias_disponiveis = ["Sábado (19:00)", "Domingo (16:00)"]

    frame_mapa_assentos = tk.Frame(janela_filme, bg="#141414", pady=20)
    frame_mapa_assentos.pack(fill="both", expand=True)

    def abrir_mapa_assentos(dia_escolhido):
        for widget in frame_mapa_assentos.winfo_children():
            widget.destroy()

        tk.Label(
            frame_mapa_assentos,
            text=f"Mapa de Assentos para {dia_escolhido}\n(Vermelho = Ocupado | Verde = Seu Lugar | Cinza = Disponível)",
            fg="white",
            bg="#141414",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        grid_assentos = tk.Frame(frame_mapa_assentos, bg="#141414")
        grid_assentos.pack()

        assentos_globais = carregar_assentos_ocupados()

        for linha in range(4):
            for coluna in range(5):
                nome_assento = f"{chr(65 + linha)}{coluna + 1}" 
                
                nome_filme_limpo = filme['nome'].replace(" ", "_")
                dia_limpo = dia_escolhido.replace(" ", "_")
                chave_reserva = f"{nome_filme_limpo}_{dia_limpo}_{nome_assento}"

                dono_reserva = assentos_globais.get(chave_reserva)

                if dono_reserva == nome_usuario:
                    cor_fundo = "#4CAF50" 
                    estado = "disabled"
                    texto_exibir = f"{nome_assento}\n(Meu)"
                elif dono_reserva is not None:
                    cor_fundo = "#E50914" 
                    estado = "disabled"
                    texto_exibir = f"{nome_assento}\n(Ocup.)"
                else:
                    cor_fundo = "#555555" 
                    estado = "normal"
                    texto_exibir = nome_assento

                def reservar(c=chave_reserva, n=nome_assento):
                    resposta = messagebox.askyesno("Confirmar Reserva", f"Deseja reservar o assento {n}?")
                    if resposta:
                        salvar_assento_ocupado(c, nome_usuario)
                        messagebox.showinfo("Sucesso!", f"Assento {n} reservado com sucesso!")

                        abrir_mapa_assentos(dia_escolhido)

                btn_assento = tk.Button(
                    grid_assentos,
                    text=texto_exibir,
                    bg=cor_fundo,
                    fg="white",
                    font=("Arial", 10, "bold"),
                    width=8,
                    height=2,
                    state=estado,
                    command=lambda c=chave_reserva, n=nome_assento: reservar(c, n)
                )
                btn_assento.grid(row=linha, column=coluna, padx=5, pady=5)

    for dia in dias_disponiveis:
        btn_dia = tk.Button(
            frame_botoes_dias,
            text=dia,
            bg="#333333",
            fg="white",
            activebackground="#E50914",
            font=("Arial", 12, "bold"),
            padx=10,
            command=lambda d=dia: abrir_mapa_assentos(d)
        )
        btn_dia.pack(side="left", padx=10)