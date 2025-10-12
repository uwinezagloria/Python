"""
Write a function that takes a string as input and returns a dictionary with the frequency of 
each character in the string."""
def char_frequency(s):
    freq = {} 
    for char in s:
        if char in freq:
            freq[char] += 1  
        else:
            freq[char] = 1   
    return freq

string_input =input("enter string : ")
result = char_frequency(string_input)
print(result)
