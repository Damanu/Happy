#/usr/bin/python
from optparse import OptionParser
import optparse
import argparse
from argparse import ArgumentParser
import os				
import datetime
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib 
import sys
#das i/o Getue geht so wie hier beschrieben: https://docs.python.org/2/tutorial/inputoutput.html
# supercoole Scientific software fuer Python: SciPy ... numpy und matplotlib sind da auch drinnen

#Definition um bash mit sh("script") aufuehren zu koennen

#def sh(script):
#    os.system("bash -c '%s'" % script)

#Dateipfad
path='/home/emanuel/Dropbox/Programmieren/Python/'

#path='/home/emanuel/Git/Hub/Happy/'
filename='TestData'
#filename='Daten_Happy'
config='Happy.config'

#if not(os.path.isfile(path+config)): 		#check if filename exitst in path , if not create it
 	
#filename='Daten_Happy_Eva'
#Parameter
now = datetime.datetime.now()
happy=-1		#subjektiv happines in % , 100% = very happy 
health=-1		#subjektiv health in % , 100%= very healthy
stress=-1		#          stress in % , 100%= much stress		
sporty=-1		#	   sportines % , 100%= very sporty
money=-1		# 	   money in %  , 100%= rich
social=-1		# 	   social contacts in % , 100% = a lot of

#vorlaufig, koennte was dazu kommen
def Input(option):	#Input programm , gibt eingegebene werte aus
	if option == "a": #option All --> alle Parameter werden angegeben
		while True:
			try:
				happy=raw_input("Gluecklichkeit (0 ist depressiv, 50 ist neutral, 100 ist euphorisch): ")
				if ((int(happy) >= 0) and (int(happy) <= 100)):
					break
			except ValueError:
				continue
		while True:
			try:
				health=raw_input("Gesundheit (0 ist TOT, 100 ist wie neu geboren): ")
				if ((int(health) >= 0) and (int(health) <= 100)):
					break
			except ValueError:
				continue
		while True:
			try:
				stress=raw_input("Stress (0 ohne irgendeine Verpflichtung, 50 Normalzustand, 100 burnout): " )
				if ((int(stress) >= 0) and (int(stress) <= 100)):
					break
			except ValueError:
				continue
		while True:
			try:
				sporty=raw_input("Sportlichkeit des Koerpers (0 keine zwei Stiegen schaffen, 50 alltagstauglich, 100 Maratontauglich): ")
				if ((int(sporty) >= 0) and (int(sporty) <= 100)):
					break
			except ValueError:
				continue
		while True:
			try:
				money=raw_input("Genug Geld (0 nicht fuer das Noetigste, 50 kein Luxus sonst alles, 100 weis nicht wo hin damit): ")
				if ((int(money) >= 0) and (int(money) <= 100)):
					break
			except ValueError:
				continue
		while True:
			try:
				social=raw_input("Soziale Kontakte (0 kein Kontakt zu irgendwem, 50 standard kontakte , 100 immer mit Freunden zusammen): ")
				if ((int(social) >= 0) and (int(social) <= 100)):
					break
			except ValueError:
				continue
		return(happy,health,stress,sporty,money,social)
	#elif option == b: #weitere Optionen folgen

def WriteData(datalist):		#ungetestet, geht wsl nicht
	text = open(path+filename,'r') #open file to read
	bis =text.read()		#save file to string
	text = open(path+filename,'w')	#open filen to write
	text.write(bis+"\n"+str(datalist[0])+" "+str(datalist[1])+" "+str(datalist[2])+" "+str(datalist[3])+" "+str(datalist[4])+" "+str(datalist[5])+" "+str(now.year)+" "+str(now.month)+" "+str(now.day)+" "+str(now.hour)+" "+str(now.minute)+" "+str(now.second))	#write data to file 

	
#Programm zum auslesen des Config files
def ReadConfig():
	text = open(path+Happy.config,'r')
	data = text.read()
#	print data
#Programm zum auslesen der Daten
#Ausgabe: endval[index], index: 0=happy,1=health,2=stress,3=sporty,4=money,5=social,6=year,7=month,8=day,9=hour,10=minute,11=second
def Read():
	try:
		text = open(path+filename,'r')	#open file to read
		data = text.read()		#safe file to string
	except:
		print 'Something went wrong, no Idea what'
		sys.exit()
#	print data			#print string
	datalen=12
	datacount=0
	linecount=0
	wordcount=0
	datapoint=0
	rowvalues=[]
	values=[]
	for x in data[:]:				#as long as there are values in data
		if data[datacount] == '\n':		#check if new line
		#	print datapoint
		#	print datacount
		#	print len(data)
		#	print data[384]
			if datacount != datapoint:
				rowvalues.append(int(data[datapoint:datacount]))	#rowvalues are the values to one date, wert speichern
			if len(rowvalues) == datalen:
				values.append(rowvalues)				#Zeile anfuegen
			rowvalues=[]						#zeile reset
		#	linecount++						#zeilencounter hoch
			datacount+=1						#datacount hoch
			datapoint=datacount					#speichstelle setzen
		#	wordcount==0						#wortcount reset
		elif data[datacount] != " ":					#wenn kein leerzeichen dann weiterzaehlen
			datacount+=1						
		elif data[datacount] == " ":					#wenn lehrzeichen dann 
			if data[datapoint:datacount]!="None":				#ask if there is a value at this point
				rowvalues.append(int(data[datapoint:datacount]))	#rowvalues are the values to one date, wert speichern
			else:
				rowvalues.append(np.nan)					#if not save 
			datacount+=1						#zeichencounter hoch 
			datapoint=datacount					#speicherstelle setzen
		#	wordcount++						#wortzaehler erhoehen
	if datacount != datapoint:
	#	if data[datapoint:datacount]!="None":				#ask if there is a value at this point
		rowvalues.append(int(data[datapoint:datacount]))	#rowvalues are the values to one date, wert speichern
	#	else:
	#		rowvalues.append(np.nan)					#if not save 
	if len(rowvalues) == datalen:
		values.append(rowvalues)				#Zeile anfuegen
									#wenn neue zeile
	print values
	mesure=[]
	endval=[]
	i=0
	ii=0
	while ii<len(values[0]):
		i=0
		while i<len(values):
			mesure.append(values[i][ii])
			i+=1
			
		endval.append(mesure)
		mesure=[]
		ii+=1
	print endval
	return endval					#return all the data in an array that has list in it as follows: [happy,health,stress,sport,money,social,year,month,day,hour,minute,second]


