import tkinter as tk
from tkinter import messagebox
import random

def abrir_pagamento(filme_nome, dia, assentos, qtd_ingressos, funcao_atualizar_menu):
    janela_pag = tk.Toplevel()
    janela_pag.title("PobreFlix - Lanche e pagamento")
    janela_pag.configure(bg="#141414")
    janela_pag.geometry("550x800")  # Aumentamos um pouco a altura para caber as novidades confortavelmente
    janela_pag.resizable(False, False)

    PRECO_INGRESSO_UNITARIO = 15.00
    subtotal_ingressos = PRECO_INGRESSO_UNITARIO * qtd_ingressos

    precos_lanches = {
        "Pipoca": 10.00, "Refrigerante": 7.00, "Suco": 6.00, "Fini": 5.00, "Água": 4.00
    }

    variaveis_lanches = {lanche: tk.BooleanVar() for lanche in precos_lanches}
    var_estudante = tk.BooleanVar(value=False)  # Variável de desconto para estudante
    forma_pagamento = tk.StringVar(value="Pix")

    tk.Label(janela_pag, text="FINALIZAR PEDIDO", fg="#E50914", bg="#141414", font=("Arial", 18, "bold")).pack(pady=10)
    
    frame_resumo = tk.LabelFrame(janela_pag, text=" Itens Escolhidos ", fg="white", bg="#222222", font=("Arial", 10, "bold"), padx=15, pady=8)
    frame_resumo.pack(fill="x", padx=20)

    tk.Label(frame_resumo, text=f"Filme: {filme_nome}", fg="white", bg="#222222", font=("Arial", 11)).pack(anchor="w")
    tk.Label(frame_resumo, text=f"Sessão: {dia}", fg="white", bg="#222222", font=("Arial", 11)).pack(anchor="w")
    tk.Label(frame_resumo, text=f"Assentos: {assentos} ({qtd_ingressos}x)", fg="#4CAF50", bg="#222222", font=("Arial", 11, "bold")).pack(anchor="w")
    
    lbl_preco_ingressos = tk.Label(frame_resumo, text=f"Valor dos Ingressos: R$ {subtotal_ingressos:.2f}", fg="white", bg="#222222", font=("Arial", 11))
    lbl_preco_ingressos.pack(anchor="w")

    # --- Lanches ---
    frame_lanches = tk.LabelFrame(janela_pag, text=" Adicionar Lanches ", fg="white", bg="#222222", font=("Arial", 10, "bold"), padx=15, pady=5)
    frame_lanches.pack(fill="x", padx=20, pady=10)

    def calcular_total_atual():
        # Se for estudante, o valor do ingresso cai pela metade (50% de desconto)
        if var_estudante.get():
            total = (subtotal_ingressos * 0.5)
        else:
            total = subtotal_ingressos

        # Adiciona os lanches (não entram no desconto de meia-entrada)
        for lanche, var in variaveis_lanches.items():
            if var.get():
                total += precos_lanches[lanche]
        return total

    def atualizar_interface_preco():
        # Atualiza a exibição no resumo de ingressos
        if var_estudante.get():
            lbl_preco_ingressos.config(text=f"Valor dos Ingressos: R$ {subtotal_ingressos * 0.5:.2f} (Estudante -50%)", fg="#FFC107")
        else:
            lbl_preco_ingressos.config(text=f"Valor dos Ingressos: R$ {subtotal_ingressos:.2f}", fg="white")
            
        lbl_total.config(text=f"TOTAL A PAGAR: R$ {calcular_total_atual():.2f}")

    for lanche, preco in precos_lanches.items():
        tk.Checkbutton(
            frame_lanches, text=f"{lanche} (+ R$ {preco:.2f})", variable=variaveis_lanches[lanche],
            bg="#222222", fg="white", selectcolor="#141414", activebackground="#222222", activeforeground="white",
            font=("Arial", 11), command=atualizar_interface_preco
        ).pack(anchor="w", pady=1)

    # --- Sessão de Descontos e Convênios ---
    frame_descontos = tk.LabelFrame(janela_pag, text=" Benefícios e Descontos ", fg="white", bg="#222222", font=("Arial", 10, "bold"), padx=15, pady=8)
    frame_descontos.pack(fill="x", padx=20, pady=5)

    tk.Checkbutton(
        frame_descontos, text="Sou estudante (Apresentar carteira de estudante - 50% desc.)",
        variable=var_estudante, bg="#222222", fg="white", selectcolor="#141414",
        activebackground="#222222", activeforeground="white", font=("Arial", 10, "bold"),
        command=atualizar_interface_preco
    ).pack(anchor="w")

    # --- Dados de Pagamento ---
    frame_detalhes_pag = tk.LabelFrame(janela_pag, text=" Dados de Pagamento ", fg="white", bg="#222222", font=("Arial", 10, "bold"), padx=15, pady=10)
    frame_detalhes_pag.pack(fill="x", padx=20, pady=5)

    def alternar_metodo_pagamento():
        for widget in frame_detalhes_pag.winfo_children():
            widget.destroy()

        metodo = forma_pagamento.get()

        if metodo == "Pix":
            chave_aleatoria = f"pobreflix{random.randint(100000, 999999)}v7x89"
            tk.Label(frame_detalhes_pag, text="Use a chave Pix copia e cola abaixo:", fg="white", bg="#222222", font=("Arial", 11)).pack(anchor="w")
            ent_pix = tk.Entry(frame_detalhes_pag, font=("Arial", 11), width=40)
            ent_pix.insert(0, chave_aleatoria)
            ent_pix.config(state="readonly")
            ent_pix.pack(pady=5)
            tk.Label(frame_detalhes_pag, text="*O ingresso será liberado após a transferência.", fg="#AAAAAA", bg="#222222", font=("Arial", 9, "italic")).pack(anchor="w")

        elif metodo in ["Cartão de Crédito", "Cartão de Débito"]:
            tk.Label(frame_detalhes_pag, text="Número do Cartão:", fg="white", bg="#222222", font=("Arial", 10)).pack(anchor="w")
            tk.Entry(frame_detalhes_pag, font=("Arial", 10), width=35).pack(pady=2)
            
            frame_linha = tk.Frame(frame_detalhes_pag, bg="#222222")
            frame_linha.pack(fill="x", pady=2)
            
            tk.Label(frame_linha, text="Validade:", fg="white", bg="#222222", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
            tk.Entry(frame_linha, font=("Arial", 10), width=10).grid(row=1, column=0, padx=(0, 20))
            
            tk.Label(frame_linha, text="CVV:", fg="white", bg="#222222", font=("Arial", 10)).grid(row=0, column=1, sticky="w")
            tk.Entry(frame_linha, font=("Arial", 10), width=8).grid(row=1, column=1)

        elif metodo == "Dinheiro":
            tk.Label(frame_detalhes_pag, text="Retire e pague seus ingressos diretamente\nna bilheteria física com até 15 minutos de antecedência.", fg="#FFC107", bg="#222222", font=("Arial", 10, "bold"), justify="left").pack(pady=5)

    frame_radios = tk.Frame(janela_pag, bg="#141414")
    frame_radios.pack(pady=5)

    opcoes = ["Pix", "Cartão de Crédito", "Cartão de Débito", "Dinheiro"]
    for op in opcoes:
        tk.Radiobutton(
            frame_radios, text=op, variable=forma_pagamento, value=op, bg="#141414", fg="white",
            selectcolor="#222222", font=("Arial", 10, "bold"), command=alternar_metodo_pagamento
        ).pack(side="left", padx=8)

    alternar_metodo_pagamento()

    lbl_total = tk.Label(janela_pag, text=f"TOTAL A PAGAR: R$ {subtotal_ingressos:.2f}", fg="white", bg="#141414", font=("Arial", 14, "bold"))
    lbl_total.pack(pady=10)

    def processar_e_gerar_ticket():
        lanches_escolhidos = [l for l, v in variaveis_lanches.items() if v.get()]
        lanches_str = ", ".join(lanches_escolhidos) if lanches_escolhidos else "Nenhum lanche"
        
        codigo_autenticacao = f"PBR-{random.randint(10000, 99999)}-{random.randint(10, 99)}"

        # Armazenando o tipo de entrada selecionada
        tipo_entrada = "Meia-Entrada (Estudante)" if var_estudante.get() else "Inteira"

        # Importação vinda de Cadastro (onde se encontra o banco de tickets original)
        from Cadastro3 import TICKETS_COMPRADOS
        TICKETS_COMPRADOS.append({
            "filme": filme_nome,
            "dia": dia,
            "assentos": assentos,
            "total": f"R$ {calcular_total_atual():.2f}",
            "codigo": codigo_autenticacao
        })

        funcao_atualizar_menu()

        janela_ticket = tk.Toplevel()
        janela_ticket.title("Seu Bilhete Digital")
        janela_ticket.geometry("440x510")
        janela_ticket.configure(bg="#ffffff")
        janela_ticket.resizable(False, False)

        tk.Label(janela_ticket, text="========= POBREFLIX CINEMAS =========", fg="black", bg="white", font=("Courier", 12, "bold")).pack(pady=10)
        tk.Label(janela_ticket, text="COMPROVANTE DE ENTRADA / TICKET", fg="black", bg="white", font=("Courier", 11, "bold")).pack()
        
        frame_corpo_ticket = tk.Frame(janela_ticket, bg="white", padx=30)
        frame_corpo_ticket.pack(fill="both", expand=True, pady=15)

        def adicionar_linha_ticket(label, conteudo):
            f = tk.Frame(frame_corpo_ticket, bg="white")
            f.pack(fill="x", pady=3)
            tk.Label(f, text=label, fg="black", bg="white", font=("Courier", 10, "bold")).pack(side="left")
            tk.Label(f, text=conteudo, fg="black", bg="white", font=("Courier", 10)).pack(side="right")

        adicionar_linha_ticket("FILME:", filme_nome.upper())
        adicionar_linha_ticket("SESSÃO:", dia)
        adicionar_linha_ticket("ASSENTO(S):", assentos)
        adicionar_linha_ticket("TIPO ENTRADA:", tipo_entrada)
        adicionar_linha_ticket("QTD INGRESSO:", str(qtd_ingressos))
        adicionar_linha_ticket("LANCHES:", lanches_str)
        adicionar_linha_ticket("PAGAMENTO:", forma_pagamento.get().upper())
        adicionar_linha_ticket("TOTAL PAGO:", f"R$ {calcular_total_atual():.2f}")
        
        tk.Label(frame_corpo_ticket, text="-----------------------------------", fg="black", bg="white", font=("Courier", 10)).pack(pady=10)
        
        # Caso o estudante tenha selecionado a opção de meia, deixamos o lembrete explícito no ticket impresso
        if var_estudante.get():
            tk.Label(frame_corpo_ticket, text="* APRESENTAR COMPROVANTE DE ESTUDANTE NA ENTRADA *", fg="red", bg="white", font=("Courier", 8, "bold")).pack()
            tk.Label(frame_corpo_ticket, text="-----------------------------------", fg="black", bg="white", font=("Courier", 10)).pack()

        tk.Label(frame_corpo_ticket, text="CÓDIGO DE ACESSO DA BILHETERIA", fg="black", bg="white", font=("Courier", 10, "bold")).pack()
        
        tk.Label(
            frame_corpo_ticket, text=codigo_autenticacao, fg="white", bg="black",
            font=("Courier", 16, "bold"), padx=15, pady=8
        ).pack(pady=10)

        tk.Label(frame_corpo_ticket, text="Apresente este código na portaria.\nTenha uma excelente sessão!", fg="black", bg="white", font=("Courier", 9, "italic"), justify="center").pack(pady=5)

        def fechar_tudo():
            janela_ticket.destroy()
            janela_pag.destroy()

        tk.Button(janela_ticket, text="FECHAR E VOLTAR PARA O MENU", bg="black", fg="white", font=("Arial", 10, "bold"), command=fechar_tudo, cursor="hand2").pack(pady=10)

    tk.Button(
        janela_pag, text="FINALIZAR COMPRA E GERAR TICKET", bg="#4CAF50", fg="white",
        font=("Arial", 12, "bold"), width=32, height=2, command=processar_e_gerar_ticket
    ).pack(pady=10)

    atualizar_interface_preco()