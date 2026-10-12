from src.tabela_hash import TabelaHash
from src.normaliza import normalizar


def construir_indice_professor(disciplinas):
    indice = TabelaHash(capacidade_inicial=max(16, len(disciplinas)))
    for d in disciplinas:
        palavras_disciplina = set()
        for professor in d["professores"]:
            palavras_disciplina.update(normalizar(professor).split())
        for palavra in sorted(palavras_disciplina):
            existentes = indice.buscar(palavra)
            if existentes is None:
                indice.inserir(palavra, [d])
            else:
                existentes.append(d)
    return indice


def busca_por_professor(indice, nome_professor):
    palavras = normalizar(nome_professor).split()
    if not palavras:
        return []
    candidatos = indice.buscar(palavras[0]) or []
    # Todas as palavras devem pertencer ao mesmo professor da disciplina.
    return [d for d in candidatos if any(
        all(palavra in normalizar(professor).split() for palavra in palavras)
        for professor in d["professores"]
    )]
