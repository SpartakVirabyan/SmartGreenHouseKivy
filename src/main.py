import threading
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
import service
from kivy.core.window import Window
Window.size = (350, 600)

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
            threading.Thread(target=service.auto_set(plant)).start()
            self.dropdown.dismiss()
        else:
            threading.Thread(target=service.set_default()).start()
            self.dropdown.dismiss()

    def button(self,key):
        threading.Thread(target=service.button(key)).start()
        threading.Thread(target=self.set_background(key,service.get_ref(key).get())).start()

    def build(self):
        self.title = "GreenHouse"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        threading.Thread(target=Clock.schedule_interval(lambda dt: self.update_data(), 1)).start()
        return self.screen

    def update_data(self):
        threading.Thread(target=self.set_text("temperature",str(service.get_temp())+"°C")).start()
        threading.Thread(target=self.set_text("humidity", str(service.get_hum())+"%")).start()
        threading.Thread(target=self.set_text("soil", str(service.get_soil()))).start()
    def set_background(self,id,bool):
        if bool:
            self.screen.ids[id].md_bg_color = self.theme_cls.primary_light
        else:
            self.screen.ids[id].md_bg_color = self.theme_cls.primary_dark
    def set_text(self,id,func:str):
        self.screen.ids[id].text = func

app = MainApp()
threading.Thread(target=app.run()).start()
