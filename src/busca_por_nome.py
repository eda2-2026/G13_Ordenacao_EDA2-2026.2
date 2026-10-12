from src.tabela_hash import TabelaHash
from src.normaliza import normalizar

def construir_indice_nome(disciplinas):
    indice = TabelaHash(capacidade_inicial=max(16, len(disciplinas) * 4))
    for d in disciplinas:
        for palavra in normalizar(d["nome"]).split():
            existentes = indice.buscar(palavra)
            if existentes is None:
                indice.inserir(palavra, [d])
            else:
                existentes.append(d)
    return indice

def busca_por_nome(indice, termo):
    palavras = normalizar(termo).split()
    if not palavras:
        return []

    resultado_por_codigo = {}
    for i, palavra in enumerate(palavras):
        encontrados = indice.buscar(palavra)
        if not encontrados:
            return []
        codigos_da_palavra = {d["codigo"] for d in encontrados}
        if i == 0:
            resultado_por_codigo = {d["codigo"]: d for d in encontrados}
        else:
            resultado_por_codigo = {
                codigo: d for codigo, d in resultado_por_codigo.items()
                if codigo in codigos_da_palavra
            }
        if not resultado_por_codigo:
            return []

    return list(resultado_por_codigo.values())
