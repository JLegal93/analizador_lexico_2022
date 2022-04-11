currentIndex = 0
currentToken = ''
fileText = open("fuente.txt", "r").read()
output_file = open("output_file.txt", "w")
def getToken():
    global currentToken
    global currentIndex
    if(currentIndex < len(fileText)-1):
        currentToken = fileText[currentIndex]
        currentIndex += 1
        return True
    else:
        currentToken = ''
        return False


def tmatch (spectedToken):
    if(not spectedToken == currentToken):
        print("error en la posicion:" + currentIndex + ",simbolo no esperado")
    getToken()

def stringrp():
    if (currentToken == '"'):
        tmatch('"')
        output_file.write('STRING ')
    else:
        getToken()
        stringrp()

def stringr():

    if (currentToken == '"'):
        tmatch('"')
        stringr()
    else:
        stringrp()

def list():
    if (currentToken == '['):
        tmatch('[')
        output_file.write('L_CORCHETE \n\t')
        attr()
    elif (currentToken == ','):
        attr()
    elif (currentToken == ']'):
        tmatch(']')
        output_file.write('L_CORCHETE\n\t')
        attr()

def truer():
    if (currentToken == 't'):
        trueString = currentToken
        for number in range(3):
            getToken()
            trueString += currentToken
        if (trueString.lower() == 'true'):
            output_file.write('PR_TRUE ')
            attr()

def falser():
    if (currentToken == 'f'):
        trueString = currentToken
        for number in range(4):
            getToken()
            trueString += currentToken
        if (trueString.lower() == 'false'):
            output_file.write('PR_FALSE ')
            attr()

def numberr():
    if (currentToken.isnumeric()):
        getToken()
        numberr()
    else:
        attr()

def attr():
    if (currentToken == '"'):
        stringr()
        attr()
    elif (currentToken == ':'):
        tmatch(':')
        output_file.write('DOS_PUNTOS ')
        attr()
    elif (currentToken == '{'):
        obj()
    elif (currentToken == '['):
        list()
    elif (currentToken == ']'):
        tmatch(']')
        output_file.write('R_CORCHETE \n')
        attr()
    elif (currentToken == 't'):
        truer()
    elif (currentToken == 'f'):
        falser()
    elif (currentToken.isnumeric()):
        output_file.write('NUMBER ')
        getToken()
        numberr()
    elif (currentToken == '}'):
        obj()
    elif (currentToken == ','):
        tmatch(',')
        output_file.write('COMA \n\t')
        attr()
    elif(getToken()):
        attr()


def obj():
    if (currentToken == '{'):
        tmatch('{')
        output_file.write('L_LLAVE \n\t')
    if (currentToken == '}'):
        tmatch('}')
        output_file.write('R_LLAVE\n')
    attr()



def json():
    getToken()
    obj()
    output_file.close()


def main():
    json()

if __name__ == '__main__':
    main()