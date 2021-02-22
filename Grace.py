# Task 1 - parse a greeting and a name
# using ctrl + f6, the command line option is set to : --name-Grace

import argparse

from argparse import ArgumentParser


def hello(name):
    print( f'Hello {name}')

if __name__ == '__main__':
    args_to_parse = ArgumentParser()
    args_to_parse.add_argument('--name', required=True, help='The name to greet')
    args = args_to_parse.parse_args()

    hello(args.name)

 # When the code is run, it gives Hello Grace  
   

# Task 2 - parse both firstname and lastname
# Using ctrl + f6, the command line option is  set to : --firstname=Favour  --lastname=Samuel

def hello(firstname, lastname):
    print( f'Hello {firstname} {lastname}')


if __name__ == '__main__':
    args_to_parse = ArgumentParser()
    args_to_parse.add_argument('--firstname', required=True, help='The name to greet')
    args_to_parse.add_argument('--lastname', required=True, help='The name to greet')
    args = args_to_parse.parse_args()

    hello(args.firstname,  args.lastname)

# When run, it gives Hello Favour Samuel.

# Task 3 - Capitalise only the first letters of "hello amazing grace"
# Using ctrl + f6, the command line options was set to as --firstname=amazing --lastname=grace
# The purpose of help : "The first name to consume", "The last name to consume"

def hello(firstname, lastname):
    print( f'Hello {firstname.title()} {lastname.title()}')


if __name__ == '__main__':
    args_to_parse = ArgumentParser()
    args_to_parse.add_argument('--firstname', required=True, help='The name to greet')
    args_to_parse.add_argument('--lastname', required=True, help='The name to greet')
    args = args_to_parse.parse_args()

    hello(args.firstname,  args.lastname)

# When run, it will give Hello Amazing Grace
         