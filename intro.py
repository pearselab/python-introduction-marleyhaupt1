# 1. Write a loop that prints out the numbers 20 to 10
x = []
for i in range(20,9, -1):
    x.append(i)
print(x)

# 2. Write a list comprehension that returns the numbers from 20 to 10
x_comp = [i for i in range(20, 9, -1)]
print(x_comp)

# 3. Write a loop that prints out only the numbers from 20 to 10 that are even
even = []
for i in range(20,9,-1):
    if i%2==0:
        even.append(i)
print(even)

# 4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even
even_comp = [i for i in range(20,9,-1) if i%2==0]
print(even_comp)

# 5. Write a function that calculates whether a number is a prime number (hint: what does 2 % 3 give you?)
def prime (x):
    for i in range(x-1, 1, -1):
        p = x % i
        if p == 0:
            return False
    return True
print(prime(5))
print(prime(24))

# 6. Write a function that loads a text file, loops over the lines in it, and
    # prints out the fifth character on the fifth line of that file.
    # "Hint" (really, frankly, this is the solution):
    # with open("name_of_file") as handle:
        # for line in handle:
        ## Do something

def text_5 (my_file):
    c = 1
    with open(my_file) as file:
        for line in file:
            if c == 5:
                print(line[4])
            c = c + 1
text_5("test_text.txt")

# 7. Write a loop that prints out the numbers from 1 to 20, printing "Good: NUMBER"
    # if the number is divisible by five and "Job: NUMBER" if the number is prime
    # and nothing otherwise

for i in range(1,21,1):
    if i % 5 == 0:
        print("Good:", i)
    elif prime(i) == True:
        print("Job:", i)
    if __name__ == '__main__':
        if __name__ == '__main__':
            if i == 5:
                print("Job:", i)

# 8. A bologist is modelling population growth using a Gompertz curve, which is defined
    # as y(t) = a.e^-b.e^-c.t where y is population size, t is time, a and b are
    # parameters, and e is the exponential function. Write them a function that calculates
    # population size at any time for any values of its parameters

def gompertz(time, a, b, c):
    import math
    y = a * math.exp(-b * math.exp(-c * time))
    return y
print(gompertz(20, 3, 30, 1))

# 9. Write a function that draws boxes of a specified width and height that look like
    # this (height 3, width 5):
    #   *****
    #   *   *
    #   *****
    # Hint: What does print("*" + " " + "*"*4) give you?

def simpleBox(height, width):
    for h in range(0,height,1):
        if h == 0 or h == (height-1):
            print("*"*width)
        else:
            print("*" + " "*(width-2) + "*")

simpleBox(10,10)            # Ahhh! Yay! It totally works!!!

# 10. Implement a point class that holds x and y information for a point in space.
    # Note that I am not asking you to plot that line

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

# 11. Write a distance method that calculates the distance between two points in space.

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    if __name__ == '__main__':
        def distance(point1, point2):
           return ((point2[x] - point1[x]) ** 2 + (point2[y] - point1[y]) ** 2) ** 0.5

# 12. Implement a line class that takes two point objects and makes a line between
    # them. Note that I am not asking you to plot the line

