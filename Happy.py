import os				
import datetime
import numpy as np
import matplotlib.pyplot as plt  
#das i/o Getue geht so wie hier beschrieben: https://docs.python.org/2/tutorial/inputoutput.html
# supercoole Scientific software fuer Python: SciPy ... numpy und matplotlib sind da auch drinnen

#Definition um bash mit sh("script") aufuehren zu koennen

#def sh(script):
#    os.system("bash -c '%s'" % script)

#Dateipfad
path='/home/emanuel/Dropbox/Programmieren/Python/'
filename='Daten_Happy'
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

	
	
#Programm zum auslesen der Daten
def Read():
	text = open(path+filename,'r')	#open file to read
	data = text.read()		#safe file to string
	print data			#print string
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
	return endval
#Plotprogramme
def plotdata(index):
	x=np.linspace(0,len(endval[0]),len(endval[0]))
	plt.plot(x,endval[index])
	plt.show()


#Ausfuehrung des Programmes
(happy,health,stress,sporty,money,social)=Input("a")
WriteData()
endval=Read()
plotdata(0)
