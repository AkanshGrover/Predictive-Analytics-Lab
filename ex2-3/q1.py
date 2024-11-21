colors = ("red", "blue", "green", "yellow", "blue", "green", "blue")
print("Tuple of colors:", colors)
first_color = colors[0]
last_color = colors[-1]
print("\nFirst color:", first_color)
print("Last color:", last_color)
try:
    colors[1] = "purple"
except TypeError as e:
    print("\nError when trying to modify the tuple:", e)
blue_count = colors.count("blue")
print("\nOccurrences of 'blue':", blue_count)