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
