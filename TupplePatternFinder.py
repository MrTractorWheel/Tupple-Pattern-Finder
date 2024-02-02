def tupple_to_string(lst):
    string = [''.join(i) for i in lst]
    return str(string)

def pattern_search(P,I):
    P0 = P
    P90t = list(zip(*P0[::-1]))
    P180t = list(zip(*P90t[::-1]))
    P270t = list(zip(*P180t[::-1]))
    P90= eval(tupple_to_string(P90t))
    P180= eval(tupple_to_string(P180t))
    P270= eval(tupple_to_string(P270t))
    I_search = ''.join(I)
    if P0[0] in I_search:
        indexes = [t for t, p in enumerate(I_search) if p == P0[0][0]]
        lenght = len(indexes)
        for a in indexes:
            x= a // int(len(I[0]))
            y = a % int(len(I[0]))
            P_count = explorer(x,y,P0,I)
            if P_count == 1:
                return (x,y,0)
    if P90[0] in I_search:
        indexes = [t for t, p in enumerate(I_search) if p == P90[0][0]]
        lenght = len(indexes)
        for a in indexes:
            x= a // int(len(I[0]))
            y = a % int(len(I[0]))
            P_count = explorer(x,y,P90,I)
            if P_count == 1:
                return (x,y,90)
    if P180[0] in I_search:
        indexes = [t for t, p in enumerate(I_search) if p == P180[0][0]]
        lenght = len(indexes)
        for a in indexes:
            x= a // int(len(I[0]))
            y = a % int(len(I[0]))
            P_count = explorer(x,y,P180,I)
            if P_count == 1:
                return (x,y,180)
    if P270[0] in I_search:
        indexes = [t for t, p in enumerate(I_search) if p == P270[0][0]]
        lenght = len(indexes)
        for a in indexes:
            x= a // int(len(I[0]))
            y = a % int(len(I[0]))
            P_count = explorer(x,y,P270,I)
            if P_count == 1:
                return (x,y,270)
    return bool(False)



def explorer(x,y,Pa,I):
    I_search = ''.join(I) 
    for i in range (len(Pa)):
            for j in range (len(Pa[0])):
                count = 1
                if x+i > len(I) or y+j > len(I[0]):
                    return 0
                else :
                    if Pa[i][j] == I[x+i][y+j]:
                        count = 1
                    else:
                        return 0
    if count == 1:
        return 1
    





