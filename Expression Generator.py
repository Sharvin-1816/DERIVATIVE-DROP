import random
def generating_Function():
    global eqn1
    eqn = "ax^3+bx^2+cx+d"
    dic = {"a":random.randint(0,3),"b":random.randint(0,3),"c":random.randint(0,3),"d":random.randint(0,3)}
    for x in list(dic.keys())[0:3]:
        if dic[x]==1:
            dic.update({x:""})
    for x in dic.keys():
        for y in eqn:
            if y==x:
                eqn = eqn.replace(y,str(dic[x]))
    l = eqn.split("+")
    l1=[]
    for index,x in enumerate(l):
        if "0" in x:
            continue
        l1.append(x)
    eqn = "+".join(l1)
    l2=[]
    for x in eqn:
        if x=="^":
            l2.append("")
        else:
            l2.append(x)    
    eqn1="".join(l2)
    return eqn1
