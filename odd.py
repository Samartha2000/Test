def odd(n):
  if n % 2 == 1:
    return True
  return False
  
for i in range(10):
  if odd(i):
    print("ODD")
  else:
    print("EVEN")
