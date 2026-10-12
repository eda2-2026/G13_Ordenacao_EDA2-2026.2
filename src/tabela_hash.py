class NoHash:
    ##Nó de lista encadeada — trata as colisoes dentro do mesmo bucket
    __slots__ = ("chave", "valor", "proximo")

    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class TabelaHash:
    def __init__(self, capacidade_inicial=16, fator_carga_max=0.75):
        self._capacidade = capacidade_inicial
        self._fator_carga_max = fator_carga_max
        self._tamanho = 0
        self._buckets = [None] * self._capacidade

    def _hash(self, chave):
        # djb2: função de hash 
        h = 5381
        for c in str(chave):
            h = ((h * 33) + ord(c)) & 0xFFFFFFFF
        return h % self._capacidade

    def inserir(self, chave, valor):
        if self._tamanho / self._capacidade >= self._fator_carga_max:
            self._redimensionar()

        indice = self._hash(chave)
        no = self._buckets[indice]
        while no:
            if no.chave == chave:
                no.valor = valor  # se já existe: atualiza
                return
            no = no.proximo

        novo_no = NoHash(chave, valor)
        novo_no.proximo = self._buckets[indice]
        self._buckets[indice] = novo_no
        self._tamanho += 1

    def buscar(self, chave):
        indice = self._hash(chave)
        no = self._buckets[indice]
        while no:
            if no.chave == chave:
                return no.valor
            no = no.proximo
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        no, anterior = self._buckets[indice], None
        while no:
            if no.chave == chave:
                if anterior:
                    anterior.proximo = no.proximo
                else:
                    self._buckets[indice] = no.proximo
                self._tamanho -= 1
                return True
            anterior, no = no, no.proximo
        return False

    def _redimensionar(self):
        ## quando o fator de carga fica alto,
         ##  evitando buckets muito longos
        antigos = self._buckets
        self._capacidade *= 2
        self._buckets = [None] * self._capacidade
        self._tamanho = 0
        for no in antigos:
            while no:
                self.inserir(no.chave, no.valor)
                no = no.proximo

    def __len__(self):
        return self._tamanho