from database.query import notebook_query
from database.dominios.db import Note


class Notebook():
    def __inti__(self):
        self.notes = self.notes()


    def new_note(self, note, session):
        query_notebook = notebook_query.NotebookQurey()
        new_note = Note(title=note.title, memo=note.memo, tags=note.tags, creation_date=note.creation_date)
        query_notebook.new_note(new_note, session)


    def notes(self, session):
        query_notebook = notebook_query.NotebookQurey()
        notes = query_notebook.notes(session)
        return notes