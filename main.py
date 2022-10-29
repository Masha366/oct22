def function2(stroka):
    spisok=[]
    dlina=len(stroka)
    i=0
    s=0
    while i<dlina:
        spisok.append(stroka[dlina-(i+1)])
        if stroka[i]==spisok[i]:
            s=s+1
        i+=1
    if s==dlina:
        return True
    else:
        return False



