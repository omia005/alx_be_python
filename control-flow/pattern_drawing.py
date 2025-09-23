pattern_size = int(input("Enter the size of the pattern:"))
size = 0
while size < pattern_size:
  for i in range(0, pattern_size):
     print("*", end="")
     i += 1
  size += 1
