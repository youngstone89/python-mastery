import chardet


def test_file_encoding():
      # Create a sample file with known content
    content = "Hello, 世界!"
    with open("test_file.txt", "w", encoding="utf-8") as f:
        f.write(content)
    
    with open("test_file.txt", "rb") as f:
        raw_data = f.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]
    
    # Assert that the detected encoding is correct
    assert detected_encoding.lower() == "utf-8"
    
    # Read the file content and compare
    with open("test_file.txt", "r", encoding="utf-8") as f:
        read_content = f.read()
    
    assert read_content == content
    


def test_encode_and_decode():
    s = '카페'
    print(len(s))
    b = s.encode('utf-8')
    print(b)
    print(len(b))
    print(b.decode('utf-8'))
    assert s == b.decode('utf-8')