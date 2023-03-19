""" 
    --REST is an arquitecture
    --requisites:
        0 an API is charged throught an URL
        1 client and server separed
        2 interaction with database must be exclusive of server
        3 to display data (interfaz) must be separed of server
        4 it is knowed as front end and backend

        5 we must make queries without state(it means that it doesn't wait a response of other application after to execute the query)
        6 uniform interfaz(interfaz = JSON file): every application access to my REST service in the same way
        7 systems by layer: 
        8 REST is an arquitecure based in HTTP protocol, therefore use the next HTTP methods:
            GET
            POST
            PUT - update
            DELETE

        9 state code of REST service
            related with 200; means query success
            related with 300; information is cached
            related with 400; service was not found
            realted with 500; it is an error exclusive of server

 """