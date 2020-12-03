def welcome():
    print(f"""
Hello Sir and welcome to the Madlib Game ....
In my game you'll be asked a few questions
Answer them or suffer in my infinit loop >:)
let's go .....

**********************************************
    """)

#=======================================================

def inputs():
    name = input("Enter your name > ")
    adjective1 = input("Enter an adjective >  ")
    hobbie1 = input("Enter a hobbie >  ")
    hobbie2 = input("Enter another hobbie >  ")
    inanimate  = input("Enter any inanimate >  ")
    adjective2 = input("Enter an adjective >  ")
    return [name, adjective1 ,hobbie1, hobbie2, inanimate, adjective2]

#=======================================================

def read():
    valList = inputs()
    with open('./assets/template.txt') as f:
        contents = f.read()
    yourContent1 = contents %(valList[0], valList[1], valList[2], valList[3], valList[4], valList[0], valList[5])
    return yourContent1

#=======================================================

def write():
    yourContent2 = read()
    with open('assets/your_answer.txt', 'w') as f2:
        f2.write(yourContent2)
    print("*****************************************************  ")
    print("also you can find your answer inside your_answer.txt")
    print("*****************************************************  ")
    print(yourContent2)

#=======================================================

if __name__ == "__main__":
    welcome()
    write()
