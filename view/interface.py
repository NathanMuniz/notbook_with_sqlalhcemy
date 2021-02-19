from database.fabricas import fabrica_de_conexao
from Notebook import notebook
from Note import note
class Interface():

    def menu_principal(self):
        print(30 * "-=")
        print("Option [1] - Show Notes")
        print("Option [2] - Create a new Note")
        print("Option [0] - Exit")
        print(30 * "-=")

    def show_notes(self):
        all_notes = "Empty"
        fabrica = fabrica_de_conexao.FabricaConexao()
        session = fabrica.create_sesson()
        try:
            nt = notebook.Notebook()
            all_notes = nt.notes(session)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            return all_notes

