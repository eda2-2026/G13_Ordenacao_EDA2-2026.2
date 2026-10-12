from src.demonstracao_insertion import demonstrar_insertion_sort
from src.insertion_sort import insertion_sort
from src.carregaDados import carregar_disciplinas
from src.busca_binaria import busca_binaria
from src.busca_por_nome import construir_indice_nome, busca_por_nome
from src.busca_por_professor import construir_indice_professor, busca_por_professor


def imprimir_resultados(resultados):
    if resultados:
        for r in resultados:
            print(f"{r['codigo']} - {r['nome']} ({r['professor']})")
    else:
        print("Nenhuma disciplina encontrada.")


def main():
    disciplinas = carregar_disciplinas()
    print("Antes (primeiros 5 codigos do JSON): " +
          " | ".join(d["codigo"] for d in disciplinas[:5]))
    disciplinas_ordenadas = insertion_sort(disciplinas)
    print("Depois (primeiros 5 codigos ordenados): " +
          " | ".join(d["codigo"] for d in disciplinas_ordenadas[:5]))
    print(f"{len(disciplinas_ordenadas)} disciplinas ordenadas com Insertion Sort.")
    indice_nome = construir_indice_nome(disciplinas_ordenadas)
    indice_professor = construir_indice_professor(disciplinas_ordenadas)

    while True:
        print("1 - Buscar por codigo (busca binaria)")
        print("2 - Buscar por nome (tabela hash)")
        print("3 - Buscar por professor (tabela hash)")
        print("4 - Demonstrar Insertion Sort")
        print("0 - Sair")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            codigo = input("Codigo: ").strip().upper()
            r = busca_binaria(disciplinas_ordenadas, codigo)
            imprimir_resultados([r] if r else [])
        elif opcao == "2":
            termo = input("Palavra do nome: ").strip()
            imprimir_resultados(busca_por_nome(indice_nome, termo))
        elif opcao == "3":
            professor = input("Nome do professor: ").strip()
            imprimir_resultados(busca_por_professor(indice_professor, professor))
        elif opcao == "4":
            demonstrar_insertion_sort(disciplinas)
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
