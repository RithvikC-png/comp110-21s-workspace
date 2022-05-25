



def GCD(val1: int, val2: int) -> int:
    
    while(val2):
        val1, val2 = val2, val1 % val2
    
    return val1
    start


def LCM(val1: int, val2: int) -> int:
    if val1 > val2:
        greater = val1
    else:
        greater = val2
    
    while(True):
        if((greater % val1 == 0) and (greater % val2 == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm
    start

in1 = int(input("What is your first number? "))
in2 = int(input("What is your second number? "))

print ("Your GCD is: ",GCD(in1, in2))

print ("Your LCM is: ",LCM(in1, in2))

        