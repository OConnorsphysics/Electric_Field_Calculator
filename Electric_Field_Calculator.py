# program written by Liam O'Connor to determine electric field from series of point charges
import numpy as np
import math

E = 0 #electric field
k = 8.99 * (10**9) #coulomb constant Nm^2/C^2
Etotal = 0  #total magnitude of electric field
multiCharges = "Yes"
while multiCharges == "Yes" or "yes" or "y" or "Y":
    q = float(input("What is the charge of q (Coulombs)?")) #charge of particle
    x = float(input("what is the x position of the charge q?"))
    y = float(input("what is the y position of the charge q?"))
    z = float(input("what is the z position of the charge q?"))
    x0 = float(input("what is the x position where the field is to be determined?"))
    y0 = float(input("what is the y position where the field is to be determined?"))
    z0 = float(input("what is the z position where the field is to be determined?"))
    rVector = [x0 - x, y0 - y, z0 - z]
    EPosition = [x0, y0, z0]
    r = np.array(rVector)
    print(f"The vector from the charge to the point of measurement is {r}")
    rMag = math.sqrt(x**2+y**2+z**2) #distance where we want to determine E in relation to point p
    print(rMag)
    E1 = k*q/(rMag**2)
    print(f"The Electric field at {EPosition} from a single charge q is {E1} N/C, in the direction of {r}.")
    Etotal = Etotal + E1
    multiCharges = input("Do you want to add another charge to the system? (Y/N)") #todo shouldn't be able to change measurement location after adding a point

print(f"The Electric field at {EPosition} from the given charges is {Etotal} N/C, in the direction of {r}.") #todo calculate the correct r value for multi point
