
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder



class ConvertidorTemperatura(BoxLayout):

    def convertir_temperatura(self, valor):
        fahrenheit = (valor * 9 / 5) + 32

        self.ids.lbl_celsius.text = f"Temperatura: {valor:.0f} °C"
        self.ids.lbl_fahrenheit.text = f"Equivale a: {fahrenheit:.0f} °F"


class TemperaturaApp(App):

    def build(self):
        Builder.load_file("interfaz.kv")
        return ConvertidorTemperatura()


TemperaturaApp().run()




