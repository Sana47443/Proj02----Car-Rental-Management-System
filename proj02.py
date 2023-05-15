###########################################################################################################################################################
#  Computer Project #2
#
#  Algorithm
#    importing required modules(math module)
#    printing the banner for the car rental for the user
#    starting a while loop which is looping until it stays True
#       prompt for whether to continue the loop or not(else it would exit)
#       prompt for customer code 
#       if desired prompt id not recieved, prompting again and agin until the user enters the desired customer code
#       after desired customer code recieved
#          prompt for number of days(integer)
#          prompt for starting odometer starting reading(integer)
#          prompt for ending odometer reading(integer)
#          a condtional statement for a special case of odometer where the atsrting reading is greater than the ending reading
#             total number of miles calculated
#          conditional stament 1 for the 1st customer code(1st in my program) of the three(if the inputted customer code matches with this, we go into this)
#             calculation of the total bill amount
#             printing customer summary
#          conditional stament 2 for the 2nd customer code(2nd in my program) of the three(if the inputted customer code matches with this, we go into this)
#             calculation of the total bill amount according to the constraints
#             printing customer summary
#          conditional stament 3 for the 3rd customer code(3rd in my program) of the three(if the inputted customer code matches with this, we go into this)
#             calculation of the total bill amount according to the constraints
#             printing customer summary
###########################################################################################################################################################

import math     #importing math module for the usage of math.ceil() for future usage in the program

BASE_BD=40      #Symbolic constant - base charge for customer code BD
BASE_D=60       #Symbolic constant - base charge for customer code D
BASE_W=190      #Symbolic constant - base charge for customer code W
PER_MILE_CHARGE=0.25     #Symbolic constant - per mile charge
NUM_DAYS_IN_A_WEEK=7     #Symbolic constant - number of days in a week

print("\nWelcome to Horizons car rentals. ")            #printing the banner for the user
print("\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")
while True:              #While loop statement
    choice_user=input("\nWould you like to continue (A/B)? ")    #user input for their choice
    if choice_user=="B":               #to exit the loop or else the loop will go on 
        print("\nThank you for your loyalty.")
        break
    else:        
        cus_code=input("\nCustomer code (BD, D, W): ")           #the program reaches here as the user desires to use this system    
        if cus_code!="BD" and cus_code!="D" and cus_code!="W":   #if the user inputs an invalid customer codes, this will check and 
            while (cus_code!="BD" and cus_code!="D" and cus_code!="W"):   #using this while loop, the program keeps prompting again and again until the users enters a valid code
                print("\n\t*** Invalid customer code. Try again. ***")
                cus_code=input("\nCustomer code (BD, D, W): ")
        if cus_code=="BD" or cus_code=="D" or cus_code=="W":  #the program goes into this as the user inputs the valid customer code 
            num_days=int(input("\nNumber of days: "))         #this line and the below 2 lines prompt for required details for calculation
            odo_start=int(input("\nOdometer reading at the start: "))
            odo_end=int(input("\nOdometer reading at the end:   "))
            if odo_start>odo_end:           #this special if statement is when the odometer for example is 999998 at the start and ending reading is 000045. It is for special cases like that
                miles=((1000000-odo_start)+odo_end)/10    #arithmetic calculation to get the correct number of miles
            else:
                miles=(odo_end-odo_start)/10       #this is when the ending reading is greater than the starting reading
        
            if cus_code=="BD":       #if the inputted customer code matches BD, the program goes into this
                charge= float(BASE_BD*num_days + PER_MILE_CHARGE*miles)  #total cost calculation
                
                print("\n\nCustomer summary:")            #printing the customer summary 
                print("\tclassification code:",cus_code)
                print("\trental period (days):",num_days)
                print("\todometer reading at start:",odo_start)
                print("\todometer reading at end:  ",odo_end)
                print("\tnumber of miles driven: ",miles)
                print("\tamount due: $",charge)
                
            elif cus_code=="D":      #if the inputted customer code matches D, the program goes into this
                avg_mil_day= miles/num_days    #calculating average number of miles driven a day
                if avg_mil_day>100:            #if the average miles driven a day is greater than the limiting value of miles to be driven in a day(which is 100), the program goes into this
                    limit_mil_day= 100*num_days     #calculation of the total number of limiting miles over the course of given days
                    charge=float(BASE_D*num_days+\
                                 (miles-limit_mil_day)*PER_MILE_CHARGE)     #calculating charge which includes the base charge over the days and the cost of the miles apart from the limiting miles over the course of the days
                    
                else:
                    charge=float(BASE_D*num_days)   #if the average miles driven a day is less than or equal to 100, the charge is just the base charge over the course of the days
                    
                print("\n\nCustomer summary:")      #printing customer summary
                print("\tclassification code:",cus_code)
                print("\trental period (days):",num_days)
                print("\todometer reading at start:",odo_start)
                print("\todometer reading at end:  ",odo_end)
                print("\tnumber of miles driven: ",miles)
                print("\tamount due: $",charge)                    
                    
            elif cus_code=="W":       #if the inputted customer code matches W, the program goes into this
                num_weeks= math.ceil(num_days/NUM_DAYS_IN_A_WEEK)    #here, we use math.ceil() function to round up the number of weeks
                avg_mil_week=miles/num_weeks                         #calculating average number of miles per week
                if avg_mil_week<=900:                                #if the average number of miles per week is less than or equal to 900 miles,the program goes into this  
                    charge=float(BASE_W*num_weeks)                   #the charge under this condition is just the base charge over the course of number of weeks
                    
                elif avg_mil_week>900 and avg_mil_week<=1500:        #if the average number miles per week is more than 900 but less than or equal to 1500, the program goes into this
                    charge=float(BASE_W*num_weeks+(100*num_weeks))   #the charge under this condition includes the base charge and additional charge 100(per week) multiplied over the course of the weeks
                    
                elif avg_mil_week>1500:                              #if the average number of miles per week is greater than 1500, the program goes into this
                    limit_mil_week=1500*num_weeks                    #here, the proram is calculating the total limiting miles(ehich is 1500 per week)
                    charge=float( BASE_W*num_weeks+ 200*num_weeks+ \
                                 (PER_MILE_CHARGE)*(miles-(limit_mil_week)))      #the charge under this condition includes the nase charge and additional charge 200(per week) multiplied over the course of the weeks and the cost of the miles apart from the limiting miles over the course of the weeks
                    
                print("\n\nCustomer summary:")       #printing customer summary 
                print("\tclassification code:",cus_code)
                print("\trental period (days):",num_days)
                print("\todometer reading at start:",odo_start)
                print("\todometer reading at end:  ",odo_end)
                print("\tnumber of miles driven: ",miles)
                print("\tamount due: $",charge)              
            
            
            
            
            
            
            
            
            
            
            
            
    
    
