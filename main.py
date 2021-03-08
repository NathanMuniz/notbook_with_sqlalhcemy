from time import sleep
from view.interface import Interface as itfc


interface = itfc()

while True:
    interface.menu_principal()
    rep = int(input("Type the desired option: "))
    if rep == 1:
        notes = interface.show_notes()
        for note in notes:
            print(30 * "-")
            print(note)
            sleep(1)
        sleep(5)

    elif rep == 2:
        title = str(input("Title: "))
        memo = str(input("Memo: "))
        tags = str(input("Tags: "))
        notes = interface.create_note(tt=title, mm=memo, tg=tags)

    elif rep == 3:
        id = int(input("Digite o id desejado"))
        note = interface.search_id(id)
        print(note)
    elif rep == 0:
        break
    else:
        print("Option not fond Please Type a corret option")
