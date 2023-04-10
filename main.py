from kivy import Config
from kivy.lang import Builder
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
        self.temperature = db.reference('/Temperature').get()
        self.humidity = db.reference('/Humidity').get()
        self.soil = db.reference('/Soil humidity').get()
        self.screen =  Builder.load_file('design.kv')
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
        )
        self.screen.ids["temperature"].text = str(self.temperature)
        self.screen.ids["humidity"].text = str(self.humidity)
        self.screen.ids["soil"].text = str(self.soil)

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        self.title = "GreenHouse"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return self.screen

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
MainApp().run()