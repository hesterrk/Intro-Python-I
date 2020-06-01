# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    x = 99
    print(x, 'x prints 99 as in scope of func')


change_x()

print(x)
# This prints 12. What do we have to modify in change_x() to get it to print 99?
# Answer --> We have to print after we have declared x as the print statement will be in scope


# This nested function has a similar problem.


def outer():
    y = 120

    def inner():
        y = 999
        print(y, 'y is in inner scope')

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y, 'prints 120 as y = 120 is in global scope')


outer()
