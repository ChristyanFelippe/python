import threading
import time

def main():
    threads = [
        threading.Thread(target=contar, args=('elefante',10)),
        threading.Thread(target=contar, args=('buraco',8)),
        threading.Thread(target=contar, args=('moeda',23)),
        threading.Thread(target=contar, args=('pato',12))
        ]


    [th.start() for th in threads]
    print('\nPodemos ir fazendo outras coisas enquanto o programa está executando\n')
    [th.join() for th in threads]
    print('Pronto')

def contar(o_que, numero):
    for n in range (1, numero+1):
        print(f'{o_que} : {n}')
        time.sleep(0)

if __name__ == '__main__':
    main()
