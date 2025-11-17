# if else statement
num = int(input("enter any number:"))

if num%2==0:
    print("number entered is even")
else:
    print("number entered is odd")


# if elif else statement
marks=int(input("enter marks: "))
if marks >= 80  and marks <=100 :
    print(f" Congartulations you have attained grade A of {marks} excellent")
elif marks < 80 and marks >=70 :
    print(f"you have attained grade b of {marks} excellent")
elif marks < 70 and marks >=60:
    print(f"you have attained grade c of {marks} can do better")
elif marks < 60 and marks >= 50:
    print(f"you have attained grade  D of {marks} can do way better")
elif marks < 50 and marks >= 0:
    print(f"you have a mark of {marks} this is a failure")
else:
    print(f"The mark {marks} is an invalid input")