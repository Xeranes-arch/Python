import numpy as np
from numpy import loadtxt
import json

file = open('C:\\Users\\Xeonis7\\Documents\\Python\\saved\\a.json')
halloffame = json.load(file)
print(halloffame)

spot = int(input("Choose spot to place your marker:"))
if type(spot) != int:
    if spot.upper() == "Q":
        raise EOFError("Quit.")
    raise ValueError("Not an Integer.")
print(int("q"))
