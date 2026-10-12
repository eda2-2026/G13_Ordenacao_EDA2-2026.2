from src.tabela_hash import TabelaHash
from src.normaliza import normalizar

def construir_indice_professor(disciplinas):

    indice = TabelaHash(capacidade_inicial=max(16, len(disciplinas)))
    for d in disciplinas:
        for professor in d["professores"]:
            chave = normalizar(professor)
            existentes = indice.buscar(chave)
            if existentes is None:
                indice.inserir(chave, [d])
            else:
                existentes.append(d)
    return indice

def busca_por_professor(indice, nome_professor):
    resultado = indice.buscar(normalizar(nome_professor))
    return resultado if resultado else []
