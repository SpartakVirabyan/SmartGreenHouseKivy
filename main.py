from kivy.lang import Builder
from kivymd.app import MDApp


class GreenHouse(MDApp):

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:
    
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "darkblue"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'Home'
            text: 'Home'
            icon: 'image python//icons8-home-64.png'
            rgb: 75,74,74
            
            
            MDLabel:
                text: 'Home'
                halign: 'center'

                FitImage:
                    source: "image python//greenhouseicon.png"  
                    x:350
                    y:360
                    halign: 'center'    
                    size: "100dp", "100dp"
                    
            MDFillRoundFlatIconButton:
                icon: "image python//icons8-temperature-inside-64.png"
                text: "Heater"
                pos_hint: {"center_x": .5, "center_y": .5}
                
            MDFillRoundFlatIconButton:
                icon: "image python//external-Cooler-propeller-others-inmotus-design-15.png"
                text: "Cooler"
                pos_hint: {"center_x": .5, "center_y": .4}
            MDFillRoundFlatIconButton:
                icon: "image python//icons8-thirst-50.png"
                text: "Water"
                pos_hint: {"center_x": .5, "center_y": .3}
            MDFillRoundFlatIconButton:
                icon: "image python//icons8-ozone-structure-64.png"
                text: "Ozon"
                pos_hint: {"center_x": .5, "center_y": .2}
            
        MDBottomNavigationItem:
            name: 'Value'
            text: 'Value'
            icon: 'image python//icon_value.png'
            md_bg_color: app.theme_cls.primary_light
            

            MDLabel:
                text: 'Value'
                halign: 'center'    

        MDBottomNavigationItem:
            name: 'Help'
            text: 'help'
            icon: 'image python//help-icon-3.png'
            md_bg_color: app.theme_cls.primary_light
            

            MDLabel:
                text: 'Help'
                halign: 'center'  

        MDBottomNavigationItem:
            name: 'Feedback'
            text: 'Feedback'
            icon: 'image python//icons8-comments-64.png'
            md_bg_color: 'grey'

            MDLabel:
                text: 'Feedback'
                halign: 'center'
                

    
'''
        )





GreenHouse().run()