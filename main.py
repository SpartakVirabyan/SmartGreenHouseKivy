from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty


class GreenHouse(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('design.kv')


GreenHouse().run()