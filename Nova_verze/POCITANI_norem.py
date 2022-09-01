from banner import Barvy, Logo

def Databaze(najdi:str, kusu:int):
	"Databaze Sebango a pozadovaný čas"
	diference = {"TR072": 0.5,\
		     "TR073": 0.5,\
		     "TR074": 0.5,\
		     "TR075": 0.5,\
		     "TR076":0.5,\
		     "TR077":0.5,\
		     "TR078": 0.5,\
		     "TR079": 0.5,\
		     "TR080": 0.5,\
		     "TR081": 0.5,\
		     "TR082": 0.5,\
		     "TR083": 0.5,\
		     "TR084": 0.5,\
		     "TR085": 0.5,\
		     "TR086": 0.5,\
		     "TR087": 0.5,\
		     "TR088":0.5,\
		     "TR089":0.5,\
		     "TR090":0.5,\
		     
		     "TF053": 0.5,\
		     "TF054":0.5,\
		     "TF055":0.5,\
		     "TF056":0.5,\
		     
		     
		     "TF067":0.5,\
		     "TF068":0.5,\
		     "TF069":0.5,\
		     "TF070":0.5,\
		     "TF071":0.5,\
		     "TF072":0.5,\
		     "TF073":0.5,\
		     "TF074":0.5,\
		     "TF075":0.5,\
		     "TF076":0.5,\
		     "TF077":0.5,\
		     "TF078":0.5,\
		     "TF079":0.5,\
		     "TF080":0.5,\
		     "TF081":0.5,\
		     "TF082":0.5,\
		     "TF083":0.5,\
		     "TF084":0.5,\
		     "TF085":0.5,\
		     "TF086":0.5,\
		     "TF087":0.5,\
		     "TF088":0.5,\
		     "TF138":0.5,\
		     "TF139":0.5,\
		     
		     "TF089":0.5,\
		     "TF090":0.5,\
		     "TF091":0.5,\
		     "TF092":0.5,\
		     "TF093":0.5,\
		     "TF094":0.5,\
		     "TF095":0.5,\
		     "TF096":0.5,\
		     "TF142":0.5,\
		     "TF141":0.5,\
		     "TF137":0.5,\
		     "TF140":0.5,\
		     
		     "TR091":0.5,\
		     "TR092":0.5,\
		     
		     "TF097":0.5,\
		     "TF098":0.5,\
		     
		     "TR101":0.5,\
		     "TR102":0.5,\
		     "TR103":0.5,\
		     "TR104":0.5,\
		     "TR109":0.5,\
		     "TR110":0.5,\
		     
		     "TF117":0.5,\
		     "TF118":0.5,\
		     "TF119":0.5,\
		     "TF120":0.5,\
		     "TF121":0.5,\
		     "TF122":0.5,\
		     "TF123":0.5,\
		     "TF124":0.5,\
		     "TF143":0.5,\
		     "TF144":0.5,\
		     "TF145":0.5,\
		     "TF146":0.5,\
		     
		     "WF001":0.5,\
		     "WF002":0.5,\
		     
		     "WR016":0.5,\
		     "WR017":0.5,\
		     "WR018":0.5,\
		     "WR026":0.5,\
		     "WR027":0.5,\
		     "WR028":0.5,\
		     
		     "TF125":0.5,\
		     "TF126":0.5,\
		     "TF127":0.5,\
		     "TF128":0.5,\
		     "TF157":0.5,\
		     "TF156":0.5,\
		     "TF158":0.5,\
		     "TF155":0.5,\
		     
		     "TR106":0.5,\
		     
		     "TR057":0.5,\
		     "TR058":0.5,\
		
		     "TF042":0.5,\
		     "TF037":0.5,\
		     "TF038":0.5,\
		     "TF041":0.5,\
		     "TF047":0.5,\
		     "TF048":0.5,\
		     "TF049":0.5,\
		     "TF050":0.5,\
		     "TF051":0.5,\
		     "TF052":0.5,\
		     "TF043":0.5,\
		     "TF105":0.5,\
		     "TF101":0.5,\
		     "TF106":0.5,\
		     "TF108":0.5,\
		     "TF031":0.5,\
		     
		     "TR064":0.5,\
		     "TR065":0.5,\
		     
		     "NR029":0.5,\
		     "NR030":0.5,\
		     "NR031":0.5,\
		     
		     "NF004":0.5,\
		     "NF005":0.5,\
		     "NF006":0.5,\
		     "NF007":0.5,\
		     "NF008":0.5,\
		     "NF009":0.5,\
		     "NF010":0.5,\
		     "NF011":0.5,\
		     "NF012":0.5,\
		     "NF013":0.5,\
		     "NF014":0.5,\
		     "NF015":0.5,\
		     "NF016":0.5,\
		     "NF017":0.5,\
		     "NF018":0.5,\
		     "NF019":0.5,\
		     "NF020":0.5,\
		     
		     "RF017":0.5,\
		     "RF018":0.5,\
		     "RF019":0.5,\
		     "RF020":0.5,\
		     "RF022":0.5,\
		     "RF025":0.5,\
		     "RF029":0.5,\
		     "RF023":0.5,\
		     "RF024":0.5,\
		     "RF031":0.5,\
		     
		     "RR013":0.5,\
		     "RR014":0.5,\
		     "RR015":0.5,\
		     "RR016":0.5,\
		     "RR017":0.5,\
		     "RR020":0.5,\
		     "RR022":0.5,\
		     "RR023":0.5,\
		     
		     "SR001":0.5,\
		     "SR005":0.5,\
		     "SR009":0.5,\
		     "SR002":0.5,\
		     "SR006":0.5,\
		     "SR010":0.5,\
		     "SR003":0.5,\
		     "SR007":0.5,\
		     "SR011":0.5,\
		     "SR004":0.5,\
		     "SR008":0.5,\
		     "SR012":0.5,\
		     "SR013":0.5,\
		     "SR016":0.5,\
		     "SR018":0.5,\
		     "SR021":0.5,\
		     
		     "TF133":0.5,\
		     "TF134":0.5,\
		     
		     "TR107":0.5,\
		     
		     "WR019":0.5,\
		     "WR020":0.5,\
		     
		     "WR011":0.5,\
		     "WR012":0.5,\
		     "WR013":0.5,\
		     "WR014":0.5,\
		     
		     "PR011":0.5,\
		     "PR012":0.5,\
		     "PR013":0.5,\
		     "PR014":0.5,\
		     
		     "PF001":0.5,\
		     "PF002":0.5,\
		     "PF004":0.5,\
		     "PF005":0.5,\
		     "PF006":0.5,\
		     
		     "TR143":0.5,\
		     "TR145":0.5,\
		     
		     "SM093":0.5,\
		     "SM091":0.5,\
		     "SM111":0.5,\
		     "SM109":0.5,\
		     "SM092":0.5,\
		     "SM100":0.5,\
		     "SM110":0.5,\
		     "SM099":0.5,\
		     "SM094":0.5,\
		     "SM102":0.5,\
		     "SM101":0.5,\
		     "SM103":0.5,\
		     "SM104":0.5,\
		     "SM112":0.5,\
		     "SM113":0.5,\
		     "SM114":0.5,\
		     "SM115":0.5,\
		     "SM116":0.5,\
		     "SM118":0.5,\
		     "SM119":0.5,\
		     "SM105":0.5,\
		     "SM107":0.5,\
		     "SM108":0.5,\
		     "SM106":0.5,\
		     "ST":0.5\
		     }
	try:
		# Vrátí seznam párů (klíč a hodnotu)
		for k, i in diference.items():
		
			# Vrátí True pokud je nalezen klic
			if najdi in k:
			
				# Přeposílání dat do funkce (vykaz)
				# k = Sebango
				# i = cas
				vykaz(dif=k, Cas=i, mnozstvi=kusu)
			
			# Vraci False, výtisk je potlačen
			else:
				pass
	except ValueError as VE:
		print("chybné Sebango")
	except KeyboardInterrupt as KI:
		print(Ki)
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
	#print(Barvy.tucne)
	print(Barvy.tucne,"\t{:^8} |{:^8} |{:^8}".format("Sebango", "kusu", "cas"))
	
	for kus, mn, s_s in list(zip(difer,m, s)):
		#vypocet = [mat * cs for mat, cs in zip(m, s)]
		vypocet = mn * s_s
		
		#print(kus,mn, round(vypocet,2))
		print(Barvy.tucne,"\t{:^8} |{:^8} |{:^8}".format(kus, mn, round(vypocet,2)))
		mi_n.append(vypocet)
		
	print(soucet(celek=mi_n))
	
