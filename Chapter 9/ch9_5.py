increment = input("Enter increment : ")
increment = float(increment)
count = 0
value = 0
for multi in range(1,10001):
    count += 1
    value += increment
    expected_value = str(increment * multi).rstrip("0")
    if expected_value != str(value).rstrip("0"):
        break
if multi == 10000:
    print("reached max increment, breaking.")
else:
    print(f"accumulated {count} times")
    print(f"final accumulated value is {value}")
    print(f"which does not equal the expected {expected_value}")