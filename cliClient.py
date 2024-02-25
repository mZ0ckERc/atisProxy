import requests

host = "localhost"
port = 8000

baseurl = f"http://{host}:{port}"


# DEFINE THE FUNCTION HERE

def getCustomParams():
    return requests.get(f"{baseurl}/getAppended").text

def setCustomParams():
    pass

def getLastQueryParams():
    return requests.get(f"{baseurl}/getLastQueryParams").text

# DEFINE THE LOOKUP TABLE FOR COMMANDS-FUNCTIONS HERE

lookupTab = {
    "GA": getCustomParams,

    "GP": getLastQueryParams,
}


def onboarding():
    global host, port, baseurl
    if not host:
        print("Please specify the host the Server runs on")
        print("Press enter for localhost.")
        hostInput = input("> ")
        if hostInput != "":
            host = hostInput
        else:
            host = "localhost"
    if not port:
        print("Please enter the port.")
        print("Press enter for port 8000.")
        while True:
            portInput = input("> ")
            if portInput != "":
                try: 
                    port = int(portInput)
                    break
                except:
                    print("The specified port was not a number! Please enter the port again!")
            else:
                port = 8000
                break
    baseurl = f"http://{host}:{port}"

    

def printCMDs():
    print("What would you like to do?")
    print("[GA] Get the customized parameters")
    print("[SA] Set customized parameters")
    print("[GP] Get the last query's parameters")
    print("[GC] Get the parameters that would currently be sent on")
    print("")

def functionChooser(cmd: str):
    print(lookupTab.get(cmd)())

if __name__ == '__main__':
    print("Welcome to the CLI Client.")
    onboarding()
    printCMDs()
    functionChooser(input("> "))
    
    