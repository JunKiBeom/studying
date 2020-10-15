print("Normal Function")
def calc_square(digit):
    return digit * digit

def calc_power_3(digit):
    return digit * digit * digit

def calc_quad(digit):
    return digit * digit * digit * digit

print (calc_square(2))
print (calc_power_3(2))
print (calc_quad(2))

# normal func vs closure_func

print("\nClosure Function")
def calc_power(n):
    def power(digit):
        return digit ** n
    return power

power2 = calc_power(2)  #save n=2
power3 = calc_power(3)  #save n=3
power4 = calc_power(4)  #save n-4

print (power2(2))  # digit=2, **2
print (power3(2))  # digit=2, **3
print (power4(2))  # digit=2, **4

# N ** 1~M
print()
list_data = list()
# N, M=[int(i) for i in input().split()]
N, M=map(int,input().split())
for num in range(1, M+1):
    list_data.append(calc_power(num))

for func in list_data:
    print((func(N)),end=" ")