# coding: utf-8
# author: Cesar Godoi

from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex as gch
from kivy.core.window import Window

Window.clearcolor = gch('#ffffff')

kv_code = '''
#:import gch kivy.utils.get_color_from_hex

<Green@FloatLayout>:
    size_hint: .3, .3
    canvas.before:
        Color: 
            rgba: gch('#22ffaa')
        Rectangle:
            pos: self.pos
            size: self.size

FloatLayout:
    Green:
        pos_hint: {'center_x': .5, 'center_y': .5}

'''


class AppApp(App):
    
    def build(self):
        return Builder.load_string(kv_code)


app = AppApp()
app.run()
