# pip win10toast
#request
# pandas

import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier

# your gmail credential here
gmail_id="8as1931140@gmail.com"
gmail_pwd="@shaurya1"

# for desktop notification
toast=ToastNotifier()

def sendmail(to, name, sub, msg):
	pass
	print("Sending Email")
	s=smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(gmail_id, gmail_pwd)
	s.sendmail(gmail_id, to, f"Subject : {sub}\n\n{msg}")
	s.quit()
	print(f"Email sent {to}\nSubject: {sub}\nMessage: {msg}")
	toast.show_toast("Email Sent!", f"Birthday mail was sent to {name}.", threaded=True, icon_path=None, duration=6)
	
 
 
if __name__=="__main__":
	# read the excel sheet having all the details
	dataframe = pd.read_excel("C:\\Users\\Shaurya Purwar\\Desktop\\data.xlsx")
	date_now = datetime.datetime.now().strftime("%d-%m")	# today date in format : DD-MM
	year_now = datetime.datetime.now().strftime("%Y")	# current year in format : YY
	
	
	for index,item in dataframe.iterrows():
		msg = "Many Many Happy Returns of the day dear " + str(item['NAME'])                 
		date_bday = item['BIRTHDAY'].strftime("%d-%m")	# extracting DD-MM of the friends from excel sheet             
		
		if (date_now == date_bday):              
			sendmail(item['EMAIL'], item['NAME'], "Happy Birthday", msg)                    
			# to record the years in which email has been sent
			i=index
			yr = dataframe.loc[i,'WISHED_IN']
			dataframe.loc[i,'WISHED_IN'] = str(yr) + ', ' + str(year_now)             
			dataframe.to_excel('C:\\Users\\Shaurya Purwar\\Desktop\\data.xlsx', index = False)
