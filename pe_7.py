#!/usr/bin/env python3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_10001st_prime():
    count = 0
    n = 1
    while True:
        if is_prime(n):
            count += 1
        if count == 10001:
            return n
        n += 1

result = find_10001st_prime()
print(result)

#result by perplexity labs lol
