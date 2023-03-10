#Calculator
#Select mode
while True:
    type = input("Please enter 'a' for addition, 's' for subtraction, 'm' for multiplication, or 'd'for division: ")
    type = type.lower()
    if type.startswith('a') or type.startswith('s') or type.startswith('m') or type.startswith('d'):
        break
    else:
        print("Error please choose an input from the following")

#int1
while True:
    try:
        int1 = int(input("Please enter a number: "))
        break
    except:
        print("error")

#int2
while True:
    try:
        int2 = int(input("Please enter another number: "))
        break
    except:
        print("error")

#Addition
if type.startswith('a'):
    print(f"{int1} + {int2} = ",end="")
    print(int(int1) + int(int2))

#Subtraction
elif type.startswith('s'):
    print(f"{int1} - {int2} = ",end="")
    print(int(int1) - int(int2))

#Multiplication
elif type.startswith('m'):
    print(f"{int1} * {int2} = ",end="")
    print(int(int1) * int(int2))

#Division
elif type.startswith('d'):
    print(f"{int1} / {int2} = ",end="")
    print(int(int1) / int(int2))
else:
    print('Error')

while True:
    input("Please hit enter to close program when ready.")
    break