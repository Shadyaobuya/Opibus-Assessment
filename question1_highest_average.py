#This is a program that takes in a list of discharge rates and returns the highest average

def find_highest_average(discharge):
    new_list=[]  #create an empty list that will hold the sum of two contiguous rates 
    for rate in range(len(discharge)-1):
        high=discharge[rate]+discharge[rate+1]      
        new_list.append(high)                  #get the sum of every two contiguous rates and append it to the empty list

    highest_sum=new_list[0]     #make an assumption that the highest sum is at the first index of the empty list
    for i in new_list:        
        if i >=highest_sum:      #loop through the empty list and reasign the value of the highest sum 
            highest_sum=i

    highest_average=highest_sum/2  #get the average of the highest sum
    return highest_average

if __name__=='__main__':
    print(find_highest_average([2, 3, 4, 1, 5])) #test case 1 output 3.5: [3,4]
    print(find_highest_average([2, 3, 4, 8, 1, 5])) #test case 2 output:6.0 [4,8]
    print(find_highest_average([6,1,7,3,9,6])) #test case 3 output:7.5: [9,6]

