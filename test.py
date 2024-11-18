#microservice A test program
#By: Seojin Lee
import datetime
import json
import time

if __name__ == "__main__":
    name = input("Please enter your name: ")
    
    check_in_out = input("Are you checking in or out? Please type in or out: ")
    if check_in_out == "in":
        check = "check in"
    else:
        check = "check out"

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    input_data = {
        "action": check,
        "name": name,
        "timestamp": current_time
    }
    
    with open("input.txt", "w") as file:
        json.dump(input_data, file, indent=4)
        file.write("\n")
        
    time.sleep(5)
    
    with open("input.txt", "r") as file:
        output = file.read()
        print(output)
    
    