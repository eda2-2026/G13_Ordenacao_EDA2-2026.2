from src.quick_sort import quick_sort
from src.demonstracao_insertion import formatar_codigos


def imprimir_passo(evento):
    tipo = evento["tipo"]
    if tipo == "inicio":
        print("Antes: " + formatar_codigos(evento["lista"]))
    elif tipo == "particao":
        print(f"\nParticao [{evento['inicio']}, {evento['fim']}] - pivo {evento['pivo']}")
    elif tipo == "comparacao":
        resultado = "sim" if evento["menor_ou_igual"] else "nao"
        print(f"{evento['codigo']} <= {evento['pivo']}? {resultado}")
    elif tipo == "troca":
        print(f"Troca entre posicoes {evento['origem']} e {evento['destino']}")
        print("Lista: " + formatar_codigos(evento["lista"]))
    elif tipo == "pivo":
        print(f"Pivo {evento['codigo']} fixado na posicao {evento['posicao']}")
        print("Lista: " + formatar_codigos(evento["lista"]))
    elif tipo == "fim":
        print("\nDepois: " + formatar_codigos(evento["lista"]))


def demonstrar_quick_sort(disciplinas):
    print("\n=== Demonstracao do QuickSort ===")
    print(f"Base completa: {len(disciplinas)} disciplinas na ordem do JSON.")
    print("Criterio: codigo crescente. Pivo: ultimo elemento da particao.")
    print("As posicoes comecam em 0.")
    quick_sort(disciplinas, ao_passo=imprimir_passo)
    print("=== Fim da demonstracao ===\n")


if __name__ == "__main__":
    from src.carregaDados import carregar_disciplinas

    demonstrar_quick_sort(carregar_disciplinas())
