# ex 1
x = 52633
print(f'The factors of {x} is')
for i in range(x + 1):
    if i == 0:
        continue
    print(f"{x} % {i} ==",x % i)  

# ex 2
def print_factors(x):
    print(f'The factors of {x} is')
    for i in range(x + 1):
        if i == 0:
            continue
        print(f"{x} % {i} ==",x % i) 

print_factors(13)

# ex 3
l = [52633, 8137, 1024, 999]
print(f'The factors of {l} is')
for number in l:
    for i in range(number + 1):
        if i == 0:
            continue
        print(f"{number} % {i} ==",number % i) 