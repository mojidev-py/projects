num = []
nonlistnum = 0
input1 = input("Enter a number here.")
total = []
final = 0

for char in input1:
    inted = int(char)
    num.append(inted)

nonlistnum = int(input1)

for number in num:
    check = number ** len(num)
    total.append(check)

for num in total:
    final += num

if final == nonlistnum:
    print("The number you provided is an armstrong number.")
else:
    print("The number you provided is not an armstrong number.")
    

