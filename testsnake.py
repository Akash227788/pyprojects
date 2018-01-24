#snake and ladder program

import random
count=0
d=0
repeat=True
a =( random.randint(1, 6))
while repeat:
    print(" u have won the game ",a )
    print("Do you want to roll again? Y/N")
    repeat = "Y" in input()
