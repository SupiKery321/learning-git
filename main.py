print("Zadanie 1")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 3 for number in numbers]
for i in squares: 
   if i % 2 != 0:
    print(i)

print("Zadanie 2.1")
a = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
a = a[1:4] + a[5:10] + a[-2:]
print(a)

print("Zadanie 2.2")
b = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
b = b[:1] + b[4:5] + b[10:12]
print(b)


print("Twój stary pijany")
