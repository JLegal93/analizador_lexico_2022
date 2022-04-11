currentIndex = 0
currentToken = ''
fileText = open("fuente.txt", "r").read()
output_file = open("output_file.txt", "w")
def getToken():
    global currentToken
    global currentIndex
    if(currentIndex <= len(fileText)):
        currentToken = fileText[currentIndex]
        currentIndex += 1
        print(currentIndex)
    else:
        return 'eof'


def tmatch (spectedToken):
    if(not spectedToken == currentToken):
        print("error en la posicion:" + currentIndex + ",simbolo no esperado")
    getToken()

def stringrp():
    if (currentToken == '"'):
        tmatch('"')
        output_file.write('STRING')
    else:
        getToken()
        stringrp()

def stringr():

    if (currentToken == '"'):
        tmatch('"')
        stringr()
    else:
        stringrp()

def obj():
        tmatch('{')
        output_file.write('L_LLAVE')
        #stringr()

def json():
    getToken()
    if(currentToken == '{'):
        obj()

    output_file.close()


def main():
    json()

if __name__ == '__main__':
    main()