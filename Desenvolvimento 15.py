# Bomba_Relógio

import time

i = 10
print("Explosão em: ")
while i >= 0:
    time.sleep(1)
    print(i)
    if i == 0:
        print("BUM!")
    i -= 1
