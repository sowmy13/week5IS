#function to take onr argument and make it double

    
def doublethisnow(first):
    double = 2*first
    print(double)
    
    
doublethisnow(5)

def doublethisgive(first):
    return 2*first
    
    
doubled = doublethisgive(5)
print(doubled)


def multiplythese(a,b):
    print(a)
    print(b)
    print("first number is {0} and second is {1} ".format(a,b))
    print(str(a) +  " " + str(b))
    return a*b
    
print(multiplythese(3,5))


def isFrance(word):
    if word =="France":
        print("Oui")
        return True
    else:
        print("non monsieur")
        return False
    
print("the result is : " + str(isFrance("Germany")))  



def xtimes2y(a,b):
    return a * doublethisgive(b)


print("The result is {0} ".format(xtimes2y(2,2)))


def doubleto100(num):
    doubledvalue = num
    n = 0
    while  doubledvalue <= 100:
        n += 1
        doubledvalue = doubledvalue*2
    return n    

print("Number of times doubled : {0} ".format(doubleto100(80)))


def doubleto100recursion(num):
    #check if i am in base case
    if num > 100:
        return 0
        
    return doubleto100recursion(2*num) + 1


print("Number of recursions : {0} ".format(doubleto100recursion(10)))




















