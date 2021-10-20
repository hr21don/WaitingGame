import random, time,os

def start_game():
    while True: #infinite loop
        os.system('cls') 
        print("Welcome to the waiting game!")
        print("\n\n")
        print("Instructions\n")
        print("You will be told to wait a number of seconds.")
        print("Wait and then press ENTER")
        print("Are you ready? Press ENTER to start...")
        input()

        waitingTime = random.randint(10,60)
        start = time.time()
        input("please wait for " + str(waitingTime) + " seconds")
        end = time.time()
        elapsed = end - start

        difference = abs(round(waitingTime - elapsed,2))

        print("You were" + str(difference) + " seconds out")

        if difference < 0.5:
            print("Well done, you have good time keeping!")

        elif difference < 1:
            print("You did okay!!")
        else:
            print("You were rubbish!!!!")

        input("Press ENTER to try again")

