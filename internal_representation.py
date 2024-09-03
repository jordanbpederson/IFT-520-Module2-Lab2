## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

# File name: internal_representation.py

# Internal representation of integers, floating-point number, and characters




# Integer represesentation

integer_value = 42

binary_integer = format(integer_value, '08b')

print(f"Integer: {integer_value}")

print(f"Binary Integer: {binary_integer}")



# Floating-point representation (limited example for simplicity)

float_value = 3.14

binary_float = ''.join(f'{ord(c):08b}' for c in format(float_value, '0.10f'))

print(f"Float: {float_value}")

print(f"Binary Float: {binary_float}")

# Character representation

char = 'A'

binary_char = format(ord(char), '08b')

print(f"Character: {char}")

print(f"Binary Character: {binary_char}")