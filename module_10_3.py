from threading import Thread, Lock
from random import randint
import time


class Bank:
    def __iter__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        self.balance = 0
        self.lock = Lock()
        for i in range(100):
            randon_number = randint(50, 500)
            self.balance += randon_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'\nПополнение: {randon_number}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            randon_number = randint(50, 500)
            print(f'\nЗапрос на {randon_number}')
            if self.balance >= randon_number:
                self.balance -= randon_number
                print(f'Снятие: {randon_number}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
