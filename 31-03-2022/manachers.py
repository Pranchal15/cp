def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)
    #abcdab

def Manacher(string):
    string = UpdatedString(string)
    # #a#b#c#d#a#b#
    LPS = [0 for _ in range(len(string))]
    
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))
    print (string[c - r : c + r].replace("#",""))
    return r

case = input()
print(Manacher(case))