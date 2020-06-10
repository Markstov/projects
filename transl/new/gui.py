from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers.pascal import DelphiLexer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
import translator as tr

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 700)

class MyApp(App):
  checker3 = 0
  def print_text(self, instance):
    mass = self.ci.text.split('\n')
    self.lbl.text =''
    for i in mass:
      print(i)
      checker = tr.func_main(i, '')
      self.lbl.text +=checker+'\n'
    print(mass)
  def print_tables(self, instance):
    self.lbl1.text = ""
    if self.checker3 == 0:
      self.lbl1.text = "Служебные слова:" + "\n"
      for i in tr.tableSLU:
        self.lbl1.text +="W" + str(tr.tableSLU.index(i)) + " = " + i + '\n'
      self.checker3+=1
    elif self.checker3 == 1:
      self.lbl1.text = "Разделители:" + "\n"
      for i in tr.tableR:
        self.lbl1.text +="R" + str(tr.tableR.index(i)) + " = " + i + '\n'
      self.checker3+=1
    elif self.checker3 == 2:
      self.lbl1.text = "Идентификаторы:" + "\n"
      for i in tr.tableID:
        self.lbl1.text +="I" + str(tr.tableID.index(i)) + " = " + i + '\n'
      self.checker3+=1
    elif self.checker3 == 3:
      self.lbl1.text = "Числовые константы:" + "\n"
      for i in tr.tableCONST:
        self.lbl1.text +="N" + str(tr.tableCONST.index(i)) + " = " + i + '\n'
      self.checker3+=1
    elif self.checker3 == 4:
      self.lbl1.text = "Операции:" + "\n"
      for i in tr.tableO:
        self.lbl1.text +="O" + str(tr.tableO.index(i)) + " = " + i + '\n'
      self.checker3+=1
    elif self.checker3 == 5:
      self.lbl1.text = "Строковые константы:" + "\n"
      for i in tr.tableC:
        self.lbl1.text +="C" + str(tr.tableC.index(i)) + " = " + i + '\n'
      self.checker3=0
      
  def build(self):
    al = AnchorLayout(anchor_x = "center", anchor_y = "center", size_hint = (1,.2))
    bl = BoxLayout(orientation = 'vertical')
    bl2 = BoxLayout(orientation = 'vertical')
    bl1 = BoxLayout(orientation = 'horizontal')
    bl3 = BoxLayout(orientation = 'horizontal', size_hint = (1,.2))
    self.lbl1 = Label(valign="top",text_size = (400,700*.8))
    
    self.lbl = Label(valign="top",text_size = (400,700*.8))
    self.ci = CodeInput(lexer = DelphiLexer())
    bl1.add_widget(self.ci)
    bl1.add_widget(self.lbl)
    bl1.add_widget(self.lbl1)
    bl.add_widget(bl1)
    bl3.add_widget(Button(text = "Трансформировать", on_press = self.print_text))
    bl3.add_widget(Button(text = "Далее", on_press = self.print_tables))
    bl.add_widget(bl3)
    
    return  bl
    
  pass

if __name__ == "__main__":
    MyApp().run()