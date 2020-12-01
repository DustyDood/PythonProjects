
def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return(var1, var2)

def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError:
            print("\n\nYou did not provide a numeric value!")
        except:
            print("\n\nOops! Program will close now.")
    print("{} + {} = {}".format(var1, var2, var3))

def tryTesting():
    try:
        yourName = input("What is your name?")
        print("Nice to meet you, {}!".format(str(yourName)))
    except:
        print("Say... you didn't enter anything, did you?")
    finally:
        print("Thanks for demoing try and except!")
        

if __name__ == "__main__":
    tryTesting()



