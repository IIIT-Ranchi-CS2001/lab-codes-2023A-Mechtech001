# String Manipulation 2nd Question (Ba Ba Black Sheep)
S = "Ba Ba Black Sheep"

length_of_s = len(S)

first_occurrence_of_e = S.find('e')

total_occurrences_of_a = S.count('a')

s_modified = S.replace('B', 'T', 1)
s_modified = s_modified.replace('B', 'T', 1)

# Output
print("Length of the string: ",length_of_s)
print("First occurrence of 'e': ",first_occurrence_of_e)
print("Total number of occurrences of 'a': ",total_occurrences_of_a)
print("Modified string: ", s_modified)