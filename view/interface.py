from database.fabricas import fabrica_de_conexao
from Notebook import notebook
from Note.note import Note

class Interface():

    def menu_principal(self):
        print(30 * "-=")
        print("Option [1] - Search")
        print("Option [2] - Create a new Note")
        print("Option [3] - Modify memo")
        print("Option [4] - Modify tags")
        print("Option [0] - Exit")
        print(30 * "-=")


    def all_notes(self, session):
        try:
            nt = notebook.Notebook()
            all_notes = nt.notes(session)
            return all_notes
        except:
            session.rollback()
            raise



    def create_note(self, tt, mm, tg):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()

        try:
            nb = notebook.Notebook()
            note = Note(title=tt, memo=mm, tags=tg)
            new_note = nb.new_note(note, session)
            session.commit()
            return "New note created"
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def search_id(self, id, session):

        try:
            nb = notebook.Notebook()
            note = nb.search_id(id, session)
            note_desejada = note
            session.commit()
            return note_desejada
        except:
            session.rollback()


    def creat_session(self):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()
        return session

    def modify_memo(self, note_id, memo):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()
        try:
            nb = notebook.Notebook()
            nb.modify_memo(note_id, memo, session)
            session.commit()
            return print(self.search_id(note_id, session))
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def modify_tags(self, note_id, tags):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()
        try:
            nb = notebook.Notebook()
            nb.modify_tags(note_id, tags, session)
            session.commit()
            return print(self.search_id(note_id, session))
        except:
            session.rollback()
            raise
        finally:
            session.close()






