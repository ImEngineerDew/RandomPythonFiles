import time


def numberFactorial(n):
    answer = 1

    while n>1:
        answer*=n
        n-=1
    
    return answer

#El factorial recursivo en su tiempo de ejecución es mucho más rápido
def recursiveFactorial(n):
    if n == 1:
        return 1
    
    return n*numberFactorial(n-1)


if __name__ == '__main__':
    n= 100000

    start = time.time()
    numberFactorial(n)
    final = time.time()
    print(final-start)

    start = time.time()
    recursiveFactorial(n)
    final = time.time()
    print(final-start)