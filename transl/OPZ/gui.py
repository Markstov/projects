from tkinter import *  
from tkinter import ttk
from tkinter import scrolledtext
import controller as ctrl
import translator as tr

def clop():
  txt1.delete(1.0,END)
  txt2.delete(1.0,END)
  txt3.delete(1.0,END)
  txc.delete(1.0,END)
  txn.delete(1.0,END)
  txin.delete(1.0,END)
  txw.delete(1.0,END)
  txr.delete(1.0,END)
  txo.delete(1.0,END)
  mass = txt.get(1.0,END)
  mass = mass.replace("\t","").split('\n')
  txt1.insert(1.0,ctrl.changer_text(mass))
  txt2.insert(1.0,ctrl.take_OPZ())
  txt3.insert(1.0,ctrl.assemb_trans())
  
  sw =''
  for i in tr.tableSLU:
    sw +="W" + str(tr.tableSLU.index(i)) + " = " + i + '\n'
  txw.insert(1.0,sw)

  sr =''
  for i in tr.tableR:
    sr +="R" + str(tr.tableR.index(i)) + " = " + i + '\n'
  txr.insert(1.0,sr)

  si = ''
  for i in tr.tableID:
    si +="I" + str(tr.tableID.index(i)) + " = " + i + '\n'
  txin.insert(1.0,si)

  sn = ''
  for i in tr.tableCONST:
    sn +="N" + str(tr.tableCONST.index(i)) + " = " + i + '\n'
  txn.insert(1.0, sn)

  so =''
  for i in tr.tableO:
    so +="O" + str(tr.tableO.index(i)) + " = " + i + '\n'
  txo.insert(1.0,so)

  sc = ''
  for i in tr.tableC:
    sc +="C" + str(tr.tableC.index(i)) + " = " + i + '\n'
  txc.insert(1.0,sc)


window = Tk()  
window.title("Транслятор")  
window.geometry('1600x800')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Транслятор')  
tab_control.add(tab2, text='Лексемы')  


lbl1 = Label(tab1, text='Исходный код')
lbl1.grid(column=0, row=0)
txt = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt.grid(column=0, row=1)

btn1 = Button(tab1, text="Start", command=clop)
btn1.grid(column=0, row=2)
 

lbl2 = Label(tab1, text='Результат')  
lbl2.grid(column=1, row=0)
txt1 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt1.grid(column=1, row=1)

lbl3 = Label(tab1, text='ОПЗ')  
lbl3.grid(column=2, row=0)
txt2 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt2.grid(column=2, row=1)

lbl4 = Label(tab1, text='Assembler')  
lbl4.grid(column=3, row=0)
txt3 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt3.grid(column=3, row=1)


lbo = Label(tab2, text='Операции')  
lbo.grid(column=0, row=0)
txo = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txo.grid(column=0, row=1)


lbr = Label(tab2, text='Разделители')  
lbr.grid(column=1, row=0)
txr = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txr.grid(column=1, row=1)


lbw = Label(tab2, text='Команды')  
lbw.grid(column=2, row=0)
txw = scrolledtext.ScrolledText(tab2, width=20, height=40)  
txw.grid(column=2, row=1)


lbin = Label(tab2, text='Идентификаторы')  
lbin.grid(column=3, row=0)
txin = scrolledtext.ScrolledText(tab2, width=20, height=40)  
txin.grid(column=3, row=1)


lbn = Label(tab2, text='Числовые константы')  
lbn.grid(column=4, row=0)
txn = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txn.grid(column=4, row=1)


lbc = Label(tab2, text='Текстовые константы')  
lbc.grid(column=5, row=0)
txc = scrolledtext.ScrolledText(tab2, width=25, height=40)  
txc.grid(column=5, row=1)


tab_control.pack(expand=1, fill='both')  
window.mainloop()


# class MyApp(App):
#   checker3 = 0
#   def print_text(self, instance):
  #   mass = self.ci.text.replace("\t","").split('\n')
#     self.lbl.text =''
#     self.lbl.text = "Синтаксический анализ: \n"+ctrl.changer_text(mass)
    
      
    
#   def print_OPZ(self, instance):
#     self.lbl.text = "Обратная польская запись: \n"+ctrl.take_OPZ()
#   def assembler_text(self, instance):
#     self.lbl.text = "Программа на языке ассемблер: \n"+ctrl.assemb_trans()
#   def print_tables(self, instance):
#     self.lbl1.text = ""
#     if self.checker3 == 0:
#       self.lbl1.text = "Служебные слова:" + "\n"
#       for i in tr.tableSLU:
#         self.lbl1.text +="W" + str(tr.tableSLU.index(i)) + " = " + i + '\n'
#       self.checker3+=1
#     elif self.checker3 == 1:
#       self.lbl1.text = "Разделители:" + "\n"
#       for i in tr.tableR:
#         self.lbl1.text +="R" + str(tr.tableR.index(i)) + " = " + i + '\n'
#       self.checker3+=1
#     elif self.checker3 == 2:
#       self.lbl1.text = "Идентификаторы:" + "\n"
#       for i in tr.tableID:
#         self.lbl1.text +="I" + str(tr.tableID.index(i)) + " = " + i + '\n'
#       self.checker3+=1
#     elif self.checker3 == 3:
#       self.lbl1.text = "Числовые константы:" + "\n"
#       for i in tr.tableCONST:
#         self.lbl1.text +="N" + str(tr.tableCONST.index(i)) + " = " + i + '\n'
#       self.checker3+=1
#     elif self.checker3 == 4:
#       self.lbl1.text = "Операции:" + "\n"
#       for i in tr.tableO:
#         self.lbl1.text +="O" + str(tr.tableO.index(i)) + " = " + i + '\n'
#       self.checker3+=1
#     elif self.checker3 == 5:
#       self.lbl1.text = "Строковые константы:" + "\n"
#       for i in tr.tableC:
#         self.lbl1.text +="C" + str(tr.tableC.index(i)) + " = " + i + '\n'
#       self.checker3=0
      
#   def build(self):
    
#     bl = BoxLayout(orientation = 'vertical')
    
#     bl1 = BoxLayout(orientation = 'horizontal')
#     bl3 = BoxLayout(orientation = 'horizontal', size_hint = (1,.2))
#     self.lbl1 = Label(valign="top",text_size = (400,700*.8))
    
#     self.lbl = Label(valign="top",text_size = (400,700*.8))
#     self.ci = CodeInput(lexer = DelphiLexer())
#     bl1.add_widget(self.ci)
#     bl1.add_widget(self.lbl)
#     bl1.add_widget(self.lbl1)
#     bl.add_widget(bl1)
#     bl3.add_widget(Button(text = "Трансформировать", on_press = self.print_text))
#     bl3.add_widget(Button(text = "ОПЗ", on_press = self.print_OPZ))
#     bl3.add_widget(Button(text = "Ассемблер", on_press = self.assembler_text))
#     bl3.add_widget(Button(text = "Далее", on_press = self.print_tables))
    
#     bl.add_widget(bl3)
    
#     return  bl
    
#   pass

# if __name__ == "__main__":
#     MyApp().run()