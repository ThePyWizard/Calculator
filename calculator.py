def calc(x,y,z):
    op=input('enter operator : ')
    while z=='y':
        if op=='+':
            print(x+y)
        elif op=='-':
            print(x-y)
        elif  op=='*':
            print(x*y)
        elif op=='/':
            print(x/y)
        elif op=='//':
            print(x//y)
        elif op!=True:
            print('Invalid operator !!! change ur operator')
    else:
        z=input('y or no :')
        if z=='y':
            calc(a,b,c)
a=int(input("enter no : "))
b=int(input("enter no : "))
c='y'
calc(a,b,c)
