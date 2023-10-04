import random  # this is a module
import string  # this is a module


def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


'''If you wright a def inside the class then it is called a method
   If you wright a def outside the class then it is called a function'''
