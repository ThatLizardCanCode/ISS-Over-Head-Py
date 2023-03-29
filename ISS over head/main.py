import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -41.366220  # Your latitude
MY_LONG = 173.132174  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
hour = time_now.hour

MY_EMAIL = "enter email"
MY_PASSWORD = "enter pw"

while True:
    time.sleep(60)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        if hour >= sunset:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs='janedoe@gmail.com',
                    msg="Look outside the iss is overhead"
                )
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs='johndoe@yahoo.co.nz',
                    msg=f"Subject:ISS \n\n Look the iss is overhead"
                )



