import os
import streamlit as st
from groq import Groq

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Naty AI Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# PROMPT DE SISTEMA PERSONALIZADO
# -----------------------------
CUSTOM_PROMPT = """
Você é o "Naty AI Assistant", um assistente de IA completo e especializado em:

- Python
- SQL
- DAX
- Power BI
- ETL
- Engenharia de Dados
- Análise de Dados
- Lógica de Programação
- Modelagem
- Automações no Zoho e Power BI
- Melhores práticas de código

REGRAS:
1. Responda de forma clara, objetiva e didática.
2. Sempre que possível, ofereça exemplos práticos.
3. Formate códigos corretamente em blocos ```.
4. Não limite o tema apenas a Python — responda perguntas gerais de tecnologia.
5. Caso receba perguntas pessoais ou fora da área de tecnologia, responda educadamente que seu foco é auxiliar com programação, dados e tecnologia.
6. Antes de dar uma resposta final, pense passo a passo e garanta clareza.

Seu objetivo é ajudar profissionais e estudantes da área de dados a entender e resolver problemas técnicos.
"""

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("✨ Naty AI Assistant")
    st.markdown("Seu assistente pessoal de programação e dados.")
    
    groq_api_key = st.text_input(
        "🔑 API Key da Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para ajudar no seu aprendizado e trabalho com:")
    st.markdown("• Python\n• SQL\n• DAX\n• Power BI\n• ETL\n• Zoho Creator")
    
    st.markdown("---")
    st.markdown("🌐 Meus Repositórios:")
    st.markdown("🔗 [GitHub - NatyAnalytics](https://github.com/NatyAnalytcs-1)")

    st.link_button("📧 Suporte / Contato", "mailto:nataliafelipy@gmail.com.br")

# -----------------------------
# TÍTULO
# -----------------------------
st.title("✨ Naty AI Assistant")
st.caption("Faça sua pergunta sobre Python, SQL, DAX, Power BI ou programação.")

# -----------------------------
# HISTÓRICO DE MENSAGENS
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# INICIALIZA CLIENTE
# -----------------------------
client = None

if groq_api_key:
    try:
        client = Groq(api_key=groq_api_key)
    except Exception as e:
        st.sidebar.error(f"Erro ao inicializar Groq: {e}")
        st.stop()
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq para continuar.")

# -----------------------------
# INPUT DO USUÁRIO
# -----------------------------
if prompt := st.chat_input("Digite sua pergunta:"):
    
    if not client:
        st.warning("Insira sua API Key na barra lateral para começar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    messages_for_api.extend(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-20b",
                    temperature=0.7,
                    max_tokens=2048,
                )

                resposta = chat_completion.choices[0].message.content

                st.markdown(resposta)
                st.session_state.messages.append(
                    {"role": "assistant", "content": resposta}
                )

            except Exception as e:
                st.error(f"Erro ao comunicar com a API: {e}")

