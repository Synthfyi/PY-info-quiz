import time

#QUESTONS

# Q - First Name

print("Please Enter Your First Name...")
firstname = input()
time.sleep(0.1)

# Q - Last Name

print("Please Enter Your Last Name...")
lastname = input()
time.sleep(0.1)

# Q - Age

print("Please Enter Your Age (years)...")
age = input()
time.sleep(0.1)

#PRINTING AWNSERS TO TXT

save = open('./info_save.txt', 'w')
save.write("FIRST NAME : ")
save.write(firstname)
save.write("\n")
save.write("LAST NAME : ")
save.write(lastname)
save.write("\n")
save.write("AGE : ")
save.write(age)