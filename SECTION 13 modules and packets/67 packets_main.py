""" 
    --a packet is a set of modules
    --we can import different packets with their different modules
    --this packets can be reutilizen
    --allows an cleaner code
    --to create a packet, We must create a folder (for example 67_my_packet)with a file named __inint__.py (indicating to python that this file is a packet)
    --after we can create many modules in the folder

    -when we import a packet, python creates a cache
 """

#importing my packet
#from a_67_my_packet import tests, tools
#from a_67_my_packet import tools

#it is posible to import many packets
from a_67_my_packet import tests, tools


tests.testing()
tools.completeName('jonathan', 'diaz')