#Importing Modules
import random

#lift1
a = random.randrange(1, 11)
print("Floor No: ", a, "Lift 1")

#Lift2
b = random.randrange(1, 11)
print("Floor No: ", b, "Lift 2")


def main():
    #Checky Checky Check Check
    if b > a:
        print("Lift 1 Incoming!")
    elif a > b:
        print("Lift 2 Incoming!")
    elif b == a:
        print("Any Of the Lift Can Come?")
    elif a == b:
        print("Any Of the Lift Can Come?")
    else:
        print("ERR 404")


if __name__ == "__main__":
    main()
    
