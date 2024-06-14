RSV = float(input("Please input a Richter scale value:"))
print("Richter scale value:", RSV)

Energy = 10**(1.5*RSV+4.8)
print("Equivalence in Joules:", Energy)

TNT = Energy/4.184*(10**9)
print("Equivalence in tons of TNT:", TNT)

NL = Energy/2930200
print("Equivalence in the number of nutritious lunches:", NL)