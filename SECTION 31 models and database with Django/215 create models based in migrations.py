""" 
    --to make migrations :        
    
                        py manage.py make migrations    

            --it command take mi models and check if a migration was created previously, and based in it create a file of migrations, where in this file will be executed all changes in my database
            --after to execute command a file named "0001_initial.py" will be created




            -after to execute this command, the model isn't in database
            --now is moment to create sql that will be executed in SGBD, for that I need to execute the next command:

                        py manage.py sqlmigrate miapp 0001
                                                # 0001 : indicating number of migration created previously
            --after to execute the previous command tables based in models will be display sql code in console




            --now to execute sql code in database use the next script:
                        py manage.py migrate
            --after to execute the previuosly script appear the next : Applying miapp.0001_initial... OK



        **visual manager for sqlite  :  db browser for sqlite
            --other equivalent program is  "navicat for sqlite"

 """