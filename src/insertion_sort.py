def insertion_sort(disciplinas, ao_passo=None):

    lista = list(disciplinas)

    def registrar(tipo, **detalhes):
        if ao_passo is not None:
            ao_passo({"tipo": tipo, **detalhes})

    if ao_passo is not None:
        registrar("inicio", lista=list(lista))

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        registrar("selecao", passagem=i, codigo=atual["codigo"])

        while j >= 0 and lista[j]["codigo"] > atual["codigo"]:
            registrar("deslocamento", codigo=lista[j]["codigo"],
                      origem=j, destino=j + 1)
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual
        if ao_passo is not None:
            registrar("insercao", codigo=atual["codigo"],
                      posicao=j + 1, lista=list(lista))

    if ao_passo is not None:
        registrar("fim", lista=list(lista))
    return lista
