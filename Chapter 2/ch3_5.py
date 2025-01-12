print(" *** Transform second ***")
time = input("Enter seconds : ")
try:
    time = float(time)
    time = int(time)
except:
    print(f"! ! ! please enter a whole number ==> {time}")
    print(f"This number ({time}) is not VALID !!!")
    print("===== program end =====")
    quit()

if time < 0:
    print(f"This number ({time}) is not VALID !!!")
    print("===== program end =====")
    quit()

print(f"{time:,} seconds ==> ",end="")

if time >= 604800: # 1 week = 604800 seconds
    week = time // 604800
    time = time % 604800
    if week == 1:
        print(f"{week} week ",end="")
    else:
        print(f"{week} weeks ",end="")

if time >= 86400: # 1 day = 86400 seconds
    day = time // 86400
    time = time % 86400
    if day == 1:
        print(f"{day} day ",end="")
    else:
        print(f"{day} days ",end="")

if time >= 3600: # 1 hour = 3600 seconds
    hour = time // 3600
    time = time % 3600
    if hour == 1:
        print(f"{hour} hour ",end="")
    else:
        print(f"{hour} hours ",end="")

if time >= 60: # 1 minute = 60 seconds
    minute = time // 60
    time = time % 60
    if minute == 1:
        print(f"{minute} minute ",end="")
    else:
        print(f"{minute} minutes ",end="")

if time != 0 :
    if time == 1:
        print(f"{time} second")
    else:
        print(f"{time} seconds")
else:
    print()

print("===== program end =====")