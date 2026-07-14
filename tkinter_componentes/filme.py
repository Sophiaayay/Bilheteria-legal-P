import os
import tkinter as tk
from tkinter import messagebox
from Pagamento_alimentos import abrir_pagamento

ARQUIVO_ASSENTOS = "assentos_ocupados.txt"


def normalizar_chave(texto):
    substituicoes = {
        " ": "_", "(": "", ")": "", ":": "", ",": "", "-": "_", "á": "a", 
        "ã": "a", "ç": "c", "é": "e", "í": "i", "ó": "o", "ú": "u"
    }
    texto_limpo = texto.lower()
    for caractere, substituto in substituicoes.items():
        texto_limpo = texto_limpo.replace(caractere, substituto)
    return texto_limpo


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


def salvar_multiplos_assentos(lista_chaves, usuario):
    with open(ARQUIVO_ASSENTOS, "a", encoding="utf-8") as arquivo:
        for chave in lista_chaves:
            arquivo.write(f"{chave}:{usuario}\n")


def abrir_filme(filme, nome_usuario, funcao_atualizar_menu):
    janela_filme = tk.Toplevel()
    janela_filme.title(f"PobreFlix - {filme['nome']}")
    janela_filme.configure(bg="#141414")
    janela_filme.geometry("800x750")
    janela_filme.resizable(False, False)

    assentos_selecionados_agora = []
    chaves_para_salvar = []

    frame_info = tk.Frame(janela_filme, bg="#141414", padx=20, pady=20)
    frame_info.pack(fill="x")

    imagem_poster = None
    if filme["imagem"] and os.path.exists(filme["imagem"]):
        try:
            imagem_poster = tk.PhotoImage(file=filme["imagem"])
            imagem_poster = imagem_poster.subsample(5, 5) 
            janela_filme._poster_referencia = imagem_poster  
        except Exception as e:
            print(f"Erro ao carregar poster: {e}")

    if imagem_poster:
        lbl_imagem = tk.Label(frame_info, image=imagem_poster, bg="#141414")
    else:
        lbl_imagem = tk.Label(frame_info, text="[Sem Imagem]", bg="#333333", fg="white", font=("Arial", 12), width=15, height=8)
    lbl_imagem.pack(side="left", padx=(0, 20))

    frame_texto = tk.Frame(frame_info, bg="#141414")
    frame_texto.pack(side="left", fill="both", expand=True)

    tk.Label(frame_texto, text=filme["nome"], fg="white", bg="#141414", font=("Arial", 20, "bold")).pack(anchor="w")
    tk.Label(frame_texto, text=f"{filme['ano']} | {filme['genero']}", fg="#AAAAAA", bg="#141414", font=("Arial", 11)).pack(anchor="w", pady=5)
    
    lbl_desc = tk.Label(frame_texto, text=filme["descricao"], fg="white", bg="#141414", font=("Arial", 10), wrap=450, justify="left")
    lbl_desc.pack(anchor="w", pady=5)

    tk.Label(janela_filme, text="Escolha seus assentos:", fg="white", bg="#141414", font=("Arial", 14, "bold")).pack(pady=5)

    frame_botoes_dias = tk.Frame(janela_filme, bg="#141414")
    frame_botoes_dias.pack()

    frame_mapa_assentos = tk.Frame(janela_filme, bg="#141414", pady=10)
    frame_mapa_assentos.pack(fill="both", expand=True)

    frame_confirmar = tk.Frame(janela_filme, bg="#141414", pady=10)
    frame_confirmar.pack(fill="x")

    def abrir_mapa_assentos(dia_escolhido):
        nonlocal assentos_selecionados_agora, chaves_para_salvar
        assentos_selecionados_agora.clear()
        chaves_para_salvar.clear()

        for widget in frame_mapa_assentos.winfo_children():
            widget.destroy()
        for widget in frame_confirmar.winfo_children():
            widget.destroy()

        # Legenda atualizada contendo os assentos preferenciais na cor azul
        tk.Label(
            frame_mapa_assentos,
            text=f"Mapa de Assentos para {dia_escolhido}\n"
                 f"(Cinza = Livre | Azul = Preferencial | Amarelo = Selecionando | Vermelho = Ocupado | Verde = Seus antigos)",
            fg="white", bg="#141414", font=("Arial", 11, "bold")
        ).pack(pady=5)

        grid_assentos = tk.Frame(frame_mapa_assentos, bg="#141414")
        grid_assentos.pack()

        assentos_globais = carregar_assentos_ocupados()

        for linha in range(4):
            letra_linha = chr(65 + linha)
            # Definindo a última linha (Linha D) como preferencial por lei
            e_preferencial = (letra_linha == "D")

            for coluna in range(5):
                nome_assento = f"{letra_linha}{coluna + 1}"
                filme_id = normalizar_chave(filme['nome'])
                dia_id = normalizar_chave(dia_escolhido)
                chave_reserva = f"{filme_id}_{dia_id}_{nome_assento}"

                dono_reserva = assentos_globais.get(chave_reserva)

                if dono_reserva == nome_usuario:
                    cor_fundo, estado, texto_exibir = "#4CAF50", "disabled", f"{nome_assento}\n(Meu)"
                elif dono_reserva is not None:
                    cor_fundo, estado, texto_exibir = "#E50914", "disabled", f"{nome_assento}\n(Ocup.)"
                elif e_preferencial:
                    # Assentos preferenciais livres começam em Azul
                    cor_fundo, estado, texto_exibir = "#1E90FF", "normal", f"{nome_assento}\n(Pref.)"
                else:
                    cor_fundo, estado, texto_exibir = "#555555", "normal", nome_assento

                def alternar_selecao(btn, pref=e_preferencial, c=chave_reserva, n=nome_assento):
                    if n in assentos_selecionados_agora:
                        assentos_selecionados_agora.remove(n)
                        chaves_para_salvar.remove(c)
                        # Retorna para a cor padrão de acordo com a categoria
                        if pref:
                            btn.config(bg="#1E90FF", text=f"{n}\n(Pref.)")
                        else:
                            btn.config(bg="#555555", text=n)
                    else:
                        # Se for preferencial, exibe um aviso educacional de confirmação
                        if pref:
                            resposta = messagebox.askyesno(
                                "Assento Preferencial",
                                f"O assento {n} é reservado preferencialmente para idosos, autistas, "
                                f"gestantes ou pessoas com deficiência física por direito de lei.\n\n"
                                f"Deseja selecionar este assento?"
                            )
                            if not resposta:
                                return  # Usuário cancelou a seleção

                        assentos_selecionados_agora.append(n)
                        chaves_para_salvar.append(c)
                        btn.config(bg="#FFC107", text=f"{n}\n(Selec.)")

                btn_assento = tk.Button(
                    grid_assentos, text=texto_exibir, bg=cor_fundo, fg="white",
                    font=("Arial", 9, "bold"), width=9, height=2, state=estado
                )

                btn_assento.config(command=lambda b=btn_assento, p=e_preferencial, c=chave_reserva, n=nome_assento: alternar_selecao(b, p, c, n))
                btn_assento.grid(row=linha, column=coluna, padx=6, pady=6)

        def enviar_para_pagamento():
            if not assentos_selecionados_agora:
                messagebox.showwarning("Aviso", "Selecione pelo menos um assento antes de continuar!")
                return
            
            salvar_multiplos_assentos(chaves_para_salvar, nome_usuario)
            janela_filme.destroy()
            
            abrir_pagamento(
                filme['nome'], 
                dia_escolhido, 
                ", ".join(assentos_selecionados_agora), 
                len(assentos_selecionados_agora),
                funcao_atualizar_menu
            )

        tk.Button(
            frame_confirmar, text="AVANÇAR PARA OS LANCHES", bg="#E50914", fg="white",
            font=("Arial", 12, "bold"), width=25, height=2, command=enviar_para_pagamento
        ).pack()

    dias_do_filme = filme.get("dias", ["Sábado (19:00)", "Domingo (16:00)"])
    for dia in dias_do_filme:
        btn_dia = tk.Button(
            frame_botoes_dias, text=dia, bg="#222222", fg="white", activebackground="#E50914",
            font=("Arial", 11, "bold"), padx=15, pady=5, command=lambda d=dia: abrir_mapa_assentos(d)
        )
        btn_dia.pack(side="left", padx=10)

    if dias_do_filme:
        abrir_mapa_assentos(dias_do_filme[0])