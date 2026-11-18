#wap to check whether the given number is prime or not 

num = int(input("Enter a number: "))

i = 2

if num <= 1:
    print("Not Prime")
else:
    while i < num:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")