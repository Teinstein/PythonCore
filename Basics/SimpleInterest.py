#Program to calcualte simple interest and total amount

#Function to calculate simple interest
def simpleInterest(princi,rate,time):
    return (princi*rate*time)/100;

def totalAmount(princi,simpleInt):
    return princi + simpleInt;
    

while True:
    princi = input("Enter Principal Amount:")
    #Checking if Principal Amount Entered is a Number and is not less than 0
    if princi.isdigit() == False and float(princi) <= 0:
         break;
    
    rate = input("Enter Rate of Interest:")
    #Checking if Rate Entered is a Number and is not less than 0 or more than 100
    if rate.isdigit() == False and 0 > float(rate) > 100:
         break;
    
    time = input("Enter duration:")
    #Checking if Time Entered is a Number and is not less than 0
    if time.isdigit() == False and float(time) < 0:
         break;
    
    print("The simple interest for the given inputs is :", simpleInterest(float(princi),
                                                                          float(rate),
                                                                          float(time)))
    print("The Total Amount for the given inputs is :", totalAmount(float(princi),
                                                                        simpleInterest(float(princi),
                                                                                       float(rate),
                                                                                       float(time))))
    break;