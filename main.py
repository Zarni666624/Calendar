from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def f9(a, b, c):
    def f1():
        if a % 7 == 6:
            return "Friday"
        elif a % 7 == 0:
            return "Saturday"
        elif a % 7 == 1:
            return "Sunday"
        elif a % 7 == 2:
            return "Monday"
        elif a % 7 == 3:
            return "Tuesday"
        elif a % 7 == 4:
            return "Wednesday"
        elif a % 7 == 5:
            return "Thursday"

    def f2():
        if a % 7 == 0:
            return "Friday"
        elif a % 7 == 1:
            return "Saturday"
        elif a % 7 == 2:
            return "Sunday"
        elif a % 7 == 3:
            return "Monday"
        elif a % 7 == 4:
            return "Tuesday"
        elif a % 7 == 5:
            return "Wednesday"
        elif a % 7 == 6:
            return "Thursday"

    def f3():
        if a % 7 == 1:
            return "Friday"
        elif a % 7 == 2:
            return "Saturday"
        elif a % 7 == 3:
            return "Sunday"
        elif a % 7 == 4:
            return "Monday"
        elif a % 7 == 5:
            return "Tuesday"
        elif a % 7 == 6:
            return "Wednesday"
        elif a % 7 == 0:
            return "Thursday"

    def f4():
        if a % 7 == 2:
            return "Friday"
        elif a % 7 == 3:
            return "Saturday"
        elif a % 7 == 4:
            return "Sunday"
        elif a % 7 == 5:
            return "Monday"
        elif a % 7 == 6:
            return "Tuesday"
        elif a % 7 == 0:
            return "Wednesday"
        elif a % 7 == 1:
            return "Thursday"

    def f5():
        if a % 7 == 3:
            return "Friday"
        elif a % 7 == 4:
            return "Saturday"
        elif a % 7 == 5:
            return "Sunday"
        elif a % 7 == 6:
            return "Monday"
        elif a % 7 == 0:
            return "Tuesday"
        elif a % 7 == 1:
            return "Wednesday"
        elif a % 7 == 2:
            return "Thursday"

    def f6():
        if a % 7 == 4:
            return "Friday"
        elif a % 7 == 5:
            return "Saturday"
        elif a % 7 == 6:
            return "Sunday"
        elif a % 7 == 0:
            return "Monday"
        elif a % 7 == 1:
            return "Tuesday"
        elif a % 7 == 2:
            return "Wednesday"
        elif a % 7 == 3:
            return "Thursday"

    def f7():
        if a % 7 == 5:
            return "Friday"
        elif a % 7 == 6:
            return "Saturday"
        elif a % 7 == 0:
            return "Sunday"
        elif a % 7 == 1:
            return "Monday"
        elif a % 7 == 2:
            return "Tuesday"
        elif a % 7 == 3:
            return "Wednesday"
        elif a % 7 == 4:
            return "Thursday"

    if b == 1:
        if c % 28 == 1 or c % 28 == 7 or c % 28 == 18 or c % 28 == 24:
            return f1()
        elif c % 28 == 6 or c % 28 == 12 or c % 28 == 17 or c % 28 == 23:
            return f2()
        elif c % 28 == 0 or c % 28 == 5 or c % 28 == 11 or c % 28 == 22:
            return f3()
        elif c % 28 == 10 or c % 28 == 16 or c % 28 == 21 or c % 28 == 27:
            return f4()
        elif c % 28 == 4 or c % 28 == 9 or c % 28 == 15 or c % 28 == 26:
            return f5()
        elif c % 28 == 3 or c % 28 == 14 or c % 28 == 20 or c % 28 == 25:
            return f6()
        elif c % 28 == 2 or c % 28 == 8 or c % 28 == 13 or c % 28 == 19:
            return f7()
    elif b == 2:
        if c % 28 == 10 or c % 28 == 16 or c % 28 == 21 or c % 28 == 27:
            return f1()
        elif c % 28 == 4 or c % 28 == 9 or c % 28 == 15 or c % 28 == 26:
            return f2()
        elif c % 28 == 3 or c % 28 == 14 or c % 28 == 20 or c % 28 == 25:
            return f3()
        elif c % 28 == 2 or c % 28 == 8 or c % 28 == 13 or c % 28 == 19:
            return f4()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 18 or c % 28 == 24:
            return f5()
        elif c % 28 == 6 or c % 28 == 12 or c % 28 == 17 or c % 28 == 23:
            return f6()
        elif c % 28 == 0 or c % 28 == 5 or c % 28 == 11 or c % 28 == 22:
            return f7()
    elif b == 3 or b == 11:
        if c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f1()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f2()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f3()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f4()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f5()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f6()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f7()
    elif b == 4 or b == 7:
        if c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f1()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f2()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f3()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f4()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f5()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f6()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f7()
    elif b == 5:
        if c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f1()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f2()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f3()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f4()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f5()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f6()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f7()
    elif b == 6:
        if c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f1()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f2()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f3()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f4()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f5()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f6()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f7()
    elif b == 8:
        if c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f1()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f2()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f3()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f4()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f5()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f6()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f7()
    elif b == 9 or b == 12:
        if c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f1()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f2()
        elif c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f3()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f4()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f5()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f6()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f7()
    elif b == 10:
        if c % 28 == 1 or c % 28 == 7 or c % 28 == 12 or c % 28 == 18:
            return f1()
        elif c % 28 == 0 or c % 28 == 6 or c % 28 == 17 or c % 28 == 23:
            return f2()
        elif c % 28 == 5 or c % 28 == 11 or c % 28 == 16 or c % 28 == 22:
            return f3()
        elif c % 28 == 4 or c % 28 == 10 or c % 28 == 21 or c % 28 == 27:
            return f4()
        elif c % 28 == 9 or c % 28 == 15 or c % 28 == 20 or c % 28 == 26:
            return f5()
        elif c % 28 == 3 or c % 28 == 8 or c % 28 == 14 or c % 28 == 25:
            return f6()
        elif c % 28 == 2 or c % 28 == 13 or c % 28 == 19 or c % 28 == 24:
            return f7()


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tex1 = TextInput(hint_text="Day Number:", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.7}, multiline=False)
        self.tex2 = TextInput(hint_text="Month Number:", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.6}, multiline=False)
        self.tex3 = TextInput(hint_text="Year:", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.5}, multiline=False)
        self.labe = Label(text="",color="lightslategray", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn = Button(text="Click Me!", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn.bind(on_press=self.third)
        self.add_widget(self.tex1)
        self.add_widget(self.tex2)
        self.add_widget(self.tex3)
        self.add_widget(self.labe)
        self.add_widget(btn)

    def third(self, obj):
        try:
            data1 = self.tex1.text
            data2 = self.tex2.text
            data3 = self.tex3.text
            if f9(int(data1), int(data2), int(data3)) == None:
                raise Exception("")
            self.labe.text=f9(int(data1), int(data2), int(data3))
        except:
            self.labe.text = "Error"
class CalendarApp(App):
    pass
CalendarApp().run()