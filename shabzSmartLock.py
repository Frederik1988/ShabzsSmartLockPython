import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import socket
import threading
from threading import Lock, Thread
import shabzLockDisplay

TCP_IP = "192.168.24.239"
TCP_PORT = 9576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT)) 

messageLocked = "The door is locked"
messageUnlocked = "The door is unlocked"
messageJoystickUnlock = "The door is unlocked by joystick"
messageJoystickLock = "The door is locked by joystick"

sense = SenseHat()
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
lock = Lock()
i = 1

lock_display = Lock()
display = padlock

pwm.start(7)
sense.set_pixels(locked)

def set_display():
  
  global display
  
  while True:
    
    lock_display.acquire()
    lock_display.release()
    
    for event in sense.stick.get_events():
        if event.action == "left":
          display = padlock
        
    for event in sense.stick.get_events():
        if event.action == "right":
          display = star
          
    for event in sense.stick.get_events():
        if event.action == "up":
          display = tree
          
    for event in sense.stick.get_events():
        if event.action == "down":
          display = firework
          

def joystick(): 
  
  global i
  global display
  
  while True:
    
    lock.acquire()
    lock.release()
    lock_display.acquire()
    lock_display.release()
    
    if (display == padlock):
      
      if (i ==1):
      
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(12)
            sock.send(bytes(messageJoystickUnlock, "UTF-8"))
            sense.show_message(str("HA EN DEJLIG DAG"), scroll_speed=0.04, text_colour=[0, 0, 255])
            sense.set_pixels(padlock_unlocked)
            i = 0
    
      if (i == 0):
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(7)
            sock.send(bytes(messageJoystickLock, "UTF-8"))
            sense.set_pixels(padlock_locked)
            i = 1
            
    if (display == star):
      
      if (i ==1):
      
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(12)
            sock.send(bytes(messageJoystickUnlock, "UTF-8"))
            sense.show_message(str("HA EN DEJLIG DAG"), scroll_speed=0.04, text_colour=[0, 0, 255])
            sense.set_pixels(star_unlocked)
            i = 0
    
      if (i == 0):
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(7)
            sock.send(bytes(messageJoystickLock, "UTF-8"))
            sense.set_pixels(star_locked)
            i = 1
    
    if (display == tree):
      
      if (i ==1):
      
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(12)
            sock.send(bytes(messageJoystickUnlock, "UTF-8"))
            sense.show_message(str("HA EN DEJLIG DAG"), scroll_speed=0.04, text_colour=[0, 0, 255])
            sense.set_pixels(tree_unlocked)
            i = 0
    
      if (i == 0):
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(7)
            sock.send(bytes(messageJoystickLock, "UTF-8"))
            sense.set_pixels(tree_locked)
            i = 1
            
    if (display == firework):
      
      if (i ==1):
      
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(12)
            sock.send(bytes(messageJoystickUnlock, "UTF-8"))
            sense.show_message(str("HA EN DEJLIG DAG"), scroll_speed=0.04, text_colour=[0, 0, 255])
            sense.set_pixels(firework_unlocked)
            i = 0
    
      if (i == 0):
        for event in sense.stick.get_events():
          if event.action == "pressed":
            pwm.ChangeDutyCycle(7)
            sock.send(bytes(messageJoystickLock, "UTF-8"))
            sense.set_pixels(firework_locked)
            i = 1
    


def recieveMessage():
  
  global i
  global display
  
  while True:
    
    lock_display.acquire()
    lock_display.release()
  
    data = sock.recv(1024)
    fromServer = data.decode('utf-8')
    message =  fromServer [0 : 1 -len(fromServer)]
    name = fromServer [1 : len(fromServer)-2]
    
    if (display == padlock): 
      
      if (message =='l'):
      
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(padlock_locked)
        sock.send(bytes(messageLocked, "UTF-8"))
        i = 1
        lock.acquire()
        lock.release()
      
      
      if (message == 'o'):  
      
        pwm.ChangeDutyCycle(12)        
        sock.send(bytes(messageUnlocked, "UTF-8"))
        sense.show_message(str(name), scroll_speed=0.04, text_colour=[0, 0, 255])
        sense.set_pixels(padlock_unlocked)
        i = 0
        lock.acquire()
        lock.release()
      
    if (display == star): 
      
      if (message =='l'):
      
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(star_locked)
        sock.send(bytes(messageLocked, "UTF-8"))
        i = 1
        lock.acquire()
        lock.release()
      
      
      if (message == 'o'):  
      
        pwm.ChangeDutyCycle(12)        
        sock.send(bytes(messageUnlocked, "UTF-8"))
        sense.show_message(str(name), scroll_speed=0.04, text_colour=[0, 0, 255])
        sense.set_pixels(star_unlocked)
        i = 0
        lock.acquire()
        lock.release()
      
    if (display == tree): 
      
      if (message =='l'):
      
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(tree_locked)
        sock.send(bytes(messageLocked, "UTF-8"))
        i = 1
        lock.acquire()
        lock.release()
      
      
      if (message == 'o'):  
      
        pwm.ChangeDutyCycle(12)        
        sock.send(bytes(messageUnlocked, "UTF-8"))
        sense.show_message(str(name), scroll_speed=0.04, text_colour=[0, 0, 255])
        sense.set_pixels(tree_unlocked)
        i = 0
        lock.acquire()
        lock.release()
      
    if (display == firework): 
      
      if (message =='l'):
      
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(firework_locked)
        sock.send(bytes(messageLocked, "UTF-8"))
        i = 1
        lock.acquire()
        lock.release()
      
      
      if (message == 'o'):  
      
        pwm.ChangeDutyCycle(12)        
        sock.send(bytes(messageUnlocked, "UTF-8"))
        sense.show_message(str(name), scroll_speed=0.04, text_colour=[0, 0, 255])
        sense.set_pixels(firework_unlocked)
        i = 0
        lock.acquire()
        lock.release()   
      

thread1 = threading.Thread(target=recieveMessage)
thread2 = threading.Thread(target=joystick)
thread3 = threading.Thread(target=set_display)
			  
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
