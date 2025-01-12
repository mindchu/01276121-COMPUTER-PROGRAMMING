print(" *** Number Fun ***")
num = int(input("Enter a 3-digit number : "))
print()
print(f"{'You have entered':21}=> {num}")
print(f"{'Square':21}=> {(num**2):,}")
print(f"{'25% 3 decimal places':21}=> {num*25/100:.3f}%")
print(f"{'Flipping':21}=> {num%10}{num//10%10}{num//100}")
print(f"{'Hexadecimal':21}=> {num:x} or {num:X}")
print(f"{'Binary':21}=> {num:b}")
bina = f"{num:08b}"
bina_8 = bina[-8:]
print(f"{'Binary right 8-digit':21}=> {bina_8[:4]} {bina_8[4:]}")