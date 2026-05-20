# wap to find even & odd number. take i/p from user through keyboard.
def even_odd(num):
    if num%2 ==0:
        print(f"{num} is even no")
    else:
        print(f"{num} is odd no")
num=int(input("Enter a number"))
even_odd(num)