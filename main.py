from kivy.lang import Builder
from kivymd.app import MDApp


class GreenHouse(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:
    

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "blue"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'Home'
            text: 'Home'
            icon: 'home'
            md_bg_color: app.theme_cls.primary_light
            
            MDLabel:
                text: 'Home'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'Help'
            text: 'help'
            icon: 'help'
            md_bg_color: app.theme_cls.primary_light
            

            MDLabel:
                text: 'Help'
                halign: 'center'
                

        MDBottomNavigationItem:
            name: 'Feedback'
            text: 'Feedback'
            icon: 'message-alert'
            md_bg_color: app.theme_cls.primary_light

            MDLabel:
                text: 'Feedback'
                halign: 'center'
    
'''
        )





GreenHouse().run()