class TrafficLight:
    def running(self):
        __color = True
        import time
        __color = "RED! "
        print("The signal is: ", __color)
        print(__color * 7)
        for i in range(7,0,-1):
            print("wait",i,"sec.")
            time.sleep(1)
        color = "YELLOW! "
        print("The signal is: ", __color, "\nwait 2 secs")
        print(__color*7)
        time.sleep(2)
        color = "GREEN! "
        print("The signal is: ", __color, "\nwait 2 secs")
        print(__color * 7)
        time.sleep(2)

signal = TrafficLight()
signal.running()