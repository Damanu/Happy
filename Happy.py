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
#filename='TestData'
filename='Daten_Happy'
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

def WriteData():		#ungetestet, geht wsl nicht
	text = open(path+filename,'r') #open file to read
	bis =text.read()		#save file to string
	text = open(path+filename,'w')	#open filen to write
	text.write(bis+"\n"+str(happy)+" "+str(health)+" "+str(stress)+" "+str(sporty)+" "+str(money)+" "+str(social)+" "+str(now.year)+" "+str(now.month)+" "+str(now.day)+" "+str(now.hour)+" "+str(now.minute)+" "+str(now.second))	#write data to file 

	
#Programm zum auslesen des Config files
def ReadConfig():
	text = open(path+Happy.config,'r')
	data = text.read()
	print data
#Programm zum auslesen der Daten
#Ausgabe: endval[index], index: 0=happy,1=health,2=stress,3=sporty,4=money,5=social,6=year,7=month,8=day,9=hour,10=minute,11=second
def Read():
	try:
		text = open(path+filename,'r+')	#open file to read
		data = text.read()		#safe file to string
	except:
		print "Something went wrong, no Idea what!"
		sys.exit()
#	print data			#print string
	datalen=12
	datacount=0
	linecount=0
	wordcount=0
	datapoint=0
	rowvalues=[]
	values=[]
	for x in data[:]:
		if data[datacount] == '\n':	
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
			rowvalues.append(int(data[datapoint:datacount]))	#rowvalues are the values to one date, wert speichern
			datacount+=1						#zeichencounter hoch 
			datapoint=datacount					#speicherstelle setzen
		#	wordcount++						#wortzaehler erhoehen
	if datacount != datapoint:
		rowvalues.append(int(data[datapoint:datacount]))	#rowvalues are the values to one date, wert speichern
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
def plotdata(index,endval,row,col,num,title):
	plot=plt.subplot(row,col,num)
	plt.title(title)
	x = [datetime.datetime.strptime(d,"%Y:%m:%d:%H:%M:%S") for d in Timestamps(endval)]
	print x
	#x=np.linspace(0,len(endval[0]),len(endval[0]))
#	plt.gca().set_major_locator(matplotlib.dates.DayLocator())
#	plt.gca().set_minor_locator(matplotlib.dates.HourLocator(arange(0,25,6)))
	plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d.%m.%Y-%H:%M:%S"))	#set format of Date at x-axis
	plt.plot(x,endval[index])		
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

#print sys.argv[1]
plotarguments=["-h","-he","-st","-sp","-m","-so","-all"]
arguments=["-all","-h","-he","-st","-sp","-m","-so","-chdata"] 
#try sys.argv[1]
if len(sys.argv)==1:
	(happy,health,stress,sporty,money,social)=Input("a")
	WriteData()
	endval=Read()
elif sys.argv[1] == "plot":
#		try sys.argv[2]
		endval=Read()
		if sys.argv[2] == "-all":
			i=0
			while i < 6:
				plotdata(i,endval,6,1,i+1,plotarguments[i])
				i+=1
		else:
			argindex=plotarguments.index(sys.argv[2])
			plotdata(argindex,endval,1,1,1,plotarguments[argindex])
else:
	print "wrong argument"
#		except NameError:
#			print "wrong second argument"
#			sys.exit()
#elif int(sys.argv[1]) >= 0 and int(sys.argv[1]) < 6:
#	(happy,health,stress,sporty,money,social)=Input("a")
#	WriteData()
#	endval=Read()
#	plotdata(int(sys.argv[1]),endval)
plt.show()
#except NameError:
#	print "Falsches argument"
