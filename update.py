from requests import get
import subprocess
#25.7.23
def kontrola(verze:str):
	
	with open("verze.txt", mode="r", encoding="utf-8") as ver_ze:
		vr = ver_ze.read()
		if vr != verze:
			return True
		else:
			return False
	
def stahni():
	ver_ze = get("https://raw.githubusercontent.com/Tobbin23/Pocitani_norem/main/verze.txt").text
	if kontrola(verze=ver_ze) is True:
		print("Probíhá update")
		subprocess.call(["git", "pull", "origin"])
	else:
		print("Verze je <Aktuální>")
		
stahni()
