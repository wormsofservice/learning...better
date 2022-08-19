number = 10

data = input("Let's check and see if your number is smaller or larger than "+ str(number)+ ": ")

try:
    data = int(data)
except:
    print("Sum ting wong")


if data > number:
    print('Larger')

elif data < number:
    print('Smaller')

else:
    print("They're equal!")
