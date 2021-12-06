from kivy.core.window import Window
from kivy.lang import Builder  # Импортируем функциональность консруктора
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel  # импортируем метки
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.picker import MDThemePicker
from kivy.utils import platform
import plyer

Window.size = (800, 600)  # Устанавливаем размеры экрана

Virus = """
Image:
    source: 'Corona.jpg'
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
                                text: '1. Использование масок'
                                on_release: manager.current = 'screen 5'
                            TwoLineListItem:
                                text: '2. Здоровье дома'
                                on_release: manager.current = 'screen 6'
                            TwoLineListItem:
                                text: '3. Гигиена'
                                on_release: manager.current = 'screen 7'
            MDScreen:
                name: 'screen 2'
                BoxLayout:
                    id: box
                    orientation: "vertical"
                    spacing: 15

                    MDToolbar:
                        title: "Напоминалка"
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10

                    MDRaisedButton:
                        id: mybutton
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        text: "Отправить уведомление"
                        on_press: app.button_pressed()

                    MDLabel:
                        id: mylabel
                        halign: "center"
                        text: ""
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
                                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                                on_release: app.show_theme_picker()
            MDScreen:
                name: 'screen 5'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Использование масок'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    ScrollView:
                        MDList:
                            TwoLineListItem:
                                text: '1. Меняйте маски каждые 2-3 часа '
                                secondary_text: 'Как правильно надеть/снять маску.'
                                on_release: manager.current = 'screen 10'
                            ThreeLineListItem:
                                text: '2. При повторном использовании многоразовой маски, необходима обработка '
                                secondary_text: 'В домашних условиях маску нужно выстирать с мылом или моющим средством, затем обработать'
                                tertiary_text: 'с помощью парогенератора или утюга с функцией подачи пара.'
                            TwoLineListItem:
                                text: '3. При повторном использовании многоразовой маски, необходима обработка '
                            TwoLineListItem:
                                text: '2. Маски эффективны только в сочетании с другими методами профилактики ' 
                                secondary_text: 'Избегайте контатков, часще мойте руки, дезинфецируйте предметы.'   
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
            
            MDScreen:
                name: 'screen 10'              
                MDBottomNavigation:
                    text_color_active: 0, 0, 0, 1
                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Как правильно надеть маску'
                        icon: 'face-mask'
                        badge_icon: "numeric-10"
                        
                        MDBoxLayout:
                            orientation: 'vertical'
                            MDToolbar:
                                title: 'Как правильно надеть маску'
                                left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                                elevation: 10
                            ScrollView:
                                MDList:
                                    OneLineListItem:
                                        text: '1.  Вымойте руки с мылом или воспользуйтесь спиртовым антисептиком, прежде чем прикасаться к маске.'
                                    OneLineListItem:
                                        text: '2.  Достаньте маску и убедитесь, что на ней нет повреждений.'
                                    OneLineListItem:
                                        text: '3.  Определите верхнюю сторону маски: это та, в которую вшит гибкий зажим для носа.'
                                    OneLineListItem:
                                        text: '4.  Определите наружную сторону маски: обычно она цветная, в то время как внутренняя сторона — белая.'
                                    OneLineListItem:
                                        text: '5.  Поочередно наденьте маску на уши, держа её за петли'
                                    OneLineListItem:
                                        text: '6.  Сомните верхний край маски по форме носа.'
                                    OneLineListItem:
                                        text: '7.  Натяните маску на рот и подбородок.' 

                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'Как правильно снять маску'
                        icon: 'face-mask'
                        badge_icon: "numeric-10"
                        
                        MDBoxLayout:
                            orientation: 'vertical'
                            MDToolbar:
                                title: 'Как правильно снять маску'
                                left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                                elevation: 10
                            ScrollView:
                                MDList:
                                    OneLineListItem:
                                        text: '1.  Вымойте руки с мылом или воспользуйтесь антисептиком, прежде чем прикасаться к маске.'
                                    TwoLineListItem:
                                        text: '2.  Не касайтесь наружной части маски, она грязная.'
                                        secondary_text: 'Дотрагивайтесь только до резиночек, которыми она крепится к голове.'
                                    OneLineListItem:
                                        text: '3.  Сложите маску вдвое, выбросьте ее в мусорку и протрите их спиртовым антисептиком.'                                      
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
                        source: 'Corona.jpg'
                        y: self.parent.y
                        x: self.parent.x
                        allow_stretch: True
                MDLabel:
                    text: '        workadsupp@mail.ru'
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
        if platform == 'android':
            from jnius import autoclass
            service = autoclass('org.test.myapp.ServiceMyservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(mActivity, argument)
            label = self.root.ids.mylabel
            label.text += "\nservice started"

    def button_pressed(self):
        import plyer
        plyer.notification.notify(title='CoronaReminder', message="Не забывайте о мерах по профилактике COVID-19!")
        label = self.root.ids.mylabel
        label.text += "\nУведомление отправлено"


if __name__ == '__CR__':
    plyer.notification.notify(title='BackgroundService Test', message="Notification from android service")

CR().run()
