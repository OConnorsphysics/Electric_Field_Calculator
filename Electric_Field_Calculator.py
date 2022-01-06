# program written by Liam O'Connor to determine electric field from series of point charges
# The space is described by cartesian coordinates and vectors are handled as numpy arrays
import numpy as np
import math

E = 0  # electric field
k = 8.99 * (10 ** 9)  # coulomb constant Nm^2/C^2
EtotalMag = 0  # total magnitude of electric field
Etotal = np.array([0, 0, 0])  # total electric field vector at point of measurement


def check_input(userInput):  # function prints and repeats the question until a float is entered
    isNumber = False
    while isNumber == False:
        try:
            val = float(input(userInput))
            isNumber = True
        except ValueError:
            print('Please enter numbers only.')
            #val = float(input(userInput))
            isNumber = False
    return val

x0 = check_input("what is the x position where the field is to be determined?")
y0 = check_input("what is the y position where the field is to be determined?")
z0 = check_input("what is the z position where the field is to be determined?")
EPosition = [x0, y0, z0]  # vector of E field measurement

multiCharges = "Yes"
while multiCharges in ('Yes', 'yes', 'Y', 'y'):
    q = check_input("What is the charge of q (Coulombs)?")  # charge of particle
    x = check_input("what is the x position of the charge q?")
    y = check_input("what is the y position of the charge q?")
    z = check_input("what is the z position of the charge q?")
    rVector = [x0 - x, y0 - y, z0 - z]  # vector from measurement point to point charge
    r = np.array(rVector)  # make vector list into numpy array
    print(f"The vector from the charge to the point of measurement is {r}")
    rMag = math.sqrt((x0 - x) ** 2 + (y0 - y) ** 2 + (z0 - z) ** 2)  # distance where we want to determine E in relation to point p
    print(rMag)
    E1Mag = k * q / (rMag ** 2) #Determine electric field from charge
    E1x = E1Mag * (r[0]/rMag)   #determine x component of E field
    print(E1x)
    print(f'r[0] equals {r[0]}')
    E1y = E1Mag * (r[1]/rMag)   #determine y component of E field
    E1z = E1Mag * (r[2]/rMag)   #determine z component of E field

    print(f"The Electric field at {EPosition} from a single charge q is {E1Mag} N/C, in the direction of {r}.")
    EtotalMag = EtotalMag + E1Mag  # add the contribution from single point to total electric field magnitude todo this only adds magnitude, doesn't account for direction
    multiCharges = input("Do you want to add another charge to the system? (Y/N)")
    print(multiCharges)
    print(type(multiCharges))

print(
    f"The Electric field at {EPosition} from the given charges is {EtotalMag} N/C, in the direction of {r}.")  # todo calculate the correct r value for multi point
