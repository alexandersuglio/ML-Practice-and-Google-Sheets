# recursion vs iterations 
# Rule of Thumb - Recursion vs For Loops or While Loops, but Recursion will still use If-Elses

def factorialI(n):
  ans = 1
  while n > 0:
    ans *= n
    n -= 1

  return ans

print(factorialI(5))

def factorialR(n):

  if n == 1:
    return n

  else: 
    return n * factorialR(n - 1)

print(factorialR(5))

def fib(n):

  if n == 0:
    return 0

  if n == 1:
    return 1

  else:
    return fib(n-1) + fib(n-2)

print(fib(3))
# 0 1 1 2 3 5 8

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  twoBefore, oneBefore = 0, 1

  for i in range(2, n + 1):

    twoBefore, oneBefore = oneBefore, twoBefore + oneBefore
    print(i,"th: ", twoBefore, oneBefore)

  return oneBefore

print(fib(6))

# 0 1 2 3 4 5
#     |      6
#.    0 1
