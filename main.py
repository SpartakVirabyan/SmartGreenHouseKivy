from kivy import Config
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kivymd.uix.menu import MDDropdownMenu

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '650')
cred = credentials.Certificate('smartgreenhouse-a7809-firebase-adminsdk-ltfsz-6e6855dac0.json')
firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://smartgreenhouse-a7809-default-rtdb.firebaseio.com/'
        })
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.array = ['None']
        # Set default
        self.plants = db.reference('/Plants')
        # Set default
        self.ref = db.reference('/')
        for i in self.plants.get():
            self.array.append(i)

        self.screen =  Builder.load_file('design.kv')
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in self.array
        ]
        self.dropdown = MDDropdownMenu(caller=self.screen.ids.toolbar.ids.left_actions,items=menu_items,
            width_mult=4,)

    def menu_callback(self, new_scaling: str):
        if self.plants.child(new_scaling).get()["Temperature"] > db.reference('/Temperature').get():
            self.set("Heating", True)
            if self.plants.child(new_scaling).get()["Temperature"] == db.reference('/Temperature').get():
                self.set("Heating", False)
        else:
            self.set("Cooling", True)
            if self.plants.child(new_scaling).get()["Temperature"] == db.reference('/Temperature').get():
                self.set("Cooling", False)
        if self.plants.child(new_scaling).get()["Humidity"] < db.reference('/Humidity').get():
            self.set("Ozon", True)
            if self.plants.child(new_scaling).get()["Humidity"] == db.reference('/Humidity').get():
                self.set("Cooling", False)
        else:
            self.set("Ozon", False)
        if self.plants.child(new_scaling).get()["Soil humidity"] < db.reference('/Soil humidity').get():
            self.set("Water", True)
            if self.plants.child(new_scaling).get()["Soil humidity"] == db.reference('/Soil humidity').get():
                self.set("Water", False)
        else:
            self.set("Water", False)
        if self.plants.child(new_scaling).get()["Temperature"] == db.reference('/Temperature').get():
            self.set("Heating", False)
            self.set("Cooling", False)
        if self.plants.child(new_scaling).get()["Soil humidity"] == db.reference('/Soil humidity').get():
            self.set("Water", False)
        if self.plants.child(new_scaling).get()["Humidity"] == db.reference('/Humidity').get():
            self.set("Cooling", False)

    def build(self):
        self.title = "GreenHouse"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        Clock.schedule_interval(lambda dt: self.update_data(), 1)
        return self.screen

    def update_data(self):
        self.screen.ids["temperature"].text = str(db.reference('/Temperature').get())
        self.screen.ids["humidity"].text = str(db.reference('/Humidity').get())
        self.screen.ids["soil"].text = str(db.reference('/Soil humidity').get())
    def set(self, part, bool):
        ref = db.reference('/')
        ref.update({part: bool})

    # main buttons command
    def button(self, function):
        ref = db.reference('/')
        if ref.get()[function]:
            self.set(function, False)
        else:
            self.set(function, True)

app = MainApp()
app.run()
