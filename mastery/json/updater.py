obj = {
    "client": "python-mastery tool",
}

obj.update({"version":"0.1.0"})

print(obj)

print(obj.get('client'))


if obj.get('client') is not None:
    print("client is not None")
    assert obj.get('client') is None