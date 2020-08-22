
import RPi.GPIO as gpio
import time
import keyboard

gpio.setmode(gpio.BCM)
gpio.setupwarning(False)
# setting up the gpio pins along with enabling pwm
Motor1 = {'EN': 25, 'input1': 24, 'input2': 23}
Motor2 = {'EN': 17, 'input1': 27, 'input2': 22}

for x in Motor1:
    gpio.setup(Motor1[x], gpio.OUT)
    gpio.setup(Motor2[x], gpio.OUT)

EN1 = gpio.PWM(Motor1['EN'], 100)    
EN2 = gpio.PWM(Motor2['EN'], 100)    

EN1.start(0)                    
EN2.start(0)                    


#definig forward and backward functions.
def forward(speed, sleep_time):
    EN1.ChangeDutyCycle(speed)
    EN2.ChangeDutyCycle(speed)

    gpio.output(Motor1['input1'], gpio.HIGH)
    gpio.output(Motor1['input2'], gpio.LOW)
        
    gpio.output(Motor2['input1'], gpio.HIGH)
    gpio.output(Motor2['input2'], gpio.LOW)

    
    time.sleep(sleep_time)
   

def backward(speed, sleep_time):
    
    EN1.ChangeDutyCycle(speed)
    EN2.ChangeDutyCycle(speed)
        
    gpio.output(Motor1['input1'], gpio.LOW)
    gpio.output(Motor1['input2'], gpio.HIGH)

    gpio.output(Motor2['input1'], gpio.LOW)
    gpio.output(Motor2['input2'], gpio.HIGH)


    time.sleep(sleep_time)
    

def stop(): #This will stop the mootrs
    EN1.ChangeDutyCycle(0)
    EN2.ChangeDutyCycle(0)

    
def key_input(event):
    
    print('Key :' + event.char)
    key_press = event.char
    sleep_time = 0.030
    temp_speed = 10   
    print(
    while True:
        
        if keyboard.is_pressed('q') :
            if(temp_speed >= 0){
            temp_speed -= 10    # decrementing the speed 
            print("speed = %d" % temp_speed) 
            }
            else{
                print("min speed reached\n")
            }
        elif keyboard.is_pressed('e'):  
            if(temp_speed <= 100){  
            temp_speed += 10    # incrementing the speed 
            print("speed = %d" % temp_speed)
            }
            else{
                print("max speed reached\n")
            }

        elif keyboard.is_pressed('w'): #moving forward
            print("key pressed is w")
            forward(temp_speed,sleep_time)
        elif keyboard.is_pressed('s'): #moving backward
            print("key pressed is s")
            backward(temp_speed,sleep_time) 
        elif keyboard.is_pressed('k') :#stopping motion
            stop()
        else:
            pass



gpio.cleanup()




