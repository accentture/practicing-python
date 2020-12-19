#importing model
import notes.note as model


#actions for notes
class Actions :
    def create(self, user) :
        print(f"\nOk user[1], let's create a new note...")

        title = input("What is title of your note?: ")
        description = input("Insert description of your note?: ")

        #instancing Note
        note = model.Note(user[0], title, description)
        resultSaved = note.save()

        #cheking rowcount
        if resultSaved[0] >= 1 :
            print(f"Your note {note.title} has been saved perfectly.")
        else :
            print(f"\n Sorry {user[1]}. Your note haven't been saved.")



