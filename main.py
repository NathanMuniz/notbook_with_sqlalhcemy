from time import sleep
from view.interface import Interface as itfc

#fabrica = fabrica_de_conexao.FabricaConexao()
#session = fabrica.create_sesson()
#nt = notebook.Notebook()


#title = str(input(("Title: ")))
#memo = str(input(("Memo: ")))
#tags = str(input(("Tags: ")))
#new_note = note.Note(title=title, memo=memo, tags=tags)

#notes = nt.notes(session)
#for n in notes:
#    print(f"{n}")

#session.commit()
#session.close()
interface = itfc()

while True:
    interface.menu_principal()
    rep = int(input("Type the desired option: "))
    if rep == 1:
        print(interface.show_notes())
        sleep(5)
    elif rep == 2:
        pass
    elif rep == 0:
        pass
    else:
        print("Option not fond Please Type a corret option")
