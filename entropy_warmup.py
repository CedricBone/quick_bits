# Compression is Intelligence Part 1 - https://youtu.be/l6DKRf-fAAM?si=uqdJDqvemZV0fD8w

# Problem - There is a rover on the moon collecting surfce data. 
# It can move in 4 directions, up, down, left, right. The moving instructions are sent from earth.
# The instructions are not uniformly distributed. We are also assuming that the instructions are independent of each other.
# If the instructions are sent as a stream of bits, What is the most efficient way to encode the instructions?

import math
import random


# Probabilities
p_UP = 2/4
p_DOWN = 1/4
p_LEFT = 1/8
p_RIGHT = 1/8

# Encodings
encoding1 = {
    'UP': '0',
    'DOWN': '10',
    'LEFT': '110',
    'RIGHT': '111'
}

encoding2 = {
    'UP': '00',
    'DOWN': '01',
    'LEFT': '10',
    'RIGHT': '11'
}

encoding3 = {
    'UP': '000',
    'DOWN': '001',
    'LEFT': '010',
    'RIGHT': '011'
}

encodings = [encoding1, encoding2, encoding3]

counter = 1
for encoding in encodings:
    avg_bits = (len(encoding['UP']) * p_UP) + (len(encoding['DOWN']) * p_DOWN) + (len(encoding['LEFT']) * p_LEFT) + (len(encoding['RIGHT']) * p_RIGHT) 
    print(f"The average number of bits per instruction for encoding {counter} is: {avg_bits}")
    counter += 1

# Information
# Adding up the fractional information content of each 
information = math.log2(1 / (p_UP * p_DOWN * p_LEFT * p_RIGHT) )
print(f"The information content of the instructions is: {information} bits")
print(f"The information of UP is: {math.log2(1/p_UP)} bits")
print(f"The information of DOWN is: {math.log2(1/p_DOWN)} bits")
print(f"The information of LEFT is: {math.log2(1/p_LEFT)} bits")
print(f"The information of RIGHT is: {math.log2(1/p_RIGHT)} bits")

