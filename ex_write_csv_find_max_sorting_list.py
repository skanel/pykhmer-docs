 #1. Create a new file name customer.csv
file = open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\customer.csv","w+") 
 
header = ["id", "firstname", "lastname", "age", "phone_number", "missed_call", "date"]

data  = [
            ["1","Sok", "Reaksmey", 12, "092222999", "19", "20190405"],
            ["2","tep", "nimit", 11, "092111999", "9", "20190404"],
            ["3","ket", "chan", 9, "012345666", "10", "20190404"],
            ["4","pongsa", "metrey", 10, "092002999", "11", "20190405"]
        ]


#write header
file.write(','.join(header)+"\n") 

who_is_max_missed_call = []
maximum = 0
date_looking = "20190404"
data_dict = {}

#Loop over data
for item in data:
    file.write(','.join(str(item))+"\n") 
    
    #tranform list to dictionary
    data_dict[item[3]] = item
    
    #3. find who is max of missed_call in the specific date
    if (int(item[5]) > int(maximum) and item[6] == date_looking):
        maximum = item[5]
       
        who_is_max_missed_call= item
    else:
        maximum = maximum
    
#print(who_is_max_missed_call)    

#4. Sort customer list by age, and print it out

#print(data_dict)
result_sorted = [data_dict[key] for key in sorted(data_dict)]
print(result_sorted)
#do it yourself
file.close() 
