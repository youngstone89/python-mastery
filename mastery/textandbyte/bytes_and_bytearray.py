s = 'cafe'

cafeBytes = bytes(s, encoding='utf-8')

print(cafeBytes)
print(len(cafeBytes))

print(s.encode('utf-8') == cafeBytes)


print(cafeBytes[0])

# slice starts from zero when left is empty
# 1 after colon means slice should stop at index 1 (exclusive)
print(cafeBytes[:1]) 


cafe_bytes_arr = bytearray(s,encoding='utf-8')
print(s)

print(cafe_bytes_arr[-1:])


tab = '\t'
print(tab.encode('utf-8'))

