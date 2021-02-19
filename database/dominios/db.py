from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text
from database.fabricas import fabrica_de_conexao

fabrica = fabrica_de_conexao.FabricaConexao()
engine = fabrica.conecatar()

Base = declarative_base()

class Note(Base):
    __tablename__ = 'note'

    _id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    creation_date = Column(Date, nullable=False)
    memo = Column(Text, nullable=False)
    tags = Column(String(100), nullable=False)

    def __repr__(self):
        return f"id: {self._id}, Title: {self.title}, Data: {self.cre}\n" \
               f"Memo: {self.memo}\n" \
               f"tags: {self.tags}"

Base.metadata.create_all(engine)