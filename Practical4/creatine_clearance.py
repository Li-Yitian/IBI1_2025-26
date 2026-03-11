#age<100 80>weight>20 
# creatine concentration>0 and <100
#gender male/female
#If one of these conditions is not met, do not report CrCl but instead which input variable needs corrected.
age = float(input("Please enter the age: "))
weight = float(input("Please enter the weight: "))
cr = float(input("Please enter the creatine concentration: "))
gender = input("Please enter the gender (male/female): ").lower()#get information about the age of the patient, the weight, the creatine concentration, and the gender of the patient.
if age >= 100 or weight < 20 or weight > 80 or cr <= 0 or cr >= 100 or gender not in ["male","female"]:
    if age >= 100 :
        print("Age is not correct")
    if weight < 20 or weight > 80:
        print("Weight is not correct")
    if cr <= 0 or cr >= 100:
        print("Creatine concentration is not correct")
    if gender not in ["male", "female"]:
        print("Gender is not correct")#make sure that the input values are within the specified ranges
else: #give out the creatine clearance (CrCl) using the Cockcroft-Gault formula
    if gender == "male":
        crcl = ((140 - age) * weight) / (72 * cr)
    if gender == "female":
        crcl = ((140 - age) * weight) / (72 * cr) * 0.85
    print("The creatine clearance is", crcl)

