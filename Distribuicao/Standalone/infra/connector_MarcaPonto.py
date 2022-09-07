from contextvars import Context
from datetime import datetime

from Distribuicao.Standalone.infra.connector_infra import Connector
from Distribuicao.Standalone.modules.Context import Context

class MarcaPonto(Context):

    def __init__(self, Context) -> None:
        self.id_User = Context.id_User
        self.nome_User = Context.nome_User
        self.usuario_User = Context.usuario_User
        self.tipo_User = Context.tipo_User
        self.uid_User = Context.uid_User

    def marcarPonto(self) -> tuple:
        con = Connector.conectar()

        if con:
            marcaPontoUser = f"""INSERT INTO `app_point` (`ID`, `ID_USER`, `DATETIME_POINT`, `TYPE_USER`, `RFID_USER_POINT`) VALUES (null, '{self.id_User}', now(), '{self.tipo_User}', '{self.uid_User} - Ponto Client');"""
            cursor = con.cursor()
            cursor.execute(marcaPontoUser)
            con.commit()
            print(f" - Ponto inserido no banco para o usuário: {self.nome_User}")
            return f"Ponto inserido no banco para o usuário: {self.nome_User}"
        else:
            return "Falha ao Marcar o ponto no banco de dados"

