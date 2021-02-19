from database.fabricas import fabrica_de_conexao
fabrica = fabrica_de_conexao.FabricaConexao()


class NotebookQurey():

    def new_note(self, note, session):
        session.add(note)