def info(name, age):
    print(f"Hi, my name is {name}. I am  {age * 365.25} days old.")

# This does what is expected
info("Alice", 23.0)

# This doesn't
# info(23.0, "Alice")

info(age=23.0, name="youngstone")