import Variables as var
import random

number_of_letters=int(input("How many letters should the password have?: "))
number_of_symbols=int(input("How many symbols should the password have?: "))
number_of_digits=int(input("How many digits should the password have?: "))

total=number_of_letters+number_of_symbols+number_of_digits;
letters=[];symbols=[];digits=[]

for x in range(0,number_of_letters):
    y=random.randint(0,len(var.letters)-1)
    letters.append(var.letters[y])
for x in range(0, number_of_symbols):
    y = random.randint(0, len(var.symbols) - 1)
    symbols.append(var.symbols[y])
for x in range(0, number_of_digits):
    y = random.randint(0, len(var.numbers) - 1)
    digits.append(var.numbers[y])

letters.extend(symbols)
letters.extend(digits)

final_list=[]

for x in range(0,len(letters)):
    y=random.randint(0,len(letters)-1)
    final_list.append(letters[y])
    letters.pop(y)

stringa=str(final_list)
print(stringa)

