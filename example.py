from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class WidgetGalaxy(GridLayout):
    counter = 1
    counter_enabled = BooleanProperty(False)
    my_text = StringProperty(str(counter))
    text_input_str = StringProperty("")
    
    
    def on_button_click(self):
        self.counter += 1
        self.my_text = str(self.counter)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.counter_enabled = False
        else:
            widget.text = "ON"
            self.counter_enabled = True
    
    def on_text_validate(self,widget):
        self.text_input_str = widget.text
        
        
class WidgetExample(App):
    def build(self):
        return WidgetGalaxy()

if __name__ == "__main__":
    WidgetExample().run()