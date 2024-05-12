from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen

class MainScreen(Screen):
    def __init__(self , **kw):
        super().__init__(**kw)

    def click(self):
        self.ids.ball.size_hint = (1 ,1)
        self.ids.ball.pos_hint = {"center_x": 0.5 , "top": 1}

    def noc(self):
        self.ids.ball.size_hint = (3 ,3)
        self.ids.ball.pos_hint = {"center_x": 0.5, "top": 1.8}

class FirstScreen(Screen):
    def __init__(self , **kw):
        super().__init__(**kw)


class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name = 'main'))
        return sm

app = ClickerApp()
app.run()