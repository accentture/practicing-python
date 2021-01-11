import pathlib, sys, datetime, hashlib
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')
import models.programming as programming

class ActionNotes : 
    def __init__(self, useModel) :
        pass
        self.models = {}
        self.useModel = useModel
        self.createCollectionOfModels()

    def createCollectionOfModels(self) :
        self.models['programming'] = programming.ProgrammingModel
        print("my models => ", self.models)

    def askForActions(self, user_id) :
        print(f"========== What action do you do with {self.useModel} notes? ==========")
        print("""
            - create 
            - remove
            - update
            - exit
        """)

        action = input("Choose action: ")

        if action == 'create':
            self.create(user_id)
            self.askForActions(user_id) #creating a infinity loop
        elif action == 'remove': 
            self.remove(user_id)
            self.askForActions(user_id)
        elif action == 'update' :
            self.update(user_id)
            self.askForActions(user_id)
        elif action == 'exit':
            print('Ok, We will see you soon.')
        else :
            print("It option doens't exists.")

    def create(self, user_id) :
        print(f"========== Creating note ==========")
        topic = input("Write topic for your note: ")
        description = input("Write a description for your note: ")

        # checkig if inputs are full
        if topic and description :

            #I STAYED HERE
            modelToUse = self.models[self.useModel]
            note = modelToUse(user_id, topic, description)
            note.create()

    def remove(self, user_id) :
        print(f"========== Removing note ==========")
        topic = input("Topic of your note to remove: ")
        keyword = input("What is the keyword of your note: ")

        if len(topic) > 1 and len(keyword) > 1:
            note = model.ProgrammingNote(user_id, topic, "", keyword)
            removed = note.remove()

            if removed :
                print("Your note has been removed.")

    def update(self, user_id) : 
        print(f"========== Updating note ==========")
        topic = input("Topic of your note to update:")
        keyword = input("What is the keyword of your note: ")

        if len(topic) > 1 and len(keyword) > 1:
            note = model.ProgrammingNote(user_id, topic, "", keyword)

            updated = note.update()

            if updated :
                print("Your note has been updated sucessfully.")
            