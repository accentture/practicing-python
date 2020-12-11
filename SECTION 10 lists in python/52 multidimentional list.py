

contacts = [
    [
        'junior', 
        234234
    ],
    [
        'yessy', 
        1234
    ],

    [
        'frank', 
        543
    ],
    [
        'esteban', 
        54645
    ],

]


for contac in contacts :
    for element in contac :
        if type(element) == int :
            print(element)