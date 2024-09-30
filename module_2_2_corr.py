first = input('input first number: ')
second = input('input second number: ')
third = input('input third number: ')
if first == second and first == third:
    print(3)
elif first == second and first != third:
    print(2)
elif first == third and first != second:
    print(2)
elif first != third and second == third:
    print(2)
else:
    print(0)