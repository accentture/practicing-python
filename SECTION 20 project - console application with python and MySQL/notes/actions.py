#importing model
import notes.note as model

#actions for notes
class Actions :
    def create(self, user) :
        print(f"\nOk {user[1]}, let's create a new note...")
        print("\nmy model", model)
        try :
            title = input("What is title of your note?: ")
            description = input("Insert description of your note?: ")

            #instancing Note
            _note = model.Note(user[0], title, description)
            resultSaved = _note.save()
            print('resutSaved', resultSaved)  
            
            #cheking rowcount
            if resultSaved[0] >= 1 :
                print(f"Your note {_note.title} has been saved perfectly.")
            else :
                print(f"\n Sorry {user[1]}. Your note haven't been saved.")

        except Exception as e :
            print(type(e))
            print(type(e).__name__)
            print(f"here is the error ")

    def display(self, user) :
        print(f"\nGood {user[0]}!! Here are your notes: ")

        note = model.Note(user[0])
        notes = note.toList() #saving all notes

        for note in notes :
            print('\n*********************************************')
            print('title: ', note[2])
            print('description: ', note[3])

    def remove(self, user) :
        print(f"\nOkey {user[1]}!! Let's remove your note")

        title = input("Enter title of note that you want to remove: ")

        note = model.Note(user[0], title)
        eliminated = note.remove()

        if eliminated[0] >= 1 :
            print(f"\n Your note {note.title} has been eliminated")
        else :
            print("Your note could not be eliminated, try later...")


