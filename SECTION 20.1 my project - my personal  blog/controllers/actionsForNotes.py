import pathlib, sys, datetime, hashlib
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')
import models.note as model

class ActionNotes : 
    def __init__(self, kindOfNote) :
        pass
        self.kindOfNote = kindOfNote
    
    def askForActions(self, user_id) :
        print(f"========== What action do you do with {self.kindOfNote} notes? ==========")
        print("""
            - create 
            - remove
            - update
        """)

        action = input("Choose action: ")

        if action == 'create':
            self.create(user_id)
        elif action == 'remove': 
            self.remove(user_id)
        elif action == 'update' :
            self.update(user_id)
        else :
            print("This action doesn't exists.")

    def create(self, user_id) :
        print(f"========== Creating note ==========")
        topic = input("Write topic for your note: ")
        description = input("Write a description for your note: ")

        # checkig if inputs are full
        if topic and description :
            note = model.ProgrammingNote(user_id, topic, description)
            note.create()

    def remove(self, user_id) :
        print(f"========== Removing note ==========")
        topic = input("Topic of your note to remove: ")
        keyword = input("What is the keyword of your note: ")

        if len(topic) > 1 and len(keyword) > 1:
            note = model.ProgrammingNote(user_id, topic, "", keyword)
            note.remove()

    def update(self, user_id) : 
        print(f"========== Updating note ==========")
        topic = input("Topic of your note to update:")
        keyword = input("What is the keyword of your note: ")

        if len(topic) > 1 and len(keyword) > 1:
            note = model.ProgrammingNote(user_id, topic, "", keyword)
            