import streamlit as st
import pandas as pd

# -------------------------------
# 1️⃣ Carregar o FAQ (ou exemplo padrão)
# -------------------------------
try:
    faq = pd.read_csv("faq.csv")
except FileNotFoundError:
    faq = pd.DataFrame({
        "Pergunta": [
            "Como criar um cadastro?",
            "Como consultar um protocolo?",
            "Como alterar minha senha?"
        ],
        "Resposta": [
            "Para criar um cadastro, clique em 'Novo Cadastro' e preencha os dados obrigatórios.",
            "Acesse 'Consulta de Protocolos', informe o número e clique em 'Pesquisar'.",
            "Vá em 'Configurações > Segurança' e clique em 'Alterar Senha'."
        ]
    })

# -------------------------------
# 2️⃣ Função simples para buscar resposta
# -------------------------------
def buscar_resposta(pergunta):
    for q, r in zip(faq["Pergunta"], faq["Resposta"]):
        if pergunta.lower() in q.lower():
            return r
    return "Desculpe, não encontrei uma resposta para sua pergunta."

# -------------------------------
# 3️⃣ Interface Streamlit
# -------------------------------
st.title("💬 Citizen Support Assistant – Versão Simples")
st.write("Pergunte algo sobre o sistema e veja se há uma resposta no manual 👇")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    resposta = buscar_resposta(pergunta)
    st.success(resposta)
