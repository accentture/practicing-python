""" 
    --after to make modifications in models, it is important to execute migration  with the next command:
                py manage.py makemigrations

    --when will appear an option to 2
    --come back to execute migrations, and other file in migrations will be created: "0002"





    --to make a sql to execute specyfying number of migration :
                py manage.py sqlmigrate miapp 0002
    



    --come back to apply changes with this command :
                py manage.py migrate



    --finally changes in database is done

 """