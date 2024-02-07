#1
def gramTOounces(grams):
    ounces = ounces = 28.3495231 * grams
    return ounces
g = int(input())
o = gramTOounces(g)
print(f"{g} grams = {o:.2f} ounces.")
    
#2
def Fahrenheit(F):
    C = (5/9) * (F - 32)
    return C
    
F = float(input())
C = Fahrenheit(F)
print(f"{F} F = {C:.2f} C.")

#3
def solve(numheads, numlegs):
    for numC in range(numheads + 1):
        numR = numheads - numC
        if (2 * numC + 4 * numR) == numlegs:
            return numC, numR
    return "No solution found"

numheads = int(input())
numlegs = int(input())
result = solve(numheads, numlegs)
print("Number of chickens and rabbits:", result)

#4
from random import randint
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

n=int(input())
numbers=[randint(1,100) for i in range(n)]
print(numbers)
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#5
from itertools import permutations

def Print_Permutations(string):
    perm = permutations(string)
    for p in perm:
        print(''.join(p))


user_input = input()
print()
Print_Permutations(user_input)

#6
def reverse_sentence(s):
    words = s.split()
    rS = ' '.join(reversed(words))
    return rS

# Example usage:
n = input("Enter a sentence: ")
rS = reverse_sentence(n)
print("Reversed sentence:", rS)

#7 No answer

#8
def spy_game(nums):
    count_0 = 0
    count_7 = 0
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 7 and count_0 >= 2:
            count_7 += 1
    return count_0 >= 2 and count_7 >= 1

print(spy_game([1,2,4,0,0,7,5]))    
print(spy_game([1,0,2,4,0,5,7]))    
print(spy_game([1,7,2,0,4,5,0]))    

#9
def sphere_volume(r):
    pi = 3.14
    v = (4/3) * pi * r ** 3
    return v

r = float(input())
v = sphere_volume(r)
print("Volume:", v)

#10
from random import randint
def unique_elements(l):
    uniqL = []
    for item in l:
        if item not in uniqL:
            uniqL.append(item)
    return uniqL


n=int(input())
l=[randint(1,100) for i in range(n)]
result = unique_elements(l)
print(l)
print("List with unique elements:", result)

#11
def is_palindrome(word):
    word = word.lower()  
    revWord = word[::-1]  
    return word == revWord 

s = input("Enter: ")
result = is_palindrome(s)
if result:
    print("YES")
else:
    print("NO")

#12 No answer
    
#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    n = input()
    print(f"Well, {n}, I am thinking of a number between 1 and 20.")

    sNum = random.randint(1, 20)
    gN= 0

    while True:
        print("Take a guess.")
        guess = int(input())
        gN += 1

        if guess < sNum:
            print("Your guess is too low.")
        elif guess > sNum:
            print("Your guess is too high.")
        else:
            print(f"Good job, {n}! You guessed my number in {gN} guesses!")
            break

guess_the_number()





