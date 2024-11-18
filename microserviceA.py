#microservice A
#By: Seojin Lee
import json
import os
import time

#get input from the user 
def read_input():
    try:
        with open("input.txt", 'r') as file:
            info = json.load(file)
        return info
    
    except:
        return None

#function for checking in
def check_in_JSON(input_data):
    json_file = "student_info.json"
    
    if input_data is None:                    #if no data was passed
        return

    name = input_data["name"]                 #get name from passed in input
    
    student_data = {                    #format the new student data for json
        "name": input_data["name"],
        "timestamp": input_data["timestamp"]
    }
    
    if os.path.exists(json_file):    #if a json file already exists
        with open(json_file,'r+') as file:    #opens json file
            json_data = json.load(file)
            
            for item in json_data.get("data", []):      #checks it see if input name already checked in
                if item.get("name") == name:
                    existing_timestamp = item.get("timestamp", "unknown")
                    
                    with open("input.txt", 'w') as file:        #returns message if name already checked in
                        file.write(f"{name} already checked-in at {existing_timestamp}\n")
                        return

            #adds new student to the json file list
            json_data["data"].append(student_data)
            file.seek(0)
            json.dump(json_data, file, indent = 4)
    
    else:                   #if a json file does not exist
        output_data = {     #formatting new json file
        "status": "success",
        "message": "Checked-in users retrieved successfully.",
        "data": [student_data]
        }
        
        with open(json_file, 'w') as file:        #write to new json file
            json.dump(output_data, file, indent=4)

    #message that name as checked in correctly
    with open("input.txt", 'w') as file:
        file.write(f"Checked-in {name} successfully. \n")

#function for checking out
def check_out_JSON(input_data):
    json_file = "student_info.json"   
    
    if input_data is None:              #if no data was passed
        return

    name = input_data["name"]           #get name from passed in input
    
    if os.path.exists(json_file):       #if a json file already exists
        with open(json_file,'r+') as file:
            json_data = json.load(file)     #opens json file
        
        found = 0
        for item in json_data.get("data", []):      #check json file for matching name
            if item.get("name") == name:
                json_data["data"].remove(item)      #if there is a match from input name then delete
                found = 1                           #the name thus checking them out
                break
        
        if found == 1:      #if there was a match found
            with open(json_file, 'w') as file:
                json.dump(json_data, file, indent=4)        #update json file
            with open("input.txt", 'w') as file:
                file.write(f"Checked-out {name} successfully. \n")  #return checked out message
        
        else:       #if there was no match
            with open("input.txt", 'w') as file:
                file.write(f"Could not find {name} in the checked-in list. \n") #return not found message
    
    else:        #if a json file does not exist
        with open("input.txt", 'w') as file:
            file.write("The student_info JSON does not exist. \n")

#checks to see with function to use
def option(input_data):
    if input_data["action"] == "check in":        #checking in
        check_in_JSON(input_data)
            
    elif input_data["action"] == "check out":     #checking out
        check_out_JSON(input_data)
  
#main function
if __name__ == "__main__":
    while(True):                #waits for correct input from user
        input_data = read_input()
        
        if input_data is not None and input_data["action"] is not None:  #if it gets a correct input
            option(input_data)
        
        time.sleep(3)


    