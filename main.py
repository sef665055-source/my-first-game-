import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# تحديد مقاس الشاشة على الكمبيوتر كأنها شاشة موبايل للتجربة
Window.size = (360, 640)

class GuessingGameApp(App):
    def build(self):
        self.limit = 10
        self.secret_number = random.randint(1, self.limit)
        
        # التصميم الرئيسي (عمودي فوق بعضه)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # الخلفية غامقة ومريحة للعين
        Window.clearcolor = (0.17, 0.24, 0.31, 1)
        
        # العناوين والنصوص
        self.title_label = Label(text="Road to 1000! 🏆", font_size='28sp', bold=True, color=(0.95, 0.77, 0.06, 1))
        self.level_label = Label(text=f"⭐ LEVEL: 1 to {self.limit}", font_size='18sp', bold=True)
        self.hint_label = Label(text="Enter your guess below:", font_size='14sp', color=(0.74, 0.76, 0.78, 1))
        
        # مكان كتابة الرقم (مخصص للموبايل)
        self.guess_input = TextInput(text='', font_size='24sp', halign='center', input_filter='int', multiline=False)
        
        # زرار التخمين
        self.submit_btn = Button(text="Check Guess 🎯", font_size='18sp', bold=True, background_color=(0.15, 0.68, 0.38, 1))
        self.submit_btn.bind(on_press=self.check_guess)
        
        # خانة النتيجة
        self.result_label = Label(text="Good Luck! 👍", font_size='16sp', bold=True, color=(0.9, 0.49, 0.13, 1))
        
        # إضافة كل العناصر للشاشة
        layout.add_widget(self.title_label)
        layout.add_widget(self.level_label)
        layout.add_widget(self.hint_label)
        layout.add_widget(self.guess_input)
        layout.add_widget(self.submit_btn)
        layout.add_widget(self.result_label)
        
        return layout

    def check_guess(self, instance):
        if not self.guess_input.text:
            self.result_label.text = "❌ Please enter a number!"
            return
            
        guess = int(self.guess_input.text)
        
        if guess == self.secret_number:
            if self.limit < 100:
                self.limit += 10
            elif self.limit < 1000:
                self.limit += 100
            else:
                self.result_label.text = "👑 VICTORY!! YOU BEAT THE GAME! 🏆"
                return
                
            self.secret_number = random.randint(1, self.limit)
            self.level_label.text = f"⭐ LEVEL: 1 to {self.limit}"
            self.result_label.text = "🎉 Correct! New level unlocked! 🎉"
            self.result_label.color = (0.18, 0.8, 0.44, 1)
        elif guess < self.secret_number:
            self.result_label.text = "❌ WRONG! Try a HIGHER number ⬆️"
            self.result_label.color = (0.91, 0.3, 0.24, 1)
        else:
            self.result_label.text = "❌ WRONG! Try a LOWER number ⬇️"
            self.result_label.color = (0.91, 0.3, 0.24, 1)
            
        self.guess_input.text = ''

if __name__ == '__main__':
    GuessingGameApp().run()
