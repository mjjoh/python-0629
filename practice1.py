from math import *
ab=int(input())
bc=int(input())
ca=float(sqrt(ab*ab+bc*bc))
answer= degrees(acos(bc/ca))
print(f'{answer}°') #도전과제 1