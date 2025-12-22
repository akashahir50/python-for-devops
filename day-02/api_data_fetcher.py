import requests
import json
api_key = "9620b821bba54ced810a95cd11e4575b"
url = "https://holidays.abstractapi.com/v1/"

country = input("Country (US, INDIA): ").upper()
year = int(input("Year: "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))

response = requests.get(url, params={
    "api_key": api_key,
    "country": country,
    "year": year,
    "month": month,
    "day": day
})

holidays = response.json()

print("HOLIDAYS:")
if holidays:
    for h in holidays:
        print(f"- {h['name']} ({h['date']})")
else:
    print("No holidays")


filename = f"output.json"
with open(filename, 'w') as f:
    json.dump(holidays, f, indent=2)
print(f"Saved to {filename}")
