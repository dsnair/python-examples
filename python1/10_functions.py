# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False

print(f"2 is even: {is_even(2)}")
print(f"5 is even: {is_even(5)}")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
print("Even!" if is_even(num) else "Odd")
