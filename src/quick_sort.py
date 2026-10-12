def quick_sort(disciplinas, ao_passo=None):
    """Ordena uma copia por codigo usando particao de Lomuto.

    Nao modifica os registros. Codigos iguais podem trocar de ordem.
    """
    lista = list(disciplinas)

    def registrar(tipo, **detalhes):
        if ao_passo is not None:
            ao_passo({"tipo": tipo, **detalhes})

    def trocar(a, b):
        if a != b:
            lista[a], lista[b] = lista[b], lista[a]
            if ao_passo is not None:
                registrar("troca", origem=a, destino=b, lista=list(lista))

    def particionar(inicio, fim):
        pivo = lista[fim]["codigo"]
        registrar("particao", inicio=inicio, fim=fim, pivo=pivo)
        i = inicio
        for j in range(inicio, fim):
            registrar("comparacao", codigo=lista[j]["codigo"], pivo=pivo,
                      menor_ou_igual=lista[j]["codigo"] <= pivo)
            if lista[j]["codigo"] <= pivo:
                trocar(i, j)
                i += 1
        trocar(i, fim)
        if ao_passo is not None:
            registrar("pivo", codigo=pivo, posicao=i, lista=list(lista))
        return i

    def ordenar(inicio, fim):
        # Recorre apenas no menor lado para limitar a pilha a O(log n).
        while inicio < fim:
            posicao = particionar(inicio, fim)
            if posicao - inicio < fim - posicao:
                ordenar(inicio, posicao - 1)
                inicio = posicao + 1
            else:
                ordenar(posicao + 1, fim)
                fim = posicao - 1

    if ao_passo is not None:
        registrar("inicio", lista=list(lista))
    ordenar(0, len(lista) - 1)
    if ao_passo is not None:
        registrar("fim", lista=list(lista))
    return lista
