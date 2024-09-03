## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

# File name: data compression.py

import zlib

# Orignal data (like uncompressed food in your kitchen)

data = "This is a simple example of data compression." * 10

print(f"Original Data Size: {len(data)} bytes")


# Compress the data (like compressing food to save space)

compressed_data = zlib.compress(data.encode('utf-8'))

print(f"Compressed Data Size: {len(compressed_data)} bytes")


# Decompress the data (like restoring the food to its original state)

decompressed_data = zlib.decompress(compressed_data).decode('utf_8')

print(f"Decompressed Data: {decompressed_data}")