# Birthday Problem - In a set of n people, what is the probability that at least two people share a birthday?

import random

N = 23
Sample = 1000

def birthday_checker(N):
    Birthdays = []
    for person in range(N):
        birthday = random.randint(1, 365)
        Birthdays.append(birthday)
    
    if len(Birthdays) != len(set(Birthdays)):
        return True
    else:        
        return False

shared_birthday_count = 0
for sample in range(Sample):
    if birthday_checker(N):
        shared_birthday_count += 1

print(f"For a group of {N} people, the probability of at least two people sharing a birthday is: {shared_birthday_count/Sample}")




    
