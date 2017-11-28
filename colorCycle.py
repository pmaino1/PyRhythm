def cycle(r,g,b, flag):
    if(flag):
        if(r>150):
            r-=1
        elif(g>150):
            g-=1
        elif(b>150):
            b-=1
        else:
            flag = False
    else:
        if(r<255):
            r+=1
        elif(g<255):
            g+=1
        elif(b<255):
            b+=1
        else:
            flag = True
    return (r,g,b,flag)
