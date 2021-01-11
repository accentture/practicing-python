""" 
    ways to install modules in python : 
        https://es.stackoverflow.com/questions/348101/error-al-instalar-paquetes-pip-no-se-reconoce-como-un-comando-interno-o-exte

    -m = modules

    --the modules are functionalities done that we can reutilize
    --a module is seems to a library 
    -- there are many modules in python : https://docs.python.org/3/py-modindex.html
    -- python has its modules, also we can get modules in internet and we can make our own modules
 """

#this method will be used in other module
def HelloWord(name) :
    return f" Hola {name}"

def operation(num1, num2) :
    return num1 + num2