byte_array = bytearray('ABC', 'utf-8')
mv = memoryview(byte_array)
mv[1] = 90  # ASCII for 'Z'
print(byte_array)  # Output: bytearray(b'AZC')
