try:
 import Tkinter
 import ttk
except:
 import tkinter as Tkinter
 import tkinter.ttk as ttk
import datetime
import beep
import os


class Clock(Tkinter.Tk):
 def _init_(self, *args, **kwargs):
  Tkinter.Tk._init_(self, *args, **kwargs)
  self['padx']=20
  self['pady']=20
  # Creating Variables
  self.waiting_string_variable = Tkinter.IntVar()
  self.show_alarm_time = Tkinter.StringVar()
  self.show_alarm_time.set(datetime.datetime.now().ctime())
  self.alarm_delta_time = None
  self.create_first_label()
  self.create_second_box()


 def create_first_label(self):
  ttk.Label(self, textvariable=self.show_alarm_time, font = ("arial 20 bold")).grid(row=0, column=1, columnspan=2, padx=10,pady=10)
  return

 def create_second_box(self):
  ttk.Label(self, text="Wait For Seconds : ").grid(row=1, column=1, padx=10,pady=10)
  ttk.Entry(self, textvariable = self.waiting_string_variable).grid(row=1, column=2, padx=10,pady=10)
  ttk.Button(self, text="Exit", command=self.destroy).grid(row=3, column=1, padx=10,pady=10)
  ttk.Button(self, text="Set Alarm!", command=self.set_alarm_button).grid(row=3, column=2, padx=10,pady=10)
  return


 def set_alarm_button(self):
  try:
   sec = self.waiting_string_variable.get()
   self.alarm_delta_time = datetime.datetime.now()+datetime.timedelta(seconds=sec)
   self.show_alarm_time.set(self.alarm_delta_time.ctime()._str_())
  except:
   self.waiting_string_variable.set(0)
  return


 def regular_update(self):
  self.update()
  self.update_idletasks()
  if self.alarm_delta_time:
   if datetime.datetime.now() > self.alarm_delta_time:
    beep.beep(5)


  return


def main():
 root = Clock(className = " Simple Alram Clock  ")
 while True:
  root.regular_update()
 return


if _name_ == '_main_':
 main()
