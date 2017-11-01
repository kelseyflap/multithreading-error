from threading import Thread
import time

def func1(delay, repeats):
    while repeats > 0:
        time.sleep(delay)
        print("This is a message.")
        repeats -= 1
    
def func2(delay, repeats):
    while repeats > 0:
        time.sleep(delay)
        word = input("Enter a word and I will repeat it: ") 
        print(word)
        repeats -= 1
        
def Main():
    f1 = Thread(target = func1, args = (1, 5))
    f2 = Thread(target = func2, args = (2, 2))
    f1.start()
    f2.start()
    
if __name__ == '__main__':
    Main()
    