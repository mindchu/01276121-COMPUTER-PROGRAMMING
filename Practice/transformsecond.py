print(" *** Transform seconds ***")
time = input("Enter seconds : ")
time = int(time)
hour = 0
minute = 0

if time >= 3600: # 1 hour = 3600 seconds
    hour = time // 3600
    time = time % 3600
if time >= 60: # 1 minute = 60 seconds
    minute = time // 60
    time = time % 60

print(f"{hour}h:{minute}m:{time}s")
print("===== End of program =====")