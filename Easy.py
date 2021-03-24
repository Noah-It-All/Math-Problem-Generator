def maineasyrun():
    from random import randint
    from time import sleep
    def typecheck():
        global thetype
        thetype = input("Type S for subtraction problems, Type a for addition problems and Type M for multiplication problems!: ")
    typecheck()
    def randomnumbergenadd():
        sleep(1)
        blah = randint(1, 10)
        blooh = randint(1, 15)
        combinestring = str(blah) + " + " + str(blooh)
        personanswer = input("Whats the answer to " + combinestring + " ?: ")
        realanswer = int(blah) + int(blooh)
        if personanswer == "end":
            print("Now ending!")
            print("3")
            sleep(1)
            print(2)
            sleep(1)
            print(1)
            print("Goodbye!")
            quit()
        try:
            if int(realanswer) == int(personanswer):
                istrue = "True"
            else:
                istrue = "False"
        except ValueError:
            print("Please give the answer next time!")
            randomnumbergenadd()
        
        if istrue == "True":
            print("Good Job! Time for the next problem!")
            randomnumbergenadd()
        if istrue == "False":
            print("Sorry that was wrong, Time for the next problem")

    def randomnumbergensub():
        sleep(1)
        blah = randint(1, 15)
        blooh = randint(1, 10)
        combinestring = str(blah) + " - " + str(blooh)
        personanswer = input("Whats the answer to " + combinestring + " ?: ")
        realanswer = int(blah) - int(blooh)
        if personanswer == "end":
            print("Now ending!")
            print("3")
            sleep(1)
            print(2)
            sleep(1)
            print(1)
            print("Goodbye!")
            quit()
        try:
            if int(realanswer) == int(personanswer):
                istrue = "True"
            else:
                istrue = "False"
        except ValueError:
            print("Please give the answer next time!")
            randomnumbergensub()
        
        if istrue == "True":
            print("Good Job! Time for the next problem!")
            randomnumbergensub()
        if istrue == "False":
            print("Sorry that was wrong, Time for the next problem")
            randomnumbergensub()

    def randomnumbergenmult():
        sleep(1)
        blah = randint(1, 5)
        blooh = randint(1, 5)
        combinestring = str(blah) + " x " + str(blooh)
        personanswer = input("Whats the answer to " + combinestring + " ?: ")
        realanswer = int(blah)*int(blooh)
        if personanswer == "end":
            print("Now ending!")
            print("3")
            sleep(1)
            print(2)
            sleep(1)
            print(1)
            print("Goodbye!")
            quit()
        try:
            if int(realanswer) == int(personanswer):
                istrue = "True"
            else:
                istrue = "False"
        except ValueError:
            print("Please give the answer next time!")
            randomnumbergenmult()
        
        if istrue == "True":
            print("Good Job! Time for the next problem!")
            randomnumbergenmult()
        if istrue == "False":
            print("Sorry that was wrong, Time for the next problem")
    while str(thetype) == "M" or str(thetype) == "m":
        print("Selecting Multiplication")
        randomnumbergenmult()



    while str(thetype) == "S" or str(thetype) == "s":
        print("Selecting Subtraction")
        randomnumbergensub()



    while str(thetype) == "A" or str(thetype) == "a":
        print("Selecting Addition")
        randomnumbergenadd()



    
