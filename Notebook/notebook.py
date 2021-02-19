from database.query import notebook_query
from Note.note import Note

class Notebook():
    def __inti__(self, notes):
        self.notes = notes

    def new_note(self, note, session):
        query_notebook = notebook_query.NotebookQurey()
        new_note = Note(note.memo, note.tags)
        query_notebook.new_note(new_note)

