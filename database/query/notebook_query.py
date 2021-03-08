from database.fabricas import fabrica_de_conexao
from database.dominios.db import Note
fabrica = fabrica_de_conexao.FabricaConexao()


class NotebookQurey():

    def new_note(self, note, session):
        session.add(note)

    def notes(self, session):
        notes = session.query(Note).all()
        return notes

    def id_search(self, note_id, session):
        notes = session.query(Note).filter(Note._id == note_id).first()
        return notes

    def modify_note_memo(self, note_id, new_memo, session):
        note = self.id_search(note_id, session)
        note.memo = new_memo
