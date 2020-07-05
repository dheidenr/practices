import math


def combination(n, k):
    return math.factorial(n) / (math.factorial(k) * (math.factorial(n - k)))


print(math.factorial(10) * math.factorial(5))
print(math.factorial(15))
print(15*14*13*12*11)
print((math.factorial(450)/math.factorial(447))*
      (math.factorial(450)/math.factorial(448))*
      (math.factorial(450)/math.factorial(449)))
print(90518400 * 450 * 202050)
print((math.factorial(450)/(math.factorial(3) * math.factorial(450 - 3))) / 2)

print(combination(450, 3) + combination(450, 1) * combination(450, 2))
