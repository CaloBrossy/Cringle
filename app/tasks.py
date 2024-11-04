import time

def example(seconds):
    print('Empezando tarea')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Tarea completa')
    