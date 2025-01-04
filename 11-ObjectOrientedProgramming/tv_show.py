from tv import TV

def main():
   # object creation
   my_tv = TV()
   my_tv.show_status()
   # object usage
   my_tv.turn_on()
   my_tv.show_status()

   my_tv.turn_off()
   my_tv.show_status()

if __name__ == "__main__":
   main() 