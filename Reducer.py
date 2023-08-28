def reducer(words):
    result = ",".join(words)
    return result

words = ["apple", "banana", "cherry"]
print(reducer(words))