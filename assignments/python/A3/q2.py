# WAP to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter any alphabet: ")

vowel = ['a','e','i','o','u']

if alphabet in vowel:
    print(alphabet,": is a vowel")
else:
    print(alphabet,": is a consonant") 