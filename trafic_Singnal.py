print("Welcom To Traffic Signal System")

print(" A. Red")
print("B. Yellow")
print("C. Green")
print("D. exist")

choice=str(input("Enter your choice (A-D):"))

if choice=="A":
    print("\n Red:Stop The Vehicle")
elif choice=="B":
    print("\n Yellow: Please Go Slow") 
elif choice=="C":
    print("\n Green: You Can Go!")   
elif choice=="D":
    print("\n Thank You For using traffic signal program")
else:
    print("\n invalid choice,please try again")