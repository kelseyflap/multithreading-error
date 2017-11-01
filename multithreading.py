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
        word = input("Enter a word and I will repeat it: ") # this part is overridden by the output text
        print(word)
        repeats -= 1
        
def Main():
    f1 = Thread(target = func1, args = (1, 5))
    f2 = Thread(target = func2, args = (2, 2))
    f1.start()
    f2.start()
    # stopping threads abruptly is apparently dangerous and there's no way of doing it safely through the multithreading module so I left that alone
    
if __name__ == '__main__':
    Main()
    
