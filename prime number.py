num = int(input("Enter value:"))
# input() is used to take values from the users
# input()  always takes string,
# that's why we use int()
# so string wll be converted into integer value

if num > 0:
    if num == 1:
        print("Not Prime.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime.")
                break
        else:
            print("Prime!!!")
else:
    print("Unidentified.")
