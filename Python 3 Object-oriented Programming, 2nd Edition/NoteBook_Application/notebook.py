import datetime
#Store the next available id for all the new note
last_id = 0

class Notebook:


    def __init__(self):
        '''Initializes a notebook with a empty list.'''

        self.notes = []


    def new_note(self, memo, tags=''):
        '''Creates a new note'''
        self.notes.append(Note(memo, tags))


    def _find_note(self, note_id):
        
        for note in self.notes:
            if note.id == note_id:
                return note
    

    def modify_memo(self,note_id,memo):
        '''Modifies a memo for a given note_id'''

        self._find_note(note_id).memo = memo


    def modify_tag(self, note_id, tag):
        '''Modifies a tag for a given note_id'''

        self._find_note(note_id).tag = tag

    
    def search(self,filter):
        return [note for note in self.notes if
                note.match(filter)]


class Note:
    '''Represents a note in a notebook. Match against a string in searches and 
    store tags for each note'''


    def __init__(self, memo, tag=''):
        '''Initializes a note with memo and some space-centred tags.
        Automatically set the note's creation date and a unique id'''

        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    
    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''

        return filter in self.memo or filter in self.tag