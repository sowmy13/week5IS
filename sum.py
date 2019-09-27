# sum of two numbers
import sys

#arguments live in sys.argv
#sys.argv =["sum.py", 3,5]

if len(sys.argv) != 3:
    print("Usage: python" + sys.argv[0] + " <first number><second number>")
    sys.exit()
    
first = int(sys.argv[1])
second= int(sys.argv[2])

print("{0} and {1}".format(first, second))

#result = first+second
#print(result)



def addthesetogether(a,b):
    result = a+b
    print(result)
addthesetogether(first,second)