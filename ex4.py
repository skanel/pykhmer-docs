 #1. Create a new file name customer.csv
file = open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\customer.csv","w+") 
 
header = ["id", "firstname", "lastname", "age", "phone_number", "missed_call", "date"]

data  = [
            ["1","Sok", "Reaksmey", "29", "092222999", "19", "20190405"],
            ["2","tep", "nimit", "39", "092111999", "9", "20190404"],
            ["3","ket", "chan", "40", "012345666", "10", "20190404"],
            ["4","pongsa", "metrey", "19", "092002999", "11", "20190405"]
        ]


#write header
file.writelines(','.join(header)+"\n") 

who_is_max_missed_call = []
maximum = 0
date_looking = "20190404"

for item in data:
    file.write(','.join(item)+"\n") 
    
    #3. find who is max of missed_call in the specific date
    if (int(item[5])> int(maximum) and item[6]==date_looking):
        maximum = item[5]
        who_is_max_missed_call= item
    else:
        maximum = maximum
    
print(who_is_max_missed_call)    

#4. Sort customer list by age, and print it out

#do it yourself

file.close() 
