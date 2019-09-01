__version__ = "1.0"

"""
Generates Vietlott ticket number
Author: Anh Hong
File Name: main.py

Vietlott 6/55

Play rule: You have to choose 6 different numbers to make a combination. Each number is between 1 to 55.

Problem: You have 1 in 28,989,675 chance of winning the Vietlott Power 6/55. How to improve the chance of winning this lottery?

Solution: Add rules in number combination generation in order to exclude rare combinations.
    1. It should generate 6 random numbers from 1-55
    2. It should generate numbers from Low (1-28) and High (29-55) with this ratios: 3:3  4:2  2:4
    3. It should generate Odd and Even numbers with the same ratio as above
    4. It should not generate 6 numbers from all of 5 groups
    5. The sum of the 6 numbers should be from 104 - 239
    6. The generated combination should not equal to any previous winning number (not working on this version)
Groups
    1 --  1-11
    2 -- 12-22
    3 -- 23-33
    4 -- 34-44
    5 -- 45-55
"""
import random

# Initialize groups
GROUP1_ODD = range(1, 12, 2)
GROUP2_ODD = range(13, 23, 2)
GROUP3_ODD = range(23, 34, 2)
GROUP4_ODD = range(35, 45, 2)
GROUP5_ODD = range(45, 56, 2)
GROUP1_EVEN = range(2, 12, 2)
GROUP2_EVEN = range(12, 23, 2)
GROUP3_EVEN = range(24, 34, 2)
GROUP4_EVEN = range(34, 45, 2)
GROUP5_EVEN = range(46, 56, 2)

GROUP1 = [GROUP1_ODD, GROUP1_EVEN]
GROUP2 = [GROUP2_ODD, GROUP2_EVEN]
GROUP3 = [GROUP3_ODD, GROUP3_EVEN]
GROUP4 = [GROUP4_ODD, GROUP4_EVEN]
GROUP5 = [GROUP5_ODD, GROUP5_EVEN]

groups = [GROUP1, GROUP2, GROUP3, GROUP4, GROUP5]

def vietlott655():
    
    # Initialize variables
    odd = random.randint(2, 4)
    high_max = random.randint(2, 4)
    low_max = 6 - high_max
    generated = []
    high = 0
    low = 0

    random.shuffle(groups)  # Shuffle the groups

    # The total sum of the generated list should be 104 - 239
    while sum(generated) < 104 or sum(generated) > 239:

        # Generate 6 numbers
        for i in range(6):

            # Checks if we need to generate an odd or an even number
            if i <= odd - 1:
                odd_or_even = 0
            else:
                odd_or_even = 1

            # Get a random group from the first four groups
            current_group = groups[random.randint(0, 3)]

            # Get either an odd or even number from the chosen group
            num = random.choice(current_group[odd_or_even])

            # Checks if num is already generated or if it is a High/Low
            # number and the max number of High/Low number is already
            # achieved
            while (num in generated or (high >= high_max and num >= 29) or
                    (low >= low_max and num < 29)):
                current_group = groups[random.randint(0, 3)]
                num = random.choice(current_group[odd_or_even])

            # Checks whether the generated number is part of the High or
            # Low numbers
            if num >= 29:
                high += 1
            else:
                low += 1

            generated.append(num)  # Append the num

    generated.sort()  # Sort the list
    return str(generated)

def vietlott645():
    aset = set()
    while (len(aset) < 6):
        temp = random.randint(1, 45)
        if temp not in aset:
            aset.add(temp)
    #return str(sorted(aset))
    return "to be available soon"

def vietlott3D():
    return "to be available soon"

def vietlott4D():
    return "to be available soon"

def vietlott4DMax():
    return "to be available soon"
