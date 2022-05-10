
# Automatic Birthday Wisher

Send birthday wishes to your friends and family members on their birthday.


## Screenshots

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Automatic-Birthday-Wisher/main/Screenshots/birthday.jpg)
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Automatic-Birthday-Wisher/main/Screenshots/Screenshot_20220504-233740_1.jpg)
Received mail

## Installation

Install required modules using:

```bash
pip install requests
pip install win10toast
pip install pandas
```
    
## Usage/Examples
Create a pandas dataframe:
```python
dataframe = pd.read_excel("C:\\Users\\Shaurya Purwar\\Desktop\\data.xlsx")
```
Extract current date / time:
```python
date_now = datetime.datetime.now().strftime("%d-%m")
year_now = datetime.datetime.now().strftime("%Y")
```
Command to send the wishes:
```python
s.login(gmail_id, gmail_pwd)
s.sendmail(gmail_id, to, f"Subject : {sub}\n\n{msg}")
```
Run above command if today is the birthday:
```python
if (date_now == date_bday):              
			sendmail(item['EMAIL'], item['NAME'], "Happy Birthday", msg)
```
Generate a Windows 10 notification:
```python
toast=ToastNotifier()
toast.show_toast("Email Sent!", f"Birthday mail was sent to {name}.", threaded=True, icon_path=None, duration=6)
```


## Acknowledgements

 - [GeeksForGeeks](https://www.bing.com/search?q=automatic+birthday+wisher+using+python&cvid=8872988571c64d9baa644afc47e1dcce&aqs=edge.0.69i59j69i57j0l6j69i60.3945j0j1&pglt=385&FORM=ANSPA1&PC=U531)
 
 

