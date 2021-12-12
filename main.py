from kivy.core.window import Window
from kivy.lang import Builder  # Импортируем функциональность консруктора
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.picker import MDThemePicker
import plyer
from kivy.clock import Clock
from kivymd.uix.picker import MDTimePicker
import datetime
import pygame

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
                        title: 'Рекомендации'
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
                MDFloatLayout:
                    orientation: "vertical"
                    MDToolbar:
						pos_hint: {'top': 1}
                        title: "Напоминалка"
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
					MDIconButton:
						icon: "plus"
						pos_hint: {"center_x": .87, "center_y": .84}
						md_bg_color: 0, 0, 0, 0
						text_color: 1, 1, 1, 1
						on_release: app.time_picker()
					MDLabel:
						id: alarm_time
						text: ""
						pos_hint: {"center_y": .5}
						halign: "center"
						font_size: "30sp"
						bold: True
					MDRaisedButton:
						text: "Stop"
						pos_hint: {"center_x": .5, "center_y": .400}
						on_release: app.stop()
						
            MDScreen:
                name: 'screen 3'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'О Covid-19'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text:'Заразиться новым коронавирусом (COVID-19) могут представители всех возрастных категорий.'
                            OneLineListItem:
                                text:'Животные – кошки, собаки, хомяки и прочие – не могут быть источником Covid-19'
                            OneLineListItem:
                                text:'Насекомые также не могут быть источником Covid-19'
                            OneLineListItem:
                                text:'Употребление дезинфицирующих средств не предотвращает и не лечит COVID-19'
                            OneLineListItem:
                                text:'Антибиотики против вирусов не действуют, но позволяют лечить бактериальные инфекции.'
                            OneLineListItem:
                                text:'Добавление в пищу перца и других острых приправ также не предотвращает и не лечит COVID-19.'

            MDScreen:
                name: 'screen 4'
                MDFloatLayout:
                    orientation: "vertical"
                    MDToolbar:
						pos_hint: {'top': 1}
                        title: "Настройки"
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    MDRaisedButton:
                        text: "Выбор темы"
                    	icon: "format-color-fill"
						pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: app.show_theme_picker()
            MDScreen:
                name: 'screen 5'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Использование масок'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 1'
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
                        title: 'Здоровье дома'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 1'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text: 'Как убираться дома'
                                on_release:manager.current = 'screen 12'
                            OneLineListItem:
                                text: 'Как не принести вирусы с улицы'
                                on_release:manager.current = 'screen 13'
                            OneLineListItem:
                                text: 'Как покупать продукты'
                                on_release:manager.current = 'screen 14'
            MDScreen:
                name: 'screen 7'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Элементарные правила гигиены'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 1'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text: 'Мойте руки'
                            OneLineListItem:
                                text: 'Прикрывайте рот при кашле или чихании'
                            OneLineListItem:
                                text: 'Соблюдайте психологическую гигиену'
                            OneLineListItem:
                                text: 'Правильно питайтесь и принимайте витамины.'
                            OneLineListItem:
                                text: 'Достаточно отдыхайте :).'
            MDScreen:
                name: 'screen 12'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Как убираться дома'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 6'

                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text: '1.  Влажную уборку нужно проводить 2–3 раза в неделю и регулярно проветривать помещения.'
                            OneLineListItem:
                                text: '2.  Во время уборки важно не забывать протирать ручки дверей,шкафов и тд.'
                            OneLineListItem:
                                text: '3.  Роспотребнадзор предписывает использовать мыло или салфетки с антисептиком. '
                            OneLineListItem:
                                text: '4.  Пульты и клавиатуры можно поместить в пакеты, так будет проще держать их в чистоте. '
                            OneLineListItem:
                                text: '5.  Не забывайте обрабатывать телефон, так как он нас сопровождает практически всюду. '
            MDScreen:
                name: 'screen 13'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Как не принести вирусы с улицы'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 6'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text: '1.  Нужно соблюдать дистанцию не меньше 2 м, мыть руки после улицы, не трогать лицо.'
                            OneLineListItem:
                                text: '2.  Использование резиновых перчаток для защиты от вируса ВОЗ считает нецелесообразным.'
                            OneLineListItem:
                                text: '3.  Использовать маску не более 2-3 часов.'
            MDScreen:
                name: 'screen 14'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Как покупать продукты'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                        MDIconButton:
                            icon: "arrow-left"
                            user_font_size: "40sp"
                            on_release: manager.current = 'screen 6'
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text: '1.  Заказывать бесконтактную доставку с предоплатой на сайте.'
                            OneLineListItem:
                                text: '2.  Мыть овощи и фрукты с антисептиками, мылом и другими средствами не рекомендуется.'
                            OneLineListItem:
                                text: '3.  Можно пересыпать продукты в домашние емкости для хранения.'

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
                                MDIconButton:
                                    icon: "arrow-left"
                                    user_font_size: "40sp"
                                    on_release: manager.current = 'screen 5'
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
                                MDIconButton:
                                    icon: "arrow-left"
                                    user_font_size: "40sp"
                                    on_release: manager.current = 'screen 5'
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

	pygame.init()
	sound = pygame.mixer.Sound("alarm.mp3")
	volume = 0

	def build(self):
		screen = Builder.load_string(navigation_helper)
		return screen

	def time_picker(self):
		time_dialog = MDTimePicker()
		time_dialog.bind(time=self.get_time, on_save=self.schedule)
		time_dialog.open()

	def schedule(self, *args):
		Clock.schedule_once(self.alarm, 1)

	def alarm(self, *args):
		Clock.schedule_interval(self.update, 1)

	def update(self, dt):
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		if self.root.ids.alarm_time.text == str(current_time):
			self.start()

	def set_volume(self, *args):
		self.volume += 0.05
		if self.volume < 1.0:
			Clock.schedule_interval(self.set_volume, 10)
			self.sound.set_volume(self.volume)
			print(self.volume)
		else:
			self.sound.set_volume(1)
			print("Max")

	def start(self, *args):
		self.sound.play(-1)
		self.set_volume()
		plyer.notification.notify(title='CoronaReminder', message="Не забывайте о мерах по профилактике COVID-19!")

	def stop(self):
		self.sound.stop()
		Clock.unschedule(self.set_volume)
		self.volume = 0

	def get_time(self, instance, time):
		self.root.ids.alarm_time.text = str(time)

	def show_theme_picker(self):
		theme_dialog = MDThemePicker()
		theme_dialog.open()

	class ContentNavigationDrawer(BoxLayout):
		manager = ObjectProperty()
		nav_drawer = ObjectProperty()

	class DrawerList(ThemableBehavior, MDList):
		pass

if __name__ == '__main__':
	plyer.notification.notify(title='Приветствуем!', message="Спасибо за выбор нашего приложения!")

CR().run()
