from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
import json

dotas = {
    "score": 0,
    "power":1,
}

def read_data():
    global dotas
    try:
        with open("play.json" , "r" , encoding="UTF-8") as file:
            dotas = json.load(file)
    except:
        print("eroor")

def save_data():
    global dotas
    try:
        with open("play.json" , "w" , encoding="UTF-8") as file:
            json.dump(dotas , file , indent=3 , ensure_ascii=True)
    except:
        print("eroor")

class MainScreen(Screen):
    def __init__(self , **kw):
        super().__init__(**kw)
    def on_enter(self, *args):
        read_data()
        self.ids.scorelabel.text = 'рахунок: ' +str(dotas["score"])


    def gclick(self):
        self.ids.ball.size_hint = (1 ,1)
        self.ids.ball.pos_hint = {"center_x": 0.5 , "top": 1}
        read_data()
        dotas["score"] +=  dotas["power"]
        self.ids.scorelabel.text = 'рахунок: ' + str(dotas["score"])
        save_data()

    def noc(self):
        self.ids.ball.size_hint = (1.2 ,1.2)
        self.ids.ball.pos_hint = {"center_x": 0.5, "top": 1.2}

    def gclick2(self):
        self.manager.current = "first"

class FirstScreen(Screen):
    def __init__(self , **kw):
        super().__init__(**kw)
    def click(self):
        self.manager.current = "main"


class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name = 'first'))
        sm.add_widget(MainScreen(name='main'))
        return sm

app = ClickerApp()
app.run()