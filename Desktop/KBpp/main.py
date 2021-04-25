
# main.py
# import the kivy module
import kivy
import os
  
# It’s required that the base Class 
# of your App inherits from the App class.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

os.environ['KIVY_WINDOW'] = 'egl_rpi'

from kivy.core.window import Window
Window.size=(800,480)
Window.fullscreen = True

# This class stores the info of .kv file
# when it is called goes to my.kv file
class KeypadWidget(GridLayout): 
    pass
    def say_hello(self):
        print("Hello World")
    def keyboard_send_r1c1(self):
        os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/keybindings/r1c1.txt",'r').read()+"\'")
    def keyboard_send_r1c2(self):
        os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/keybindings/r1c2.txt",'r').read()+"\'")
    def keyboard_send_r1c3(self):
        os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py \'" + open("/home/pi/Desktop/keybindings/r1c3.txt",'r').read()+"\'")
    def keyboard_send_hello(self):
        os.system("python3 /home/pi/BL_keyboard_RPI/keyboard/send_string.py 'Hello World'")
class MainWidget(BoxLayout):
    pass
    def program_exit(self):
            exit()


class MenuWidget(BoxLayout):
    pass
    def program_exit(self):
        exit()
  
# we are defining the Base Class of our Kivy App
class GUI_KBppApp(App):
    def build(self):
        self.title = "KB++ GUI v0.1"
        # return a MainWidget() as a root widget
        return MainWidget()
    
  
if __name__ == '__main__':
      
    # Here the class MyApp is initialized
    # and its run() method called.
    GUI_KBppApp().run()

