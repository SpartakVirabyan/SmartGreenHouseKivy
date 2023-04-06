from kivy import Config
from kivy.lang import Builder
from kivymd.app import MDApp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kivymd.uix.menu import MDDropdownMenu

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '650')

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen =  Builder.load_file('design.kv')
        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item_menu)
        self.cred = credentials.Certificate('smartgreenhouse-a7809-firebase-adminsdk-ltfsz-6e6855dac0.json')
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://smartgreenhouse-a7809-default-rtdb.firebaseio.com/'
        })
        # Set default
        self.ref = db.reference('/')

    def set_item_menu(self, instance):
        self.screen.ids.button.set_item(instance.text)

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