from database.fabricas import fabrica_de_conexao
from database.dominios.db import Note
fabrica = fabrica_de_conexao.FabricaConexao()


class NotebookQurey():

    def new_note(self, note, session):
        session.add(note)

    def notes(self, session):
        notes = session.query(Note).all()
        return notes