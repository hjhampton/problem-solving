import time

# unoptimized recursive fibonacci 1, 1, 2, 3, 5, 8, 13
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# optimized fib using hashmap(dictionary) (key:value) (n:sum)
# this function is optimized by storing each value in a dictionary once it is calculated. Rather than recalculating
# values every single pass, it simply looks up the value in the dictionary if it exists, and calculates it if it does not.
# O(2^n) -> O(n)
def optimizedFib(n, hashmap):
    
    if n in hashmap:
        return hashmap[n]

    if n <= 2:
        return 1

    fibValues[n] = optimizedFib(n-1, hashmap) + optimizedFib(n-2, hashmap)
    return fibValues[n]








start = time.time()
fibValues = dict()
print(optimizedFib(999, fibValues))
end = time.time()
print("Time: " + str(end-start))









