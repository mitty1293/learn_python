import sys, math

def main(input_value: str):
    if validate(input_value):
        print('Prime List:', sieve(int(input_value)))
        return
    print("Use an integer number (2 or more) as an argument.")
    return

def validate(data: str) -> bool:
    try:
        int_data: int = int(data)
    except ValueError:
        return False
    if int_data < 2:
        return False
    return True

def sieve(count: int) -> list:
    natural: list = [False]*2 + [True]*(count-1)
    prime: list = []
    
    i: int = 2
    while i < math.sqrt(count):
        if natural[i]:
            prime.append(i)
            for j in range(i**2, count+1, i):
                natural[j] = False
        i += 1
    for k in range(i, count+1):
        if natural[k]:
            prime.append(k)
    return prime

if __name__=='__main__':
    main(sys.argv[1])