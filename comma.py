def numComma(a):
    tmp = len(a:=str(a)) % 3 + 1
    a = ''.join([f',{c}' if not(tmp := tmp - 1)%3 else c for c in a])
    a = (a[1:] if a[0] == ',' else a)
    return a
print(numComma(123456789))
