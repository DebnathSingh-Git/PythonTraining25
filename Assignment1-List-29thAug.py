# Create an empty list to store scores.
scorelist = []

# Append the scores: 85, 90, 78, 92, 88
scorelist.extend([85, 90, 78, 92, 88])
print("Scrore List: ", scorelist)

# Insert the score 80 at index 5
scorelist.insert(5, 80)
print("Scrore List after insert: ", scorelist)

# Remove the score 92 from the list
scorelist.remove(92)
print("Scrore List after remove: ", scorelist)

# Sort the scores in ascending order
scorelist.sort()
print("Scrore List after sorting: ", scorelist)

# Reverse the list
scorelist.reverse()
print("Scrore List after reversing: ", scorelist)

# Find and print the maximum and minimum score
print("Scrore List Min: ", min(scorelist), "  Max: ", max(scorelist))

# Check if 90 is in the list
print("Scrore List - if 90 is in the list: ", 90 in scorelist)

# Print the total number of scores
print("Scrore List total number ", len(scorelist))

# Slice and print the first three scores
print("Scrore List after slicing first three scores: ", scorelist[:3])

# find the last element from the list
print("Scrore List last element: ", scorelist[-1])

# replace the score with new score on the index 2
scorelist[2] = 1000
print("Scrore List new score on the index 2: ", scorelist)

# create a new copied list also
copiedscorelist = scorelist.copy()
print("Copied Scrore List: ", copiedscorelist)



