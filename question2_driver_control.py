# This is a program that checks for the availability of an e-bike. It returns true if its available and false if not
def check_bookings(bookings):
    booking_list=[]                   #empty list that holds all the booked time slots
    not_booked_list=[]                #empty list that will store time slots that have not been booked
    already_booked_list=[]            #empty list that stores timeslots that have already been booked
    
    #iterate over all the bookings and add each time slot range item to the empty booking list 
    for interval in bookings:
        start=interval[0]
        stop=interval[(len(interval)-1)]
        for time in range(start,stop+1): 
            booking_list.append(time)

    #make an assumption that duplicate elements in booking_list means it was already booked
    for time in booking_list:   
        if time not in not_booked_list:
            not_booked_list.append(time)         #iterate over each item in the new booking list to remove duplicates 
        else:
            already_booked_list.append(time)  #stores all the duplicate time slots

    if len(already_booked_list)<1:       #checks if the already_booked_list has an element stored
        return True                 #returns true if already_booked_list has no time slot
    else:
        return False 
   
            
if __name__=='__main__':      
    print(check_bookings([[1,4], [2,5], [7,9]]))  #Test case 1 output: False
    print(check_bookings([[6,7], [2,4], [8,12]])) #Test case 2 output:True
    print(check_bookings([[4,5], [2,3], [3,6]])) #Test case 3  output:False
    print(check_bookings([[4,5], [2,3], [7,10],[12,18]])) #Test case 4 output:True
