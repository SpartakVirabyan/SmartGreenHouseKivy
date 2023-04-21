import threading

from kivy import Config
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
import service
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '650')

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        threading.Thread(target=service.add_array()).start()
        self.screen =  Builder.load_file('design.kv')
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in service.array
        ]
        self.dropdown = MDDropdownMenu(caller=self.screen.ids.toolbar.ids.left_actions,items=menu_items,
            width_mult=4,)

    def menu_callback(self, plant: str):
        if not plant == "None":
            service.auto_set(plant)
        else:pass

    def button(self,key):
        service.button(key)
    def build(self):
        self.title = "GreenHouse"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        Clock.schedule_interval(lambda dt: self.update_data(), 1)
        return self.screen

    def update_data(self):
        self.screen.ids["temperature"].text = str(service.get_temp())
        self.screen.ids["humidity"].text = str(service.get_hum())
        self.screen.ids["soil"].text = str(service.get_soil())

app = MainApp()
app.run()
