class Context:
    def __init__(self, sessao) -> None:
        self.id_User = sessao[0]
        self.nome_User = sessao[1]
        self.senha_User = sessao[2]
        self.tipo_User = sessao[3]
        self.uid_User = sessao[4]
        self.usuario_User = sessao[5]