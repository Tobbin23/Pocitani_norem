
def Databaze(najdi:str, kusu:int):
	"Databaze Sebango a pozadovaný čas"
	diference = {"TR072": 0.265,\
		     "TR073": 0.265,\
		     "TR074": 0.265,\
		     "TR075": 0.265,\
		     "TR076":0.265,\
		     "TR077":0.265,\
		     "TR078": 0.265,\
		     "TR079": 0.265,\
		     "TR080": 0.265,\
		     "TR081": 0.265,\
		     "TR082": 0.265,\
		     "TR083": 0.265,\
		     "TR084": 0.265,\
		     "TR085": 0.265,\
		     "TR086": 0.265,\
		     "TR087": 0.265,\
		     "TR088":0.265,\
		     "TR089":0.265,\
		     "TR090":0.265,\
		     
		     "TF053": 0.46,\
		     "TF054":0.46,\
		     "TF055":0.46,\
		     "TF056":0.46,\
		     
		     
		     "TF067":0.59,\
		     "TF068":0.59,\
		     "TF069":0.59,\
		     "TF070":0.59,\
		     "TF071":0.59,\
		     "TF072":0.59,\
		     "TF073":0.59,\
		     "TF074":0.59,\
		     "TF075":0.59,\
		     "TF076":0.59,\
		     "TF077":0.59,\
		     "TF078":0.59,\
		     "TF079":0.59,\
		     "TF080":0.59,\
		     "TF081":0.59,\
		     "TF082":0.59,\
		     "TF083":0.59,\
		     "TF084":0.59,\
		     "TF085":0.59,\
		     "TF086":0.59,\
		     "TF087":0.59,\
		     "TF088":0.59,\
		     "TF138":0.59,\
		     "TF139":0.59,\
		     
		     "TF089":0.59,\
		     "TF090":0.59,\
		     "TF091":0.59,\
		     "TF092":0.59,\
		     "TF093":0.59,\
		     "TF094":0.59,\
		     "TF095":0.59,\
		     "TF096":0.59,\
		     "TF142":0.59,\
		     "TF141":0.59,\
		     "TF137":0.59,\
		     "TF140":0.59,\
		     
		     "TR091":0.219,\
		     "TR092":0.219,\
		     
		     "TF097":0.52,\
		     "TF098":0.52,\
		     
		     "TR101":0.24,\
		     "TR102":0.24,\
		     "TR103":0.24,\
		     "TR104":0.24,\
		     "TR109":0.24,\
		     "TR110":0.24,\
		     
		     "TF117":0.55,\
		     "TF118":0.55,\
		     "TF119":0.55,\
		     "TF120":0.55,\
		     "TF121":0.55,\
		     "TF122":0.55,\
		     "TF123":0.55,\
		     "TF124":0.55,\
		     "TF143":0.55,\
		     "TF144":0.55,\
		     "TF145":0.55,\
		     "TF146":0.55,\
		     
		     "WF001":0.45,\
		     "WF002":0.45,\
		     
		     "WR016":0.411,\
		     "WR017":0.411,\
		     "WR018":0.411,\
		     "WR026":0.411,\
		     "WR027":0.411,\
		     "WR028":0.411,\
		     
		     "TF125":0.531,\
		     "TF126":0.531,\
		     "TF127":0.531,\
		     "TF128":0.531,\
		     "TF157":0.531,\
		     "TF156":0.531,\
		     "TF158":0.531,\
		     "TF155":0.531,\
		     
		     "TR106":0.22,\
		     
		     "TR057":0.2,\
		     "TR058":0.2,\
		
		     "TF042":0.555,\
		     "TF037":0.555,\
		     "TF038":0.555,\
		     "TF041":0.555,\
		     "TF047":0.555,\
		     "TF048":0.555,\
		     "TF049":0.555,\
		     "TF050":0.555,\
		     "TF051":0.555,\
		     "TF052":0.555,\
		     "TF043":0.555,\
		     "TF105":0.555,\
		     "TF101":0.555,\
		     "TF106":0.555,\
		     "TF108":0.555,\
		     "TF031":0.555,\
		     
		     "TR064":0.23,\
		     "TR065":0.23,\
		     
		     "NR029":0.19,\
		     "NR030":0.19,\
		     "NR031":0.19,\
		     
		     "NF004":0.412,\
		     "NF005":0.412,\
		     "NF006":0.412,\
		     "NF007":0.412,\
		     "NF008":0.412,\
		     "NF009":0.412,\
		     "NF010":0.412,\
		     "NF011":0.412,\
		     "NF012":0.412,\
		     "NF013":0.412,\
		     "NF014":0.412,\
		     "NF015":0.412,\
		     "NF016":0.412,\
		     "NF017":0.412,\
		     "NF018":0.412,\
		     "NF019":0.412,\
		     "NF020":0.412,\
		     
		     "RF017":0.37,\
		     "RF018":0.37,\
		     "RF019":0.37,\
		     "RF020":0.37,\
		     "RF022":0.37,\
		     "RF025":0.37,\
		     "RF029":0.37,\
		     "RF023":0.37,\
		     "RF024":0.37,\
		     "RF031":0.37,\
		     
		     "RR013":0.25,\
		     "RR014":0.25,\
		     "RR015":0.25,\
		     "RR016":0.25,\
		     "RR017":0.25,\
		     "RR020":0.25,\
		     "RR022":0.25,\
		     "RR023":0.25,\
		     
		     "SR001":0.136,\
		     "SR005":0.136,\
		     "SR009":0.136,\
		     "SR002":0.136,\
		     "SR006":0.136,\
		     "SR010":0.136,\
		     "SR003":0.136,\
		     "SR007":0.136,\
		     "SR011":0.136,\
		     "SR004":0.136,\
		     "SR008":0.136,\
		     "SR012":0.136,\
		     "SR013":0.136,\
		     "SR016":0.136,\
		     "SR018":0.136,\
		     "SR021":0.136,\
		     
		     "TF133":0.653,\
		     "TF134":0.653,\
		     
		     "TR107":0.44,\
		     
		     "WR019":0.57,\
		     "WR020":0.57,\
		     
		     "WR011":0.32,\
		     "WR012":0.32,\
		     "WR013":0.32,\
		     "WR014":0.32,\
		     
		     "PR011":0.2,\
		     "PR012":0.2,\
		     "PR013":0.2,\
		     "PR014":0.2,\
		     
		     "PF001":0.513,\
		     "PF002":0.513,\
		     "PF004":0.513,\
		     "PF005":0.513,\
		     "PF006":0.513,\
		     
		     "TR143":0.73,\
		     "TR145":0.73,\
		     
		     "SM093":0.33,\
		     "SM091":0.33,\
		     "SM111":0.33,\
		     "SM109":0.33,\
		     "SM092":0.33,\
		     "SM100":0.33,\
		     "SM110":0.33,\
		     "SM099":0.33,\
		     "SM094":0.33,\
		     "SM102":0.33,\
		     "SM101":0.33,\
		     "SM103":0.33,\
		     "SM104":0.33,\
		     "SM112":0.33,\
		     "SM113":0.33,\
		     "SM114":0.33,\
		     "SM115":0.33,\
		     "SM116":0.33,\
		     "SM118":0.33,\
		     "SM119":0.33,\
		     "SM105":0.33,\
		     "SM107":0.33,\
		     "SM108":0.33,\
		     "SM106":0.33,\
		     }
	# Vrátí seznam párů (klíč a hodnotu)
	for k, i in diference.items():
		
		# Vrátí True pokud je nalezen klic
		if najdi in k:
			
			# Přeposílání dat do funkce (vykaz)
			vykaz(dif=k, Cas=i, mnozstvi=kusu)
			
		# Vraci False, výtisk je potlačen
		else:
			pass
		
	#for i in diference:
		#cas = i.get(najdi)
		#if cas:
			#vykaz(dif=najdi, Cas=cas, mnozstvi=kusu)

