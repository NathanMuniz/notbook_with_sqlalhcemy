from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FabricaConexao():

    def conecatar(self):
        engine = create_engine("mysql://root:root@localhost:3306/notebook")
        return engine

    def create_sesson(self):
        conexao = self.conecatar()

        Session = sessionmaker()
        Session.configure(bind=conexao)
        Session.expire_on_commit=False
        session = Session()

        return session

