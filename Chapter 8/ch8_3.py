def seperate_inp(num):
    if num == None:
        return None, None
    else:
        index = 0
        divisor_arr = []
        phase_arr = []
        for char in num:
            if index % 2 == 0:
                divisor_arr.append(char)
            else:
                phase_arr.append(char)
            index += 1
        divisor_arr = list(map(int, divisor_arr))
        return divisor_arr,phase_arr

def check(num,divisor_arr,phase_arr):
    phase = None
    for divisor in divisor_arr:
        if num % divisor == 0:
            if phase == None:
                phase = phase_arr[divisor_arr.index(divisor)]
            else:
                phase = phase + phase_arr[divisor_arr.index(divisor)]
    if phase == None:
        return num
    else:
        return phase

inp = input("input : ").split()
start = int(inp.pop(0))
end = int(inp.pop(0))
divisor_arr,phase_arr = seperate_inp(inp)
for num in range(start,end+1):
    print(check(num,divisor_arr,phase_arr))
