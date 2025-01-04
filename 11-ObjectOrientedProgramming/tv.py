class TV:
   def __init__(self):
      self.channel_no = 1
      self.is_on = False
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def channel_change(self,channel):
      self.channel_no = channel
   def show_status(self):
      print(f"TV is {'on' if self.is_on else 'off'}")
      if self.is_on == True:
         print(f"Channel: {self.channel_no}")