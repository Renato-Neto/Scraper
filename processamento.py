import pandas as pd
import os

def processar_dados(resultados, tipo_busca):
    """
    Processa os dados coletados e os organiza em um DataFrame.

    Args:
        resultados (dict): Dados coletados divididos por categorias (ex.: produto, preço).
        tipo_busca (str): O tipo de busca realizada (ex.: 'produtos').

    Returns:
        DataFrame: Dados organizados em formato tabular.
    """
    if not resultados or all(len(valores) == 0 for valores in resultados.values()):
        raise ValueError("Nenhum dado foi coletado para processar.")

    print(f"Processando dados para o tipo de busca: {tipo_busca}...")

    # Tratamento para busca de produtos
    if tipo_busca == "produtos":
        # Mapear colunas esperadas
        data = {
            "Nome do Produto": resultados.get("produto", []),
            "Preço": resultados.get("preço", [])
        }

        # Preencher valores ausentes para manter a consistência
        max_len = max(len(data[coluna]) for coluna in data)
        for coluna in data:
            data[coluna].extend(["N/A"] * (max_len - len(data[coluna])))

        # Criar DataFrame
        df = pd.DataFrame(data)
        df.drop_duplicates(inplace=True)
        print(f"Dados processados com sucesso! Total de registros: {len(df)}")
        return df

    elif tipo_busca == "artigos":
        data = {
            "Título": resultados.get("artigos", []),
            "Conteúdo": resultados.get("texto", [])
        }

        # Preenchendo valores ausentes
        max_len = max(len(data[coluna]) for coluna in data)
        for coluna in data:
            data[coluna].extend(["N/A"] * (max_len - len(data[coluna])))

        df = pd.DataFrame(data)
        df.drop_duplicates(inplace=True)
        print(f"Dados processados com sucesso! Total de registros: {len(df)}")
        return df

    else:
        raise ValueError(f"Tipo de busca '{tipo_busca}' não suportado.")

def salvar_csv(dados, tipo_busca):
    """
    Salva os dados coletados em um arquivo CSV.

    Args:
        dados (dict): Dados coletados (produtos, preços, links, imagens).
        tipo_busca (str): Tipo de busca realizada (ex.: 'produtos').
    """
    filename = f"{tipo_busca}_output.csv"
    filepath = os.path.join(os.getcwd(), filename)
    df = pd.DataFrame(dados)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"Dados salvos com sucesso em: {filepath}")
