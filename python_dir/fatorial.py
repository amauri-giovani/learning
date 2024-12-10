def fatorial(n):
   return n * fatorial(n - 1) if n != 0 else 1

print(fatorial(5))