def Timestamps (endval):				#transform Date segments into string list of datetimes ["datetime","datetime",...] for example ["2002:1:2:14:23:12",...]
	i=0
	timearr=[]
	for x in endval[6]:
		timearr.append(str(endval[6][i])+":"+str(endval[7][i])+":"+str(endval[8][i])+":"+str(endval[9][i])+":"+str(endval[10][i])+":"+str(endval[11][i]))
		i+=1
	print timearr
	return timearr
#Plotprogramm
#input: the index wich list of endval should be taken, endval, the number of rows for subplot, the number of columns for subplot, the plot number for subplot, the Title of the subplot
#Output: a matplotlib.pyplot.plot subplot 
def plotdata(index,endval,sign,row,col,num,title):
	plot=plt.subplot(row,col,num)
	plt.title(title)
	x = [datetime.datetime.strptime(d,"%Y:%m:%d:%H:%M:%S") for d in Timestamps(endval)]
	print x
	#x=np.linspace(0,len(endval[0]),len(endval[0]))
#	plt.gca().set_major_locator(matplotlib.dates.DayLocator())
#	plt.gca().set_minor_locator(matplotlib.dates.HourLocator(arange(0,25,6)))
	plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d.%m.%Y-%H:%M:%S"))	#set format of Date at x-axis
	plt.plot(x,endval[index],sign)		
	plt.gcf().autofmt_xdate()		#format x-axis for Date (diagonal)
#	plt.show()
	return plot

#Ausfuehrung des Programmes
#Optionen: 
#               -all ... alle Daten einlesen
#               -h ... nur happy wert einlesen
#               -he ... health einlesen
#               -st ... stress einlesen
#               -sp ... sporty einlesen
#               -m ... money einlesen
#               -so ... social einlesen
#		-
#               -plot -[option] ... plotmodus [option] gibt zu plotende daten an
#                       zu -plot: [options]: -h happy, -he health, -st stress, -sp sporty, -m money, -so social, -all plot all data in several diagramms
#               - 
def main(argv):
	usage="	%prog [option] argument"		#define Usage message
	
#-----------------------option configurations----------------------------------------------
	parser = ArgumentParser(usage=usage)
	parser.add_argument("--Plot","-P",action="store",type=str,dest="plotargument",help="plot data for given argument \narguments are:\nha happy,\nhe health,\nst stress,\nsp sporty,\nm money,\nso social,\nall plot all data in several diagramms")
	parser.add_argument("--All","-A",action="store_true",default=False,help="starts the program (like default) asking you all the data possible")
	parser.add_argument("-H","--Happy",default=None,action="store",dest="happy",type=int,help="only intake is happy value")
	parser.add_argument("--Health","--He",default=None,action="store",dest="health",type=int,help="only intake is health value")
	parser.add_argument("--Stress","--St",default=None,action="store",dest="stress",type=int,help="only intake is stress value")
	parser.add_argument("--Sporty","--Sp",default=None,action="store",dest="sporty",type=int,help="only intake is sporty value")
	parser.add_argument("-M","--Money",default=None,action="store",dest="money",type=int,help="only intake is money value")
	parser.add_argument("--Social","--So",default=None,action="store",dest="social",type=int,help="only intake is social value")
	(options,args)=parser.parse_args()
#---------------------------------------------------------------------------------------------
			
	plotarguments=["ha","he","st","sp","m","so","all"]		#list of arguments for -Plot or -P command

	#save arguments of single data input options
	happy=options.happy
	health=options.health
	sporty=options.sporty
	stress=options.stress
	money=options.money
	social=options.social
	datalist=[happy,health,stress,sporty,money,social]		#save input to list
	
	if options.All or len(sys.argv)==1:			#if option all  was set, take data and write to file
		datalist=Input("a")		#save new input to datalist
		WriteData(datalist)
	for x in datalist :			#find out if single input was chosen and save the data to the data file
		if x!=None:  
			WriteData(datalist)
	if plotarguments.count(options.plotargument):		#if plotarguments list has argument of Plotoption in it, plot the given arguments diagramm
		endval=Read()					#read data file
		if options.plotargument == "all":		#first ask if the plotargument is all and if plot all datalists
			i=0
			while i < 6:
				plotdata(i,endval,'o',6,1,i+1,plotarguments[i])
				plotdata(i,endval,'-',6,1,i+1,plotarguments[i])
				i+=1
		else:						#if not plot the chosen data
			argindex=plotarguments.index(options.plotargument) 	#find out the index of the chosen plotargument in the plotargumentlist
			plotdata(argindex,endval,'o',1,1,1,plotarguments[argindex])		#plot the data to this argument
			plotdata(argindex,endval,'-',1,1,1,plotarguments[argindex])		#plot the data to this argument
	plt.show()
if __name__=="__main__":
	main(sys.argv)
	
