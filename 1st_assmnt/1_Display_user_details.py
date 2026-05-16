# wap to Display user_details, take i/p from user/keyboard

def user_details():
    name=input("Enter your Name:")
    age=int(input("Enter your age:"))
    qualification=input("Enter your last qualification:")
    college=input("Enter your college name:")
    board=input("Enter your board name:")
    city=input("Enter your city name:")
    pincode=int(input("Enter your pincode:"))
    print("\t\t\t\tYour Details are:")
    print(f"Your Name is:{name}\nYour Age is:{age}\nQualification:{qualification}\nCollege Name:{college}\nBoard Name:{board}\nCity Name:{city}\nPincode:{pincode}")
    
user_details()
