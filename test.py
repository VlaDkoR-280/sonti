import multiprocessing as mp
import os


def addi(num1, num2):
    print(num1 + num2)

def calc(num1, num2):

    m = mp.Process(target=addi, args=(num1, num2))
    m.start()

    print("here is main", os.getpid())
    m.join()
if __name__ == "__main__":
    calc(5, 6)
