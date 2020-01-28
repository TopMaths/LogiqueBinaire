import operator as op
OP=[op.__and__, op.__or__, op.__xor__]
symb=["&", "|", "^"]
StrRes="{} {} {} = {}"
L=[True, False]
for i in range(3):
    for a in L:
        for b in L:
            print(StrRes.format(a,symb[i],b,OP[i](a,b)))
    print() 
