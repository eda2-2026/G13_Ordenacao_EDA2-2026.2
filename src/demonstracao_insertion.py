from src.insertion_sort import insertion_sort


def formatar_codigos(lista):
    return " | ".join(d["codigo"] for d in lista) or "(lista vazia)"


def imprimir_passo(evento):
    tipo = evento["tipo"]
    if tipo == "inicio":
        print("Antes: " + formatar_codigos(evento["lista"]))
    elif tipo == "selecao":
        print(f"\nPassagem {evento['passagem']} - inserir {evento['codigo']}")
    elif tipo == "deslocamento":
        print(f"Deslocando {evento['codigo']}: "
              f"posicao {evento['origem']} -> {evento['destino']}")
    elif tipo == "insercao":
        print(f"Inserindo {evento['codigo']} na posicao {evento['posicao']}")
        print("Lista: " + formatar_codigos(evento["lista"]))
    elif tipo == "fim":
        print("\nDepois: " + formatar_codigos(evento["lista"]))


def demonstrar_insertion_sort(disciplinas):
    # Demonstra a ordenacao de toda a base na ordem real do JSON.
    # O insertion_sort cria a copia e preserva a entrada.
    amostra = disciplinas
    print("\n=== Demonstracao do Insertion Sort ===")
    print(f"Base completa: {len(amostra)} disciplinas na ordem do JSON.")
    print("Criterio: codigo crescente. As posicoes comecam em 0.")
    insertion_sort(amostra, ao_passo=imprimir_passo)
    print("=== Fim da demonstracao ===\n")


if __name__ == "__main__":
    from src.carregaDados import carregar_disciplinas

    demonstrar_insertion_sort(carregar_disciplinas())
