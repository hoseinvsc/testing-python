
# for i in range(11,0,-1):
#     print("*"*i)

def myprinter(range1):

    if isinstance(range1,str) == True:
        print("import numbers in type of int!")
    
    elif isinstance(range1,float) == True:
        print("import numbers in type of int , not float!")
     
    else :
        for i in range(range1,0,-1):
            print("*"*i,)


myprinter(range1=10.2)