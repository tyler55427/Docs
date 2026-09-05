s=input()
sign=False
temp=''
res=[]
for i in s:
    if i=='-':
        if temp:
            res.append(temp)
            temp=''
        sign=True
        continue
    if i.isdigit():
        if sign:
            temp+='-'
            sign=False
        temp+=i
    elif i=='.':
        if temp:
            ss=False
            for j in temp:
                if j=='.':
                    ss=True
            if ss:
                res.append(temp)
                temp=''
            else:
                temp+=i
    else:
        if temp:
            res.append(temp)
            temp=''
    sign=False
if temp:
    res.append(temp)
for i in res:
    if i[-1]=='.':
        print(int(i[:-1]))
        continue
    try:
        print(int(i))
    except:
        try:
            print(float(i))
        except:
            continue