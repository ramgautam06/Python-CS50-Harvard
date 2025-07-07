# while loop
i = 0 
while i < 3:
    print ("meow", end='')
    i +=1

# for loop 
for i in range(3):
    print("meow")

for _ in range(3): # does not need varaible here
    print("meow")

print("meow\n" * 3, end="")

# Ask from the user using loop 
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")