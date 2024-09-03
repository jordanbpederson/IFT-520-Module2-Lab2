## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

#  File name: data_formats.py

# Converting human communication into binary format



# Test to binary conversion

text = "Hello"

binary_text = ' '.join(format(ord(char), '08b') for char in text)

print(f"Text: {text}")



# Image simulation (convert a pixel value to binary)

pixel_value = 255 # Max value for an 8-bit pixel

binary_pixel = format(pixel_value, '08b')

print(f"Pixel value: {pixel_value}")

print(f"Binary pixel: {binary_pixel}")



# Sound simulation (convert an audio sample to binary)

audio_sample = 32767 # Max value for a 16-bit audio sample

binary_audio = format(audio_sample, '016b')

print(f"Audio sample: {audio_sample}")

print(f"Binary audio: {binary_audio}")