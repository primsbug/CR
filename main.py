from kivy.core.window import Window
from kivy.lang import Builder  # Импортируем функциональность консруктора
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel  # импортируем метки
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.picker import MDThemePicker

Window.size = (300, 500)  # Устанавливаем размеры экрана под мобильное устройство

Virus = """
Image:
    source: 'CoronaV.jpg'
"""

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            id: manager

            MDScreen:
                name: 'screen 0'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'CoronaReminder'
                        font_style: 'subtitle1'
                        elevation: 12
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                    Widget:

            MDScreen:
                name: 'screen 1'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Окно1'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            TwoLineListItem:
                                text: '1. Ношение масок'
                                secondary_text: '[О масках в условиях COVID-19]'
                                on_release: manager.current = 'screen 5'
                            TwoLineListItem:
                                text: '2. Здоровье дома'
                                secondary_text: '[#HealthyAtHome]'
                                on_release: manager.current = 'screen 6'
                            TwoLineListItem:
                                text: '3. Гигиена'
                                on_release: manager.current = 'screen 7'
                                secondary_text: '[Элементарные правила гигиены]'

            MDScreen:
                name: 'screen 2'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Окно2'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            Button:
                                text: '0'

            MDScreen:
                name: 'screen 3'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'О covid-19'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            TwoLineListItem:
                                text: '1'
                                secondary_text: '[Recent text here]'

            MDScreen:
                name: 'screen 4'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Настройки'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            MDFillRoundFlatIconButton:
                                text: "Выбор темы"
                                icon: "format-color-fill"
                                pos_hint: {"center_x": .5}
                                on_release: 
                                    app.show_theme_picker()

            MDScreen:
                name: 'screen 5'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'О масках в условиях COVID-19'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            OneLineListItem:
                                text: 'What have you forgotten here?'
                            OneLineListItem:
                                text: 'There is nothing to see here :('

            MDScreen:
                name: 'screen 6'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: '#HealthyAtHome'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            OneLineListItem:
                                text: 'What have you forgotten here?'
                            OneLineListItem:
                                text: 'There is nothing to see here :('

            MDScreen:
                name: 'screen 7'

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Элементарные правила гигиены'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    ScrollView:

                        MDList:
                            OneLineListItem:
                                text: 'What have you forgotten here?'
                            OneLineListItem:
                                text: 'There is nothing to see here :('

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '1dp'
                padding: '8dp'

                Button: # Теперь при нажатии на картинку CoronaV осуществляется переход на начальный экран (необязательно к применению)
                    size_hint: None, None
                    size: '225dp', '120dp'
                    y: self.parent.y
                    x: self.parent.x
                    background_color:(1, 1, 1, 0)
                    on_release: 
                        manager.current = 'screen 0'
                        nav_drawer.set_state("close")
                    Image:
                        id: Corona
                        size_hint: None, None
                        size: '225dp', '120dp'
                        source: 'CoronaV.jpg'
                        y: self.parent.y
                        x: self.parent.x
                        allow_stretch: True
                MDLabel:
                    text: '  workadsupp@mail.ru'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]   


                ScrollView:

                    MDList:
                        OneLineIconListItem:  # Добавил вкладку "На главную" при нажатии на которую происходит переход на начальный экран
                            text: 'На главную'
                            on_release: 
                                manager.current = 'screen 0' 
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'arrow-left-thick'
                        OneLineIconListItem:
                            text: 'Рекомендации'
                            on_release: 
                                manager.current = 'screen 1'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'information'
                        OneLineIconListItem:
                            text: 'Напоминалка'
                            on_release: 
                                manager.current = 'screen 2'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'alarm-check'
                        OneLineIconListItem:
                            text: 'О Covid-19'
                            on_release: 
                                manager.current = 'screen 3'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'flask-round-bottom'
                        OneLineIconListItem:
                            text: 'Настройки'
                            on_release: 
                                manager.current = 'screen 4'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'cog-outline'        

"""


class CR(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        manager = ObjectProperty()
        nav_drawer = ObjectProperty()

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def on_start(self):
        pass


CR().run()
