"""
Written by sanzelda

This program will output random 16Character discord nitro links into a file called links.txt
"""
import random

try:
    open('alreadyGenerated.txt', 'x')
except:
    pass



characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

already_generated = []

for line in open('alreadyGenerated.txt'):
    if (len(line) == 17):
        already_generated.append(line[:-1])
    elif(len(line) == 37):
        already_generated.append(line[21:-1])
    else:
        continue





print('If you have already used or generated links, paste them to alreadyGenerated.txt for better results.')
number_of_gens = int(input('Enter how many links you would like generated: '))

with open("links.txt", 'w') as linkFile:
    for i in range(number_of_gens):
        code = ''

        
        while True:
            for i in range(16):
                code += characters[random.randrange(len(characters))]

            if (code in already_generated):
                code = ''
                continue
            else:
                break
        



        link = 'https://discord.gift/' + code
        print(link)
        linkFile.write(link + '\n')

        already_generated.append(link)
        open('alreadyGenerated.txt', 'a').write(link + '\n')

    print('\nThe links were output to links.txt')
    input('')

        
        
            