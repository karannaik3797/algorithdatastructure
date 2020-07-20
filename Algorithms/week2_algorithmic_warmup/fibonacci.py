# Uses python3
def calc_fib(n):
  res = []
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    res.append(0)
    res.append(1)
    for i in range(2,n+1):
        res.append(res[i-1]+res[i-2])
    return res[n]
n = int(input())
print(calc_fib(n))
