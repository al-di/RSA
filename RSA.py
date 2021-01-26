alph = {" ":"00",
        "A":"01",
        "B":"02",
        "C":"03",
        "D":"04",
        "E":"05",
        "F":"06",
        "G":"07",
        "H":"08",
        "I":"09",
        "J":"10",
        "K":"11",
        "L":"12",
        "M":"13",
        "N":"14",
        "O":"15",
        "P":"16",
        "Q":"17",
        "R":"18",
        "S":"19",
        "T":"20",
        "U":"21",
        "V":"22",
        "W":"23",
        "X":"24",
        "Y":"25",
        "Z":"26"}
chars=list(alph.keys())



def text2numbers(text, blocklength):
    """
    >>> text2numbers("HALLO WELT", 3)
    [80112, 121500, 230512, 200000]
    >>> text2numbers("HALLO WELT", 1)
    [8, 1, 12, 12, 15, 0, 23, 5, 12, 20]
    >>> text2numbers("HALLO WELT", 2)
    [801, 1212, 1500, 2305, 1220]
    >>> text2numbers("HALLO WELT", 5)
    [801121215, 23051220]
    """
    lastI=0#letztes gefundenes i
    numbersblocked=[]# Zahlen in Blöcke eingeteilt
    numbers=[]# Zahlen zu den Buchstaben
    for i in range(len(text)):# Buchstaben in Zahlen übersetzen
        numbers.append(alph[text[i]])

    if(blocklength==1):# wenn blöcklänge 1 ist dann alle zahlen in int formatieren
        for i in range(len(numbers)):
            numbersblocked.append(int(numbers[i]))
            
    else:# sonst in blöcke einteilen
        for i in range(len(numbers)):# über numbers ??itarieren??
            if((i+1)%blocklength == 0 and i != 0):# wenn durch blocklänge teilbar
                lastI=i
                j=blocklength
                block=""
                
                while(j!=0):# um blocklänge zurückgehen und ab da alles in block aneinanderhängen
                    block += numbers[i-j+1]
                    j = j-1
                    
                numbersblocked.append(int(block))# block in int konvertieren und an numbersblocked anhängen

        block=""
        if(lastI!=len(numbers)-1):
            lastI=lastI+1
            
            while(lastI<=len(numbers)-1):
                block += numbers[lastI]
                lastI+=1
                
            while(len(block)!=blocklength*2):
                block += "00"
            numbersblocked.append(int(block))
    return(numbersblocked)



def numbers2text(numbersblocked, blocklength):
    """
    >>> numbers2text(text2numbers("HALLO WELT", 3), 3)
    'HALLO WELT'
    >>> numbers2text([8, 1, 12, 12, 15, 0, 23, 5, 12, 20], 1)
    'HALLO WELT'
    >>> numbers2text([801, 1212, 1500, 2305, 1220], 2)
    'HALLO WELT'
    >>> numbers2text([801121215, 23051220], 5)
    'HALLO WELT'
    """

    
    text=""
    zero="0"
    numbers=[]
    if(blocklength == 1):
        for i in range(len(numbersblocked)):
            numbers.append(str(numbersblocked[i]))
    else:
        for i in range(len(numbersblocked)):
            numberblock=str(numbersblocked[i])
            
            while(len(numberblock)<(blocklength*2)):
                numberblock=zero+numberblock
                
            for j in range(len(numberblock)):
                if((j+1)%2 == 0 and j != 0):
                    k=2
                    number=""
                
                    while(k!=0):
                        number += numberblock[(j+1)-k]
                        k = k-1
                    numbers.append(number)
    
    for i in range(len(numbers)):
        text+=chars[int(numbers[i])]

    while(text[len(text)-1]==" "):
        text=text[0:len(text)-1]

    return text



def encryptAdd(klartext, e, m, blocklength):
    """
    >>> encryptAdd("HALLO WELT", 10, 65, 1)
    [18, 11, 22, 22, 25, 10, 33, 15, 22, 30]
    >>> encryptAdd("HALLO WELT", 12, 40, 3) # NB: m zu klein gewaehlt zum tatsaechlichen Verschluesseln!
    [4, 32, 4, 12]
    """
    klarnumbers=text2numbers(klartext, blocklength)

    return encryptnumbersAdd(klarnumbers, e, m)


def encryptnumbersAdd(klarnumbers, e, m):
    encryptednumbers=[]
    for i in range(len(klarnumbers)):
        y=(klarnumbers[i]+e)%m

        encryptednumbers.append(y)

    return encryptednumbers


# e+d = m, also d = m-e
def decryptAdd(geheimnumbers, d, m, blocklength):
    """
    >>> decryptAdd([18, 11, 22, 22, 25, 10, 33, 15, 22, 30], 55, 65, 1)
    'HALLO WELT'
    >>> decryptAdd(encryptAdd("HALLO WELT",12345,462626,3),462626-12345,462626,3)
    'HALLO WELT'
    >>> decryptAdd(encryptAdd("HALLO WELT ICH BIN  EIN TEST  ",12345,462626,3),462626-12345,462626,3)
    'HALLO WELT ICH BIN  EIN TEST'
    """
    klarnumbers=encryptnumbersAdd(geheimnumbers, d, m)
    klartext=numbers2text(klarnumbers, blocklength)
    return klartext







def encryptMul(klartext, e, m, blocklength):
    """
    >>> encryptMul("HALLO WELT", 3, 32, 1)
    [24, 3, 4, 4, 13, 0, 5, 15, 4, 28]
    """
    klarnumbers=text2numbers(klartext, blocklength)

    return encryptnumbersMul(klarnumbers, e, m)


def encryptnumbersMul(klarnumbers, e, m):
    encryptednumbers=[]
    for i in range(len(klarnumbers)):
        y=(klarnumbers[i]*e)%m

        encryptednumbers.append(y)

    return encryptednumbers


# e+d = m, also d = m-e
def decryptMul(geheimnumbers, d, m, blocklength):
    """
    >>> decryptMul(encryptMul("HALLO WELT", 3, 32, 1), 11, 32, 1)
    'HALLO WELT'
    """
    klarnumbers=encryptnumbersMul(geheimnumbers, d, m)
    klartext=numbers2text(klarnumbers, blocklength)
    return klartext




##################



def encryptPot(klartext, e, m, blocklength):
    """
    >>> encryptPot("ASTERIX", 13, 77, 1)
    [1, 61, 69, 26, 46, 58, 52]
    """
    klarnumbers=text2numbers(klartext, blocklength)

    return encryptnumbersPot(klarnumbers, e, m)


def encryptnumbersPot(klarnumbers, e, m):
    encryptednumbers=[]
    for i in range(len(klarnumbers)):
        y=(klarnumbers[i]**e)%m

        encryptednumbers.append(y)

    return encryptednumbers


def decryptPot(geheimnumbers, d, m, blocklength):
    """
    >>> decryptPot(encryptPot("HALLO WELT", 13, 77, 1), 37, 77, 1)
    'HALLO WELT'
    """
    klarnumbers=encryptnumbersPot(geheimnumbers, d, m)
    klartext=numbers2text(klarnumbers, blocklength)
    return klartext



#####################







if __name__ == "__main__":
    import doctest
    doctest.testmod()
