class Prime_Numbers:
    def __init__(self,n):
        self.n = n
    def is_prime(self, n):
        if (n>1):
            for i in range(2,n):
                if (n%i==0):
                    return False
            return True
        return False
    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x),self.n))
    
arr = input()
n = list(map(int, arr.split()))
prime_filter = Prime_Numbers(n)
print(prime_filter.filter_primes())