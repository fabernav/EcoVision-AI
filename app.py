import streamlit as st
from google import genai
import PIL.Image
import pandas as pd
import plotly.express as px
import json
import re

# 1. Configuração da Página
st.set_page_config(page_title="EcoVision AI", page_icon="🌿", layout="wide")

# 2. Estilo CSS Style Apple / Lovable
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }

    .main-title {
        color: #10b981;
        font-size: 3rem !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: #64748b;
        text-align: center;
        margin-bottom: 3rem;
    }

    .metric-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .card-negative { border: 2px solid #ef4444 !important; background: #fffafa !important; }
    .card-positive { border: 2px solid #10b981 !important; }

    .metric-label {
        color: #1e293b !important;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #0f172a !important;
        font-weight: 700;
        font-size: 1.4rem;
    }

    .stButton>button {
        width: 100%;
        background-color: #10b981;
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 0.8rem;
        font-weight: 600;
    }

    .report-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        color: #1e293b; 
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">EcoVision AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Auditoria Ambiental com Inteligência Artificial Multimodal.</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ⚙️ Engine")
    api_key = st.text_input("Gemini API Key", type="password", help="Pegue sua chave no Google AI Studio")
    st.info("A chave não fica salva no código por segurança.")

col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.markdown("### 📷 Entrada de Imagem")
    uploaded_file = st.file_uploader("Upload de resíduos", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        img = PIL.Image.open(uploaded_file)
        st.image(img, use_container_width=True)
        btn_analisar = st.button("EXECUTAR ANÁLISE ESG 🚀")

with col_right:
    if uploaded_file and 'btn_analisar' in locals() and btn_analisar:
        if not api_key:
            st.warning("⚠️ Adicione sua API Key na barra lateral.")
        else:
            client = genai.Client(api_key=api_key, http_options={'api_version': 'v1'})
            with st.spinner('Processando auditoria...'):
                prompt = """
                Aja como auditor ESG. Analise a imagem e retorne APENAS um JSON:
                "pet_kg", "aluminio_kg", "papel_kg", "vidro_kg", "outros_kg", "total_co2", "reciclabilidade", "relatorio_texto"
                """
                try:
                    response = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt, img])
                    match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if match:
                        res_data = json.loads(match.group(0))
                        co2_val = float(res_data.get('total_co2', 0))
                        card_style = "card-negative" if co2_val < 0 else "card-positive"
                        label_text = "CO2 (DÉBITO)" if co2_val < 0 else "CO2 EVITADO"

                        m1, m2 = st.columns(2)
                        with m1:
                            st.markdown(f'<div class="metric-card {card_style}"><div class="metric-label">{label_text}</div><div class="metric-value">{co2_val} kg</div></div>', unsafe_allow_html=True)
                        with m2:
                            st.markdown(f'<div class="metric-card"><div class="metric-label">RECICLABILIDADE</div><div class="metric-value">{res_data.get("reciclabilidade")}</div></div>', unsafe_allow_html=True)

                        st.write("")
                        df = pd.DataFrame({
                            'Material': ['PET', 'Alumínio', 'Papel', 'Vidro', 'Outros'],
                            'kg': [float(res_data.get('pet_kg', 0)), float(res_data.get('aluminio_kg', 0)), 
                                   float(res_data.get('papel_kg', 0)), float(res_data.get('vidro_kg', 0)), 
                                   float(res_data.get('outros_kg', 0))]
                        })
                        fig = px.bar(df, x='Material', y='kg', template='plotly_white', color_discrete_sequence=['#10b981'])
                        fig.update_layout(height=300, margin=dict(l=0,r=0,b=20,t=10))
                        st.plotly_chart(fig, use_container_width=True)
                        
                        st.markdown(f"<div class='report-card'>{res_data.get('relatorio_texto')}</div>", unsafe_allow_html=True)
                except Exception as e:
                    if "429" in str(e): st.error("Limite de requisições atingido. Aguarde 30s.")
                    else: st.error(f"Erro: {e}")
    else:
        st.info("Aguardando imagem para análise...")