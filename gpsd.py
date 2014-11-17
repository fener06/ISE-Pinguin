#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')
 		fo = open("foo.txt", "wb")
   		fo.write(  \n' GPS reading' \n '----------------------------------------' 
    	  		\n 'latitude    ' , gpsd.fix.latitude
     		 	\n 'longitude   ' , gpsd.fix.longitude
      			\n 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
  			    \n 'altitude (m)' , gpsd.fix.altitude
  			    \n 'eps         ' , gpsd.fix.eps
      			\n 'epx         ' , gpsd.fix.epx
      			\n 'epv         ' , gpsd.fix.epv
      			\n 'ept         ' , gpsd.fix.ept
      			\n 'speed (m/s) ' , gpsd.fix.speed
      			\n 'climb       ' , gpsd.fix.climb
      			\n 'track       ' , gpsd.fix.track
      			\n 'mode        ' , gpsd.fix.mode
	  			\n
  			    \n 'sats        ' , gpsd.satellites )
 
      time.sleep(5) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."