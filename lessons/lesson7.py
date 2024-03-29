# Lesson 7 Loopoing Statements

# while loop
# executes a set of statements until it's condition is false
def basic_while(arg):
    alpha = arg
    while alpha < 4:
        print(alpha)
        # increment by 1
        alpha += 1


# basic_while(0)


# for loop
# executes a set of statements as it iterates a collection or sequence
def basic_for(arg):
    for alpha in arg:
        print(alpha)


# basic_for('I like coding.')

# Nested for loop
# You can have a loop inside a loop. The inner loop can use the variable of the outer loop. Both must have different
# declared variables.

def basic_nested():
    for hop in range (1, 11):
        for bop in range(hop):
            print(hop, end=' ')
            print()
        print()


# basic_nested()


# rang()
# This is used to return a sequence of numbers. This includs
# a start number, end number, and increment. The most you can have is 3 arguments
# single argument
def basic_single():
    for able in range(5):
        print(able)


# two arguments
def basic_double():
    for beta in range(2, 10):
        print(beta)


# basic_single()
# basic_double()
# three arugments
def basic_three():
    for charlie in range(0, 15, 2):
        print(charlie)


# basic_three()

# pass statement
# This allows a for loop to be created without a body.
for num in 'Hello':
    pass


# break statement
# this is used in conjunction with an if statement to break from a loop
def basic_break(num1):
    while num1 < 10:
        print(num1)
        if num1 == 5:
            break
        num1 += 1


basic_break(0)

# using for a loop
def basic_break_for():
    for value in 'Python':
        if value == 'h':
            break
        print(value)


# basic_break_for()


# continue statement
# This statement will stop an active iteration and begin the next one
def basic_continue():
    for value in 'Python':
        if value == 'h':
            continue
    print(value)


# else statement
# Also used in loops, this statement can be used after the loop ends
def basic_else():
    thing1 = 0
    while thing1 < 4:
        print(thing1)
        thing1 =+ 1
    else:
        print('loop ends')


basic_else()










