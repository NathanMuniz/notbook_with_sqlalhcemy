from time import sleep
from view.interface import Interface as itfc


interface = itfc()

while True:
    interface.menu_principal()
    rep = int(input("Type the desired option: "))
    if rep == 1:
        filter = str(input("[all, id, tag]filter: ")).upper()

        # Search all
        if filter == "ALL":
            notes = "empety"
            session = interface.creat_session()
            notes = interface.all_notes(session)
            for note in notes:
                print(30 * "-")
                print(note.memo)
                sleep(1)
            sleep(5)
            session.close()

        # Search ID
        elif filter == "ID":
            session = interface.creat_session()
            id = int(input("Digite o id desejado"))
            note = interface.search_id(id, session)
            print(note)
            sleep(3)
            session.close()

        # Search Tags
        elif filter == "TAG":
            pass
        else:
            print("[ERRO] Filter not fund")

    # New Note
    elif rep == 2:
        title = str(input("Title: "))
        memo = str(input("Memo: "))
        tags = str(input("Tags: "))
        notes = interface.create_note(tt=title, mm=memo, tg=tags)

    # Modify Note
    elif rep == 3:
        id = int(input("Type the Id that you want modify memo"))
        memo = str(input("New memo: "))
        print(30 * "-")
        interface.modify_memo(id, memo)
        sleep(4)

    # Modify Tags
    elif rep == 4:
        id = int(input("Type the ID that you want modify tags"))
        tags = str(input("New Tags: "))
        print(30 * "-")
        interface.modify_tags(id, tags)
        sleep(4)

    # Exit
    elif rep == 0:
        break
    else:
        print("Option not fond Please Type a corret option")
