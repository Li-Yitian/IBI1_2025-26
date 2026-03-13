#input the age, weight, creatine concentration, and gender
#Check if the input values are within the specified ranges:
#age<100 20<weight<80 
#creatine concentration>0 and <100
#gender male/female
#if all the conditions are met, calculate the creatinine clearance (CrCl) using the Cockcroft-Gault equation.
    #if one of these conditions is not met, do not report CrCl but instead which input variable needs corrected.
    #if age >= 100, report "Age is not correct" end if
    #if weight < 20 or weight > 80, report "Weight is not correct" end if
    #if creatine concentration < 0 or creatine concentration > 100, report "Creatine concentration is not correct" end if
    #if gender is not male or female, report "Gender is not correct" end if
#else: all conditions are met, report the creatine clearance (CrCl) using the Cockcroft-Gault formula: CrCl according to the gender
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

