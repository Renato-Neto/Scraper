from raspador import coletar_dados_com_playwright
from processamento import salvar_csv
from playwright.sync_api import sync_playwright
import validators

def corrigir_url(url):
    """
    Corrige e valida a URL fornecida pelo usuário.

    Args:
        url (str): URL do site.

    Returns:
        str: URL corrigida e válida.
    """
    # Adiciona "https://" se não estiver presente
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # Não altera URLs que já possuem extensões conhecidas
    if any(url.endswith(ext) for ext in [".com", ".com.br", ".org", ".net", ".gov"]):
        pass
    # Não altera URLs que já possuem caminhos adicionais
    elif "/" in url.split("//")[-1]:
        pass
    else:
        # Adiciona ".com.br" apenas se não houver extensão ou caminho
        url += ".com.br"

    # Verifica se a URL é válida
    if not validators.url(url):
        raise ValueError(f"URL inválida: {url}")

    return url

def main():
    print("Bem-vindo ao query_ferretDados!")

    with sync_playwright() as p:
        while True:
            try:
                url = input("Insira a URL do site que deseja raspar: ").strip()
                url = corrigir_url(url)
                print(f"URL válida e corrigida: {url}")
                break
            except ValueError as e:
                print(f"Erro: {e}")

        navegador = input("Escolha o navegador (1 - Chromium, 2 - Firefox, 3 - WebKit): ").strip()
        navegadores = {"1": "chromium", "2": "firefox", "3": "webkit"}
        navegador = navegadores.get(navegador, "chromium")
        print(f"Navegador selecionado: {navegador}")

        print("\nEscolha o que deseja buscar:")
        print("1 - Produtos (Nome, preço e imagem, se possível)")
        tipo = input("Digite o número da opção desejada: ").strip()

        if tipo != "1":
            print("Opção inválida. Encerrando o programa.")
            return

        try:
            print("\nBuscando produtos...")
            resultados = coletar_dados_com_playwright(p, url, navegador)

            if not resultados or not resultados["produto"]:
                print("Nenhum produto relevante encontrado.")
                return

            print("\nProdutos encontrados:")
            for i, (nome, preco, link, imagem) in enumerate(zip(resultados["produto"], resultados["preço"], resultados["link"], resultados["imagem"]), start=1):
                print(f"{i}. {nome} - Preço: {preco} - Link: {link} - Imagem: {imagem}")

            print("\nSalvando resultados em CSV...")
            salvar_csv(resultados, "produtos")
            print("Resultados salvos com sucesso!")

        except Exception as e:
            print(f"Erro ao buscar ou processar dados: {e}")

if __name__ == "__main__":
    main()
    
    
    
def scrape_overcome(page_content):
    # Código específico para o site Overcome
    pass

def scrape_sometimesonline(page_content):
    # Código específico para o site Sometimes Online
    pass


def scrape_site(url, content):
    if "overcome.com.br" in url:
        return scrape_overcome(content)
    elif "sometimesonline.com" in url:
        return scrape_sometimesonline(content)
    else:
        raise ValueError("Site não suportado.")
