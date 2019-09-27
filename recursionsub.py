#subtract 20 to 10

def subtractTo10(num):
    #check if i am in base case
    if num ==10:
        return 0
        
    return subtractTo10(num-1) + 1


print("Number of recursions : {0} ".format(subtractTo10(20)))


# return (subtractTo10(19) +1 = 1
# return (subtractTo10(18) +1 = 1
# return (subtractTo10(17) +1 = 1
# return (subtractTo10(16) +1 = 1
# return (subtractTo10(15) +1 = 1
# return (subtractTo10(14) +1 = 1
# return (subtractTo10(13) +1 = 1
# return (subtractTo10(12) +1 = 1
# return (subtractTo10(11) +1 = 1

# return (subtractTo10(10) +1 = 0
