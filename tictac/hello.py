from pyjamas import Window
from pyjamas.ui import RootPanel, Button

def greet(sender):
    Window.alert("Hello, AJAX!")

class Hello:
    def onModuleLoad(self):
        b = Button("Click me", greet)
        RootPanel().add(b)
