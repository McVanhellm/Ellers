i1=99
iMin=10
polindrom=0
while i1>iMin:
    i2=i1
    while i2>iMin:
        pro=i1*i2
        if str(pro)==str(pro)[::-1] and pro>polindrom:
            polindrom=pro
            iMin=i2
            break
        i2-=1
    i1-=1
    if i1*i1<polindrom:
        break
print(polindrom)