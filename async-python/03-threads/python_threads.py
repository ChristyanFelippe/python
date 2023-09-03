import datetime
import math

import threading
import multiprocessing

def main():
    
    qtd_cores = multiprocessing.cpu_count()
    print(f'Quantidade de cores {qtd_cores}')
    
    inicio = datetime.datetime.now()

    threads = [
        
    ]
    for n in range (1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        threads.append(
            threading.Thread(
                target=computar, 
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True,
            ) 
        )
    [th.start() for th in threads]
    [th.join() for th in threads]
    
    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')

def computar(fim,inicio=1):
    posicao = inicio
    fator = 1000 * 1000
    while posicao < fim:
        posicao += 1
        math.sqrt((posicao - fator) * (posicao - fator))

if __name__ == '__main__':
    main()
    """
    Terminou em 10.33 segundos.
    Terminou em 10.61 segundos.
    """