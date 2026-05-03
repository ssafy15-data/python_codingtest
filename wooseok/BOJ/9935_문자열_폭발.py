import sys

input = lambda: sys.stdin.readline().rstrip()

input_string = input()
trigger = input()
trigger_length = len(trigger)

stack = []
for x in input_string:
    stack.append(x)
    if x == trigger[-1] and len(stack) >= trigger_length:
        if ''.join(stack[-trigger_length:]) == trigger:
            for _ in range(trigger_length):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
