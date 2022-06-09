from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window


Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (360, 640)


class Container(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Ошибка"


class CalculatorApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Calculator"
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Container()


if __name__ == "__main__":
    CalculatorApp().run()