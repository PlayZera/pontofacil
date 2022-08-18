class Context:

    def __init__(self):
        self.user = "Nome do usuário"
        self.tipoUser = "Tipo do usuário"

    def set_User(self, user):
        self.user = user

    def set_TypeUser(self, typeUser):                 
        self.tipoUser = typeUser

    def get_User(self):
        return self.user

    def get_TypeUser(self):
        return self.tipoUser
    
    userRet = property(set_User, get_User)
    typeUserRet = property(set_TypeUser, get_TypeUser)