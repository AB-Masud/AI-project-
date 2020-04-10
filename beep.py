import os
def beep(sec):
 for i in range(sec):
  os.system('say Good morning Friends')
 return
if _name_ == '_main_':
 beep(5)
