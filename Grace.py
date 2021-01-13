#A task was given before to just include a name and then parse it of which I did 
#The second assignment was to parse both firstname and lastname together which was
#done and Favour Samuel was gotten.
#The third task isto Capitalise the first letters of "hello amazing grace"

#Code for the second task.
import argparse

from argparse import ArgumentParser


def hello(firstname, Lastname):
    print( f'Hello {firstname} {Lastname}')


if __name__ == '__main__':
    args_to_parse = ArgumentParser()
    args_to_parse.add_argument('--firstname', required=True, help='The name to greet')
    args_to_parse.add_argument('--Lastname', required=True, help='The name to greet')
    args = args_to_parse.parse_args()

    hello(args.firstname,  args.Lastname)
    
#Code for the third task
def hello(firstname, Lastname):
    print( f'Hello {firstname} {Lastname}')


if __name__ == '__main__':
    args_to_parse = ArgumentParser()
    args_to_parse.add_argument('--firstname', required=True, help='The name to greet')
    args_to_parse.add_argument('--Lastname', required=True, help='The name to greet')
    args = args_to_parse.parse_args()

    hello(args.firstname.title(),  args.Lastname.title())


 
    
         