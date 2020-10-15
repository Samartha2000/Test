def odd(n):
  if n % 2 == 1:
    return True
  return False
  
for i in range(10):
  if odd(i):
    print(str(i) + " is ODD")
  else:
    print(str(i) + " is EVEN")
