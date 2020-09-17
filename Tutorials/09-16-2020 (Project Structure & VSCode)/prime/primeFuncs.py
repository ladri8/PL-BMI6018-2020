def isPrime(N):
    if N == 1 or N == 0:
        return False
    else:
        for i in range(2,N//2):
            if N % i == 0:
                return False
        return True