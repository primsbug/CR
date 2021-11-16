from kivy.core.window import Window
from kivy.lang import Builder  # Импортируем функциональность консруктора
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel # импортируем метки

Window.size = (300, 500) # Устанавливаем размеры экрана под мобильное устройство

Virus = """
Image:
    source: 'CoronaV.jpg'
"""


navigation_helper = """

Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'CoronaReminder'
                        font_style: 'subtitle1'
                        elevation: 12
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '1dp'
                padding: '8dp'
                
                Image:
                    id: Coron
                    size_hint: None, None
                    size: '225dp', '120dp'
                    source: 'CoronaV.jpg' 
                    
                MDLabel:
                    text: '  workadsupp@mail.ru'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]   
                 
                    
                ScrollView:
                
                    MDList:
                        OneLineIconListItem:
                            text: 'Советы'
                            IconLeftWidget:
                                icon: 'information'
                        OneLineIconListItem:
                            text: 'Напоминалка'
                            IconLeftWidget:
                                icon: 'alarm-check'
                        OneLineIconListItem:
                            text: 'О Covid-19'
                            IconLeftWidget:
                                icon: 'flask-round-bottom'
                        OneLineIconListItem:
                            text: 'Настройки'
                            IconLeftWidget:
                                icon: 'cog-outline'        
                
"""


class CR(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "A700"
        screen = Builder.load_string(navigation_helper)
        return screen


CR().run()