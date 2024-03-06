"""
You computer uses a stack internally called the call stack. Let's see it in action.
Here's a simple function:
"""

def greet2(name):
    print("How are you today ?")


def bye():
    print("Okay, bye!")


def greet(name):
    print("hello " + name + "!")
    greet2(name)
    print("Getting ready to say bye!...")
    bye()


# greet("Ubaydullo")
    
# how do you think what call stack is being created to execute this recursive function
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

print(fact(5))
