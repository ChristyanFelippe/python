import threading
import time
import random

from typing import List

class Conta:
    def __init__(self, valor=0) -> None:
        self.saldo=saldo
        
        
def main():
    contas = criar_contas()
    total = sum(conta.saldo for conta in contas)
    print('Iniciando transferências...')
    
    tarefas = [
        threading.Thread(target=servicos, args=(contas,total))
    ]
    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]
    
    print('Transferencias completas')
    valida_banco(contas, total)
    
def servicos(contas, total):
    for _ in range(1, 10_000):
        c1,c2 = pega_duas_contas(contas)
        valor = random.randint(1,100)
        transferir(c1,c2,valor)
        valida_banco(contas, total)
        
def criar_contas() -> List(Conta):
    return {
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        
    }
    
def transferir(origem:Conta, destino:Conta, valor: int):
    if origem.saldo < valor:
        