# anotace
def vykaz(dif:str,Cas:int, mnozstvi:int, difer=[], m=[], s=[]):
	# Pro aktualizace hodnot 
	difer.append(dif)
	m.append(mnozstvi)
	s.append(Cas)
	mi_n = []
	
	print("{:<1} {:^5} {:^5}".format("Sebango", "kusu", "cas"))
	
	for kus, mn, s_s in list(zip(difer,m, s)):
		#vypocet = [mat * cs for mat, cs in zip(m, s)]
		vypocet = mn * s_s
		
		#print(kus,mn, round(vypocet,2))
		print("{:^5} {:^8} {:^5}".format(kus, mn, round(vypocet,2)))
		mi_n.append(vypocet)
		
	print(soucet(celek=mi_n))
	
def soucet(celek:round):
	prac_minuty = 450
	#vaše norma je: {round(sum(celek)/450,2)}
	return f"pocet minut= {round(sum(celek),1)} "\
	       f"na {prac_minuty} = norma {round(sum(celek)/prac_minuty ,2)}"
	
		
	
def uzivatel():
	#Databaze(najdi="TR087", kusu=276)
	# Ošetření vyjímky pro chybné zadání
	try:
		# Smyčka , podminka walrus vrací True jinak "Q" vrací False  
		while (diference := input("$> ").upper()) != "Q" and (kusu := int(input("$^> "))) != "Q":
			
			# Jestli je True
			if diference:
				Databaze(najdi=diference, kusu=kusu)
				
			else:
				pass
			
	except ValueError as VE:
		print("chybna hodnota")
	except KeyboardInterrupt as KI:
		print(KI)
uzivatel()
	