# Uses python3
import sys

def optimal_sequence_old(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence(a):
    result = [1]
    value = {1 : [1]}
    available_ops = [1, 2, 3]

    for i in range(2, a+1):
        if i  % 3 == 0 and i >= 3:
            
            temp3 = list(value.get(i / 3))
            temp3.append(temp3[-1] * 3)
            # print("temp3:", temp3)
        else:
            temp3 = []

        if i % 2 == 0 and i >= 2: 
            
            temp2 = list(value.get(i / 2))
            temp2.append(temp2[-1] * 2)
            # print("temp2:", temp2)

            if len(temp3) != 0 and len(temp3) <= len(temp2):
                value[i] = temp3 
            if len(temp3) == 0  or len(temp3) > len(temp2):
                value[i] = temp2
        else:
            value[i] =temp3

        temp1 = list(value.get(i - 1))
        temp1.append(temp1[-1] + 1)
        # print("temp1:", temp1)
        # print("value[{}]: {}".format(i, value[i]))

        if len(value[i]) == 0 or len(temp1) < len(value[i]) :
            value[i] = temp1
    return value[a]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
