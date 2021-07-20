Prompt1 = "Enter first number"
Prompt2 = "Enter second number"

print(Prompt1)
s = input()
print(Prompt2)
s2 = input()

a1 = float(s) / float(s2)
a2 = float(s) % float(s2)

print('{0} divided by {1} is {2} with a remainder of {3}'.
format(s,s2,a1,a2))
