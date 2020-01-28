a=12
FormatDec="en décimal : {} << {} = {} "
FormatBin="en binaire : {} << {} = {} "

for i in range(3):
    print(FormatDec.format(a, i, a<<i))
    print(FormatBin.format(bin(a), i, bin(a<<i)))
    print()
    
for i in range(3):
    print(FormatDec.format(a, i, a>>i))
    print(FormatBin.format(bin(a), i, bin(a>>i)))
    print()
