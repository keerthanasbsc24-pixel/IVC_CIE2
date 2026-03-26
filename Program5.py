n=input("Enter a string : ")
s += 0

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")