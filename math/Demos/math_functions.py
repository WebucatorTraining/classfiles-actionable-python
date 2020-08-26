print(abs(-5)) # 5
print(abs(5)) # 5
print(abs(-5.5)) # 5.5
print(abs(5.5)) # 5.5

print(float(5)) # object is integer. Returns 5.0
print(float("5")) # object is string. Returns 5.0
print(float(5.4)) # object is already float. Returns 5.4
print(float("5.4")) # object is string. Returns 5.4
print(float("-5.99")) # object is string. Returns -5.99
print(float(-5.99)) # object is float. Returns -5.99

print(int(5)) # object is integer already. Returns 5
print(int("5")) # object is string. Returns 5
print(int(5.4)) # object is float. Returns 5
print(int(5.9)) # object is float. Returns 5
print(int(-5.9)) # object is float. Returns -5

# object is string. Returns ValueError: invalid literal: 
# print(int("5.4")) 

print(round(3.14)) # 3
print(round(-3.14)) # -3
print(round(3.14, 1)) # 3.1
print(round(3.95, 1)) # 4.0
print(round(1111, 0)) # 1111
print(round(1111, -2)) # 1100