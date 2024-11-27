Query Ferret 🦦

Web Scraping Inteligente e Modular

Query Ferret é um projeto de web scraping poderoso e escalável, projetado para extrair dados de diversos tipos de sites, como e-commerces, portais de notícias e plataformas especializadas. Utilizando Python e Streamlit, o aplicativo oferece uma interface intuitiva para facilitar o uso tanto por desenvolvedores quanto por usuários leigos.

O objetivo é transformar dados dispersos da web em informações organizadas e úteis, com opções de exportação flexíveis e suporte a múltiplos formatos.
🚀 Funcionalidades

    Scraping em Lote: Forneça múltiplas URLs (lista ou arquivo .txt) e processe todas de uma só vez.
    Suporte Multiplataforma: Compatível com sites populares como Amazon, Mercado Livre, G1, Reuters, Kaya Mind, e mais.
    Configurações Personalizáveis:
        Formato de exportação: .csv, .xlsx e .json.
        Limite de itens por site.
        Tempo limite por página.
    Interface Moderna:
        Desenvolvida com Streamlit.
        Tema clean em roxo/preto com feedback em tempo real.
        Tabela interativa para exibir resultados.
    Exportação Facilitada:
        Download direto dos dados processados.
        Visualização de imagens e links no resultado.
    Modularidade:
        Código organizado em módulos para scraping, processamento e interface.
        Facilmente expansível para novos sites.

🛠 Tecnologias Utilizadas

    Python: Backend principal.
    Streamlit: Criação da interface de usuário.
    Playwright: Raspagem dinâmica para lidar com sites baseados em JavaScript.
    Pandas: Processamento e manipulação de dados.
    OpenPyXL: Exportação de arquivos Excel.
    Requests e BeautifulSoup: Raspagem de sites mais simples.

📈 Próximas Melhorias

    Suporte adicional a APIs para scraping e integração.
    Gráficos de análise de tendências e dados.
    Agendamento de scraping automático.
    Otimização para dispositivos móveis.

🧑‍💻 Como Contribuir

    Faça um fork do repositório.
    Crie uma branch para sua funcionalidade (git checkout -b feature/nova-funcionalidade).
    Submeta suas mudanças com um Pull Request.

📂 Estrutura do Projeto

Query_Ferret/
├── app_streamlit.py       # Interface principal do Streamlit
├── chupa.py               # Coordenador principal do projeto
├── processamento.py       # Limpeza e estruturação dos dados
├── raspador.py            # Lógica de scraping para diferentes sites
├── requirements.txt       # Dependências do projeto
└── README.md              # Arquivo atual

🎯 Objetivo do Projeto

O Query Ferret nasceu para facilitar a coleta de dados da web de forma acessível e eficiente. Seja para um projeto pessoal ou profissional, o objetivo é proporcionar uma ferramenta flexível e fácil de usar para transformar informações da web em insights valiosos.
