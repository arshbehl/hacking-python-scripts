from argparse import ArgumentParser
import secrets
import random
import string


# Setting up Argument Parser
parser = ArgumentParser(
    prog = 'Password Generator.',
    description = 'Generates any number of passwords with this tool'
)


# Adding arguments to this tool
parser.add_argument("-n", "--numbers", default=0, help="Number of digits in the PW", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Number of lowercase chars in the PW", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Number of uppercase chars in the PW", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Number of special chars in the PW", type=int)


# Add total pw length arguments
parser.add_argument("-t", "--total-length", type=int,
                    help="The total password length. If passed, it will ignore -n, -l, -u and -s, " \
                    "and generate completely random passwords with the specified length")


# The amount is a number so we check it to be of type int
parser.add_argument("-a", "--amount", default=1 ,type=int)
parser.add_argument("-o", "--output-file")


# Parsing the command line arguments
args = parser.parse_args()


# Lists of passwords
passwords = []


# Looping through the amount of passwords
for _ in range(args.amount):
    if args.total_length:
        # generates random passwords with the length of total_length based on all available characters
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                for _ in range(args.total_length)
            ]
        ))
    
    else:
        password = []
        
        # If / how many numbers the password should contain 
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))

        # If / how many uppercase characters the password should contain 
        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        # If / how many lowercase characters the password should contain 
        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # If / how many special characters the password should contain 
        for _ in range(args.special_chars):
            password.append(secrets.choice(string.punctuation))

        
        # Shuffle the list with all possible letters, numbers and symbols
        random.shuffle(password)


        # Get the letters of the string up to the length agrument and then join them.
        password = ''.join(password)


        # Append this password to the overall list of password.
        passwords.append(password)


# Store the password to a .txt file.
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))


print('\n'.join(passwords))


# -n -> integer numbers length
# -l -> lowercase characters length
# -u -> uppercase characters length
# -s -> special characters length
# -a -> Total number of passwords generated
# --output_file -> make a .txt file containing the passwords generated


# For genearting and saving file, write the following command -> 
# python password_generator.py -n 6 -u 4 -l 4 -s 2 -a 500

# For genearting and saving file, write the following command -> 
# python password_generator.py -n 6 -u 4 -l 4 -s 2 -a 500 --output-file keys.txt