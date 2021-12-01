x = 1
formula = int((x**2+x)/2)
blocks = int(input("Input a number: "))

ended = False

what_step = 0
inStep = None

while not(ended):
    if formula == blocks:
        ended = True
        inStep = True
    if formula > blocks:
        ended = True
        inStep = False
    x += 1
    what_step += 1
    formula = int((x**2+x)/2)

if inStep == True:
    print("It is in the pattern")
    print(f"It is in step {what_step}")
else:
    print("It's not in the pattern")
    x = x-2
    formula = int((x**2+x)/2)
    difference = blocks - formula
    print(f"Difference between the right number of blocks is {difference}. This difference is the block difference from step {x}")