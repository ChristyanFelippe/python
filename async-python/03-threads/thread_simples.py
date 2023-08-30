import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante',10))
    th.start()
    print('Podemos ir fazendo outras coisas enquanto o programa está executando')
    th.join()
    print('Pronto')

def contar(o_que, numero):
    for n in range (1, numero+1):
        print(f'{o_que} : {n}')
        time.sleep(1)

if __name__ == '__main__':
    main()
