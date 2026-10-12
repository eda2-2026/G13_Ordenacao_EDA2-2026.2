def busca_binaria(disciplinas, codigo_alvo):
    """Busca um codigo em uma lista previamente ordenada por codigo."""
    lo, hi = 0, len(disciplinas) - 1
    while lo <= hi:
        meio = (lo + hi) // 2
        atual = disciplinas[meio]["codigo"]
        if atual == codigo_alvo:
            return disciplinas[meio]
        if atual < codigo_alvo:
            lo = meio + 1
        else:
            hi = meio - 1
    return None
