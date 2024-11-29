import math

a = int(input('1st side'))
b = int (input('2nd side'))
c = int(input('3rd side'))

s = float((a+b+c)/2)

area =math.sqrt((s)*(s-a)*(s-b)*(s-c))
print(f"area of traingle is {area}")

angA = math.asin(2*area/(b*c))
angB = math.asin(2*area/(c*a))
angC = math.asin(2*area/(a*b))

angle_a = math.degrees(angA)
angle_b = math.degrees(angB)
angle_c = math.degrees(angC)

print(f"angA={angle_a},angb={angle_b},angc={angle_c}")
