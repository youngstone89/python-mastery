from unicodedata import name

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

print(name(chr(200)))
