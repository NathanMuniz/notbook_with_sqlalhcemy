from database.fabricas import fabrica_de_conexao
from Notebook import notebook
from Note import note

fabrica = fabrica_de_conexao.FabricaConexao()
session = fabrica.create_sesson()
notebook = notebook.Notebook()

title = str(input(("Title: ")))
memo = str(input(("Memo: ")))
tags = str(input(("Tags: ")))
new_note = note.Note(title=title, memo=memo, tags=tags)

notebook.new_note(new_note, session)

session.commit()
session.close()