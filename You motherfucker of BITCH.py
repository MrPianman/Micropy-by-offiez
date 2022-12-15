from machine import PWM,Pin
from time import sleep
import threading
p = PWM(Pin(25))
#p.freq(100)
sw26 = Pin(26,Pin.IN)
led18 = Pin(19,Pin.OUT)
spd=1
p.duty(100)

def light():
    while True:
        led18.value(1)
        s(0.5)
        led18.value(0)
        s(0.5)

def speed():
    if sw26.value() and spd==1:
        spd=0.7
        sleep(0.5)
    elif sw26.value() and spd==0.7:
        spd=0.5
        sleep(0.5)
    elif sw26.value() and spd==0.5:
        spd=1
        sleep(0.5)
        
def f(a):
    p.freq(a)

def s(b):
    sleep(b)

def pa(c):
    p.freq(25000)
    sleep(c)

sw26.irq(trigger=Pin.IRQ_FALLING,handler=speed)

while True:
    C4=261; CS4=277; D4=293; DS4=311; E4=329; F4=349; FS4=370; G4=392; GS4=415; A4=440; AS4=466; B4=493
    C5=523; CS5=554; D5=587; DS5=622; E5=659; F5=698; FS5=734; G5=784; GS5=830; A5=880; AS5=932; B5=987
    C6=1046; CS6=1108; D6=1174; DS6=1244; E6=1318; F6=1396; FS6=1480; G6=1568; GS6=1661; A6=1760; AS6=1864; B6=1975
    #-------1
    print(1)
    print(spd)
    f(AS5)
    s(spd)
    pa(0.1)
    f(AS5)
    s(spd)
    f(D5)
    s(spd)
    pa(0.1)
    f(D5)
    s(spd)

    f(AS5)
    s(spd)
    pa(0.1)
    f(AS5)
    s(spd)

    f(G5)
    s(spd+0.5)
    pa(1)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(D5)
    s(spd)
    f(DS5)
    s(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    #-------------2
    print(2)
    print(spd)
    f(AS5)
    s(spd)

    f(D5)
    s(spd)
    pa(0.1)
    f(D5)
    s(spd)

    f(AS5)
    s(spd)
    pa(0.1)
    f(AS5)
    s(spd)

    f(G5)
    s(spd+0.5)
    #-----------3
    print(3)
    print(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(D5)
    s(spd)
    f(DS5)
    s(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(AS5)
    s(spd)
    #-----------4
    print(4)
    print(spd)
    f(D5)
    s(spd)
    pa(0.1)
    f(D5)
    s(spd)

    f(AS5)
    s(spd)
    pa(0.1)
    f(AS5)
    s(spd)

    f(G5)
    s(spd)
    #------------5
    print(5)
    print(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(D5)
    s(spd)
    f(DS5)
    s(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(AS5)
    s(spd)
    #----------6
    print(6)
    print(spd)
    f(D5)
    s(spd)
    f(AS5)
    s(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    f(D5)
    s(spd)
    f(C5)
    s(spd)
    #----------7
    print(7)
    print(spd)

        
'''
C4=261; CS4=277; D4=293; DS4=311; E4=329; F4=349; FS4=370; G4=392; GS4=415; A4=440; AS4=466; B4=493
C5=523; CS5=554; D5=587; DS5=622; E5=659; F5=698; FS5=734; G5=784; GS5=830; A5=880; AS5=932; B5=987
C6=1046; CS6=1108; D6=1174; DS6=1244; E6=1318; F6=1396; FS6=1480; G6=1568; GS6=1661; A6=1760; AS6=1864; B6=1975
'''

#stackoverflow help me 
