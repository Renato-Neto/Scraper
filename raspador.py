from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def coletar_dados_com_playwright(playwright, url, navegador):
    """
    Coleta nomes, preços e outras informações de produtos, tentando ser o mais universal possível.

    Args:
        playwright (Playwright): Instância do Playwright.
        url (str): URL do site.
        navegador (str): Navegador a ser usado ('chromium', 'firefox', 'webkit').

    Returns:
        dict: Dados estruturados com nomes, preços, links e imagens.
    """
    try:
        browser = configurar_navegador(playwright, navegador)
        page = browser.new_page()
        print(f"Acessando a URL: {url}")
        page.goto(url, timeout=60000)

        # Aguarda o carregamento completo da página
        page.wait_for_load_state("networkidle", timeout=40000)

        # Obtém o conteúdo da página
        html = page.content()
        browser.close()

        soup = BeautifulSoup(html, 'html.parser')
        produtos = []

        # Lista de possíveis classes para nomes, preços e links
        nome_classes = ["product__title", "product-title", "item-title", "product_name"]
        preco_classes = ["money", "product__price", "price", "product-price"]
        contenedor_classes = ["product__details", "product", "item"]

        # Buscar contêineres de produtos
        for cont_class in contenedor_classes:
            for produto_div in soup.find_all("div", class_=cont_class):
                # Nome do Produto
                nome_produto = None
                for nome_class in nome_classes:
                    nome_tag = produto_div.find(class_=nome_class)
                    if nome_tag:
                        nome_produto = nome_tag.text.strip()
                        break
                if not nome_produto:
                    nome_produto = "Nome não encontrado"

                # Preço do Produto
                preco_produto = None
                for preco_class in preco_classes:
                    preco_tag = produto_div.find(class_=preco_class)
                    if preco_tag:
                        preco_produto = preco_tag.text.strip()
                        break
                if not preco_produto:
                    preco_produto = "Preço não encontrado"

                # Link do Produto
                link_tag = produto_div.find_parent("a")
                link_produto = link_tag["href"] if link_tag else "Link não encontrado"

                # Imagem do Produto
                # Imagem do Produto
                imagem_tag = produto_div.find("img")
                imagem_url = imagem_tag["src"] if imagem_tag and "src" in imagem_tag.attrs else "Imagem não encontrada"

                # Adicionar produto à lista
                produtos.append({
                    "Nome do Produto": nome_produto,
                    "Preço": preco_produto,
                    "Link": link_produto,
                    "Imagem": imagem_url
                })

        if not produtos:
            print("Nenhum produto relevante encontrado.")
        else:
            print(f"{len(produtos)} produtos encontrados com sucesso.")

        return {"produto": [p["Nome do Produto"] for p in produtos],
                "preço": [p["Preço"] for p in produtos],
                "link": [p["Link"] for p in produtos],
                "imagem": [p["Imagem"] for p in produtos]}
    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
        return {}

def configurar_navegador(playwright, escolha):
    """
    Configura o navegador Playwright com base na escolha do usuário.
    """
    navegadores = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit
    }

    if escolha not in navegadores:
        raise ValueError("Navegador inválido. Escolha entre chromium, firefox ou webkit.")

    return navegadores[escolha].launch(headless=True)
