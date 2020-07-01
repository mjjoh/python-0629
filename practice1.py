from math import sqrt, acos, degrees
ab=int(input())
bc=int(input())
ca=float(sqrt(ab*ab+bc*bc))
answer= round(degrees(acos(bc/ca)))
print(f'{answer}°') #도전과제 1