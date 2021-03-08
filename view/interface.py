from database.fabricas import fabrica_de_conexao
from Notebook import notebook
from Note.note import Note
class Interface():

    def menu_principal(self):
        print(30 * "-=")
        print("Option [1] - Show Notes")
        print("Option [2] - Create a new Note")
        print("Option [0] - Exit")
        print(30 * "-=")

    def show_notes(self):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()
        all_notes = "Empty"
        try:
            nt = notebook.Notebook()
            all_notes = nt.notes(session)
            return all_notes
        except:
            session.rollback()
            raise
        finally:
            session.close()

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

    def search_id(self, id):
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()

        try:
            nb = notebook.Notebook()
            note = nb.search_id(id, session)
            session.commit()
            return note
        except:
            session.rollback()
            raise
        finally:
            session.close()







