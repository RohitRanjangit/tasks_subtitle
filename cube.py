import time 
import pyautogui 
import math

# pause for 10 seconds
time.sleep(10)  

# coordinates of bottom right corner
end_x, end_y = (pyautogui.size())

start_x, start_y = end_x/2, end_y/2

# set size of cube
cube_size=100

x_dest=cube_size*math.cos(math.pi/6)
y_dest=cube_size*math.sin(math.pi/6)



pyautogui.moveTo(start_x, start_y)
pyautogui.dragRel(0, cube_size)
pyautogui.dragRel(-x_dest, y_dest)
pyautogui.dragRel(-x_dest, -y_dest) 
pyautogui.dragRel(x_dest, -y_dest) 
pyautogui.dragRel(0, -cube_size)    
pyautogui.dragRel(x_dest, y_dest)
pyautogui.dragRel(0, cube_size)
pyautogui.dragRel(-x_dest, -y_dest)
pyautogui.dragRel(-x_dest, y_dest) 
pyautogui.dragRel(0, -cube_size) 
pyautogui.dragRel(x_dest, -y_dest) 
