n = 999
fact = 1
 
for i in range(1, n+1):
    fact = fact * i
 
print(f"The factorial of {n} is: ", end="")
print(fact)
print("\n\n")
orthis = 500 ** n
print(f"500 on a {n} is: ", end="")
print(orthis)

print("factorial" if fact > orthis else "orthis")
