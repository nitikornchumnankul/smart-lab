from gpiozero import LED, Button, Buzzer
import serial
led1 = LED(17)
sw1 = Button(21)

serialPort = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
def sw1Pressed():
    serialPort.write("SW1 Pressed".encode('utf-8'))

sw1.when_pressed = sw1Pressed
