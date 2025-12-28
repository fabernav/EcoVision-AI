# 🌿 EcoVision AI - Auditoria Ambiental Inteligente

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?style=for-the-badge&logo=google-gemini&logoColor=white)

O **EcoVision AI** é uma plataforma de inteligência climática que utiliza Visão Computacional e IA Generativa Multimodal (**Gemini 2.5 Flash**) para transformar imagens de descartes de resíduos em dashboards de auditoria ambiental (ESG) em tempo real.

O projeto automatiza a identificação de materiais e a quantificação do impacto ecológico, entregando dados acionáveis para estratégias de economia circular e relatórios de sustentabilidade.

---

## 🚀 Funcionalidades Principais

* **Identificação Multimodal:** Reconhecimento automático de materiais (PET, Alumínio, Papel, Vidro e Outros) através do processamento de imagens por IA.
* **Analytics de Carbono:** Cálculo dinâmico do **CO2 Evitado** (ou débitos ambientais) baseado em fatores de conversão industriais e volumetria estimada.
* **UX Inteligente (Apple/Lovable Style):** Interface minimalista com cards que reagem aos dados, alterando cores e status para destacar riscos ambientais (Cards Vermelhos para débitos).
* **Relatórios Técnicos Executivos:** Geração de auditoria detalhada via IA com análise de cenário, estimativas de peso e sugestões de mitigação de impacto.
* **Pipeline Blindado:** Tratamento de respostas via Regex para garantir a integridade do JSON e evitar falhas de processamento em múltiplas análises.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.9+
* **Frontend:** Streamlit (Custom CSS para Design Premium)
* **Motor de IA:** Google Gemini 2.5 Flash API
* **Dados e Gráficos:** Plotly Express & Pandas
* **Processamento de Imagem:** Pillow (PIL)

---

## 📦 Estrutura de Arquivos

```text
├── app.py              # Aplicação principal (Dashboard e Lógica de IA)
├── requirements.txt    # Gerenciamento de dependências
├── .gitignore          # Proteção de chaves de API e arquivos temporários
└── README.md           # Documentação técnica completa
🔧 Instalação e Uso
1. Pré-requisitos
Python instalado no sistema.

API Key do Google AI Studio.

2. Passo a Passo
Bash

# Clone o repositório
git clone [https://github.com/fabernav/EcoVision-AI.git](https://github.com/fabernav/EcoVision-AI.git)

# Acesse a pasta do projeto
cd EcoVision-AI

# Instale as dependências necessárias
pip install -r requirements.txt

# Inicie a aplicação
streamlit run app.py
🛡️ Segurança e Boas Práticas
Este repositório foi desenvolvido com foco em segurança:

Isolamento de Credenciais: A API Key não é hardcoded. O sistema exige a inserção via sidebar para garantir que chaves privadas não sejam versionadas.

Configuração de Ignore: O arquivo .gitignore protege o projeto contra o envio de ambientes virtuais (venv/), arquivos de sistema e binários de teste.

📈 Impacto e Visão ESG
O diferencial do EcoVision AI é converter dados visuais em KPIs ambientais. Em vez de apenas identificar o lixo, a ferramenta quantifica o benefício climático, permitindo que empresas monitorem sua conformidade ambiental e comprovem o ROI de suas iniciativas sustentáveis de forma visual e transparente.

Desenvolvido por Fabrício - Analista de Soluções de IA.