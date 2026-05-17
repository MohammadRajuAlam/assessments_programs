# 2) wap to find, positive or even, odd number, but 0 is not odd, even number, Take i/p from user.
def even_odd(num):
    if num > 0 and num %2 == 0:
        print(f"{num} is positive and even number")
    elif num > 0 and num %2 != 0:
        print(f"{num} is positive and odd number")
    elif num == 0:
        print(f"{num} is neither even nor odd number")
    elif num < 0 and num %2 == 0:
        print(f"{num} is negative and even number")
    elif num < 0 and num %2 != 0:
        print(f"{num} is negative and odd number")
num=int(input("Enter a number:"))
even_odd(num)