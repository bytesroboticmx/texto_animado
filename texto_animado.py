import time

text = "Programando en Python3, Matematicas discretas"

for i in range(len(text)):
    print(text[:i+1])
    time.sleep(0.2)
