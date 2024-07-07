reverses = "python is fun"
words = reverses.split()
Empty = ""
index = len(words) - 1
while index >= 0:
    Empty += words[index] + " " 
    index -= 1
print(Empty.strip()) # Output become fun is python   

