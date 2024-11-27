import streamlit as st
from raspador import coletar_dados_com_playwright
from processamento import processar_dados
import pandas as pd
import os

# Configuração do tema do Streamlit
st.set_page_config(
    page_title="Query Ferret",
    page_icon="🦡",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Carregar a logo
logo_path = os.path.join("static", "imgs", "logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.warning("Logo não encontrada no caminho: 'static/imgs/logo.png'")
# Estilo customizado com Streamlit
st.markdown(
    """
    <style>
        /* Fundo principal */
        body, .stApp {
            background-color: #a07495;
            color: #333333;
        }

        /* Sidebar */
        .stSidebar {
            background-color: #120A15;
            color: #120A15;
        }

        /* Botões */
        .stButton>button {
            background-color: #6a1b9a;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
        }
        .stButton>button:hover {
            background-color: #D8BCAC;
        }

        /* Títulos */
        h1, h2, h3, h4, h5, h6 {
            color: #6a1b9a;
        }

        /* Inputs e Áreas de Texto */
        textarea, input {
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 5px;
            color: #333333;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e descrição do aplicativo
st.title("Query Ferret: Web Scraping Inteligente 🦡")
st.subheader("Explore e extraia dados da web com eficiência e estilo!")

# Barra lateral para configurações
st.sidebar.header("Configurações")
navegador = st.sidebar.radio("Selecione o navegador:", ["chromium", "firefox", "webkit"], index=0)
formato = st.sidebar.selectbox("Formato de exportação:", ["CSV", "XLSX", "JSON"])
timeout = st.sidebar.slider("Tempo limite por página (segundos):", min_value=10, max_value=120, value=30)
limite = st.sidebar.number_input("Limite de itens a raspar por página:", min_value=1, max_value=100, value=10)

# Entradas organizadas
st.header("Entradas")
urls = st.text_area("Insira uma ou mais URLs (separadas por vírgula):", placeholder="https://site1.com, https://site2.com")
file_upload = st.file_uploader("Ou carregue um arquivo .txt com URLs:", type=["txt"])

# Processar URLs do arquivo carregado
if file_upload:
    try:
        urls = file_upload.read().decode("utf-8").strip().split("\n")
        st.success("URLs carregadas com sucesso!")
    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")

# Botão de execução
if st.button("Iniciar Scraping"):
    if urls:
        urls = [url.strip() for url in urls.split(",") if url.strip()]  # Limpar e separar as URLs
        if urls:
            try:
                st.info("Coletando dados... Aguarde.")
                progress = st.progress(0)  # Barra de progresso
                resultados_completos = []

                # Iterar pelas URLs
                for idx, url in enumerate(urls):
                    progress.progress((idx + 1) / len(urls))  # Atualizar progresso
                    resultados = coletar_dados_com_playwright(url, navegador)
                    if resultados:
                        processados = processar_dados(resultados)
                        resultados_completos.append(processados)
                    else:
                        st.warning(f"Nenhum dado encontrado para a URL: {url}")

                # Consolidar resultados
                if resultados_completos:
                    df_final = pd.concat(resultados_completos, ignore_index=True)
                    st.success(f"Scraping concluído! Total de {len(df_final)} itens.")
                    st.dataframe(df_final)

                    # Exportar resultados
                    if formato == "CSV":
                        csv = df_final.to_csv(index=False).encode("utf-8")
                        st.download_button("Baixar como CSV", data=csv, file_name="dados_extraidos.csv", mime="text/csv")
                    elif formato == "XLSX":
                        df_final.to_excel("dados_extraidos.xlsx", index=False)
                        with open("dados_extraidos.xlsx", "rb") as f:
                            st.download_button("Baixar como Excel", data=f, file_name="dados_extraidos.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    elif formato == "JSON":
                        json_data = df_final.to_json(orient="records", indent=2)
                        st.download_button("Baixar como JSON", data=json_data, file_name="dados_extraidos.json", mime="application/json")
                else:
                    st.warning("Nenhum dado foi coletado.")
            except Exception as e:
                st.error(f"Erro durante o scraping: {e}")
        else:
            st.warning("Por favor, insira URLs válidas.")
    else:
        st.warning("Por favor, forneça URLs ou carregue um arquivo.")