def soucet(celek:round):
	prac_minuty = 450
	# Vypocet odpracovanych minut pracovnika
	ok_nok = round(sum(celek)/prac_minuty ,2)
	
	# Vypocet chybejicich minut do 85%
	do_ok = round(sum(celek))-prac_minuty
	
	if ok_nok <= 0.84:
		#vaše norma je: {round(sum(celek)/450,2)}
		return f"\t{Barvy.tucne}pocet minut= {round(sum(celek),1)} "\
		       f": {prac_minuty} = norma {Barvy.tucne}{Barvy.ruda}{ok_nok}\n"\
		       f"\tDo normy {do_ok} minut\n"
	elif ok_nok >= 0.85:
		return f"\t{Barvy.tucne}pocet minut= {round(sum(celek),1)} "\
			       f": {prac_minuty} = norma {Barvy.tucne}{Barvy.zelena}{ok_nok}\n"
		
	
		
	
def uzivatel():
	#Databaze(najdi="TR087", kusu=276)
	# Ošetření vyjímky pro chybné zadání
	try:
		print(Logo())
		# Smyčka , podminka walrus vrací True jinak "Q" vrací False  
		while (diference := input(f"\t{Barvy.reset}Sebango-> ").upper()) != "Q" and (kusu := int(input(f"\tcelkem+> "))) != "Q":
			
			# Jestli je True
			if diference:
				print()
				Databaze(najdi=diference, kusu=kusu)
				
			else:
				pass
			
	except ValueError as VE:
		print("chybna hodnota")
	except KeyboardInterrupt as KI:
		print("Relace ukončena")
uzivatel()
