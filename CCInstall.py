from urllib.request import Request, urlopen
webpage = str(urlopen(Request("https://raw.githubusercontent.com/rhysj6/PyUp/master/CCLV")).read().decode("utf-8"))
try:
	f = open('CCVersion.txt', 'r+')
	currentVersion= str(f.read()) ##Reads the version file
	f.close()
except:
	currentVersion = "Not installed" ##If there is no file then this will fail the if statement
if webpage != currentVersion and currentVersion != "Beta" and currentVersion != "Don't Update": ##Checks if the current version is the same as the latest version 
	print("Installing Custom Code module Version:",webpage)
	f = open('CCVersion.txt', 'w+')
	f.write(webpage) ##updates the version number
	f.close()
	webpage = str(urlopen(Request("https://raw.githubusercontent.com/rhysj6/PyUp/master/CustomCode")).read().decode("utf-8"))
	f = open('CustomCode.py', 'w+')
	f.write(webpage) ##updates the main py file
	f.close()
