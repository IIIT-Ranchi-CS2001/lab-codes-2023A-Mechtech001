import math

point1 = (1, 2, 3)
point2 = (4, 6, 8)

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

print(f"Euclidean distance between {point1} and {point2} is {distance:.2f}")