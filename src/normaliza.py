import unicodedata


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    # Pontuacao separa palavras; espacos extras nao alteram a pesquisa.
    texto = "".join(c if c.isalnum() else " " for c in texto)
    return " ".join(texto.split())
