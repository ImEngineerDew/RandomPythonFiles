#Sum law
def f(n):
    for i in range (n):
        print(i)
    
    for i in range (n):
        print(i)

#Sum law second version
def f_2(n):
    for i in range (n):
        print(i)
    
    for i in range (n*n):
        print(i)

#Product law
def pr(n):
    for i in range (n):
        for j in range (n):
            print(i,j)       

if __name__ == '__main__':
    f(3)
    print("")
    f_2(3) 
    print("")
    pr(3)      