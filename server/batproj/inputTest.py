#charSet1 = "()'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "


def charTest(input, charSet):
    for x in input:
        if x not in charSet:
            return False
    return True


# either all the letters are upcase or the letter is precided by one of the char + space
def capitalTest1(input):
    chartestset = ['.', '?', '!']
    if not input.isupper():  # if all upcase = true
        #print("not all uppercase wow")
        if input[0].isupper() and not input[1].isupper():  # if the 1st char isn't upcase
            #print("well 1st is upcase & second ins't")
            for i in range(2, len(input)):
                if input[i].isupper():
                    #print("print this item is upcase in the middle")
                    print(input[i])
                    if input[i-1] != " " or input[i-2] not in chartestset:
                        return False
            return True
        else:
            return False
    else:
        return True


def capitalTest(input, splitChar):
    if not input.isupper():
        words = input.split(splitChar)
        for word in words:
            if word != '':  # test if the '.' is a last char
                aux = word[1:]
                if not aux.islower():
                    return False
    return True


def spaceTest(input):
    for x in range(len(input)-1):
        if input[x] == " " and input[x+1] == " ":
            return False
    return True


def ponctuationTest(input):
    pts = ['?', '.', '!']
    # print(len(input))
    for x in range(len(input)):
        if input[x] in pts:
            #print("ponctuation exists")
            if x != len(input)-1:
                #print("item isn't last")
                # item isn't last
                if x == (len(input)-2):
                    # item isn't before last => there is only 1 char after it
                    return False
                else:
                    # item got 2 char in front !
                    #print(input[x+1]+"   "+input[x+2])
                    if input[x+1] != " " and input[x+2].islower():

                        # next char isn't a space or the second next isn't uppercase
                        return False
    return True


def pauseTest(input):
    pts = [',', ';', ':']
    for x in range(len(input)):
        if input[x] in pts:
            if x != 0 and x != len(inputTxt)-1:
                if input[x+1] != " ":
                    return False
            else:
                return False
    return True


def inputTextTest(charSet, inputText):
    if charTest(inputText, charSet):
        #print("atleast charset is good")
        if capitalTest1(inputText):
            #print("well capital test is ok")
            if spaceTest(inputText):
                #print("space test kinda works")
                if ponctuationTest(inputText):
                    #print("pnctuationtest workds uwu")
                    if pauseTest(inputText):
                        return True
    return False


#inputText = "Hey."

#print(inputTextTest(charSet1, inputText))
