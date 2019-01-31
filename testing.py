# use for, split(), and if statement to create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'

for w in st.split(' '):
    if w.startswith('s'):
        print(w)

else:
    print('------------------------\n')    


# use range() to print out all the even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)


# use list comprehensions to create a list of all numbers between 1 and 50 that are divisible by 3
r = [ x for x in range(1, 51) if x % 3 == 0 ]
print(r)
print('------------------------\n')

# go through the list below and if the length of a word is even print "even"
sT = 'Print every word in this sentence that has an even number of letters'

res = [ wrd for wrd in sT.split(' ') if len(wrd) % 2 == 0 ]
print(res, '\n------------------------\n')

"""
for word in sT.split(' '):
    #print(len(word))
    if len(word) % 2 == 0:
        print('even')
else:
    print('------------------------')
"""

# write a program that prints the integers form 1 to 100, but for multiples of three print "Fizz"
# isntead of the nubmer, and for thee multiples of five print "Buzz"
# for numbers which are multiples of both three and five print "FizzBuzz"

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print( 'FizzBuzz' )
    elif i % 3 == 0:
        print( 'Fizz' )
    elif i % 5 == 0:
        print( 'Buzz' )
    else:
        print(i)

else:
    print('------------------------')

# use list comprehension to create a list of the first letters of every word in the string below:
s_t = 'Create a list of the first letters of every word in this string'

mylist = [ a[0] for a in s_t.split(' ') ]

print(mylist, '\n------------------------\n')


###############
# if word starts with a vowel --> add 'ay'to the end
# if word does not start with a vowel --> put first letter at the end, than add 'ay'

def pig_latin(word):
    
    first_letter = word[0]

    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('ccnp'))
pig_latin('ccnp')
print('------------------------')
