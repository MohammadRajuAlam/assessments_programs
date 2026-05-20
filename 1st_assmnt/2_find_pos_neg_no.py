# 2) wap to find positive & Negative number but 0 is not pos & Neg no. take i/p from user through keyboard.
def pos_neg(num):
    if num > 0:
        print(f"{num} is a Positive number")
    elif num == 0:
        print(f"{num} is neither positive nor negative")
    else:
        print(f"{num} is a Negative number")
num=int(input("Enter a number:"))
pos_neg(num)