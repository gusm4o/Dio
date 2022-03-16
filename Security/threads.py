import time
from threading import Thread


def car1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Rubinho: ', trajeto)
        trajeto+=velocidade

def car2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Massa: ', trajeto)
        trajeto+=velocidade

def corrida(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(1)
        print('#' * 60)
        print('Piloto: {}  KM: {}\n'.format(piloto, trajeto))
#car1(10)
#car2(50)

time_car1 = Thread(target=corrida, args=[10, 'Felipe'])
time_car2 = Thread(target=corrida, args=[20, 'Josue'])
#time_car1 = Thread(target=car1, args=[1])
#time_car2 = Thread(target=car2, args=[10,])

time_car1.start()
time_car2.start()

