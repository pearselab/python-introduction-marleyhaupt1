# 1. Write a loop that prints out the numbers 20 to 10
x = []
for i in range(20,9, -1):
    x.append(i)
#print(x)

# 2. Write a list comprehension that returns the numbers from 20 to 10
x_comp = [i for i in range(20, 9, -1)]
#print(x_comp)

# 3. Write a loop that prints out only the numbers from 20 to 10 that are even
even = []
for i in range(20,9,-1):
    if i%2==0:
        even.append(i)
#print(even)

# 4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even
even_comp = [i for i in range(20,9,-1) if i%2==0]
#print(even_comp)

# 5. Write a function that calculates whether a number is a prime number (hint: what does 2 % 3 give you?)
def prime (x):
    for i in range(x-1, 2, -1):
        p = x % i
        if p == 0:
            return False
    return True
#print(prime(5))
#print(prime(24))

# 6. Write a function that loads a text file, loops over the lines in it, and
    # prints out the fifth character on the fifth line of that file.
    # "Hint" (really, frankly, this is the solution):
    # with open("name_of_file") as handle:
        # for line in handle:
        ## Do something

