import subprocess
import subprocess
 
# getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
 
# decoding meta data
data = meta_data.decode('utf-8', errors ="backslashreplace")
 
# spliting data by line by line
data = data.split('\n')
 
# creating a list of profiles
profiles = []
 
# traverse the data
for i in data:
     
    # find "All User Profile" in each item
    if "All User Profile" in i :
         
        # if found
        # split the item
        i = i.split(":")
         
        # item at index 1 will be the wifi name
        i = i[1]
         
        # formatting the name
        # first and last chracter is use less
        i = i[1:-1]
         
        # appending the wifi name in the list
        profiles.append(i)  
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")
for i in profiles:
    try:
        results = subprocess.check_output(['netsh','wlan', 'show', 'profiles',i,"Key=clear"])
        results = results.decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b] 
        try:
            print("{:<30}| {:<}".format(i, results[0]))
         
        # else it will print blank in fornt of pass word
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))         
    # called when this process get failed
    except subprocess.CalledProcessError:
        print("Encoding Error Occured") 
print(input())