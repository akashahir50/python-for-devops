import requests
import json
from typing import Dict, List, Optional

API_KEY = "9620b821bba54ced810a95cd11e4575b"
BASE_URL = "https://holidays.abstractapi.com/v1/"
OUTPUT_FILE = "holidays.json"

# Get and validate user inputs for API parameters.
def get_inputs() -> Optional[Dict[str, str]]:
    try:
        country = input("Country (US, IN): ").strip().upper()
        if country not in ['US', 'IN']:
            raise ValueError("Invalid country")
        year, month, day = map(int, [input("Year: "), input("Month: "), input("Day: ")])
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Invalid date")
        return {"country": country, "year": str(year), "month": str(month), "day": str(day)}
    except (ValueError, KeyboardInterrupt) as error:
        print(f"Input error: {error}")
        return None


# Fetch holidays from AbstractAPI with error handling
def fetch_holidays(params: Dict[str, str]) -> Optional[List[Dict]]:
    try:
        response = requests.get(BASE_URL, params={**params, "api_key": API_KEY}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data if isinstance(data, list) else None
    except (requests.RequestException, json.JSONDecodeError) as error:
        print(f"API error: {error}")
        return None


# Display holidays and save to JSON file safely.
def process_holidays(holidays: List[Dict]) -> None:
    print("\nHOLIDAYS:")
    if not holidays:  
        print("No holiday")
    else:
        for holiday in holidays:
            print(f"- {holiday.get('name', 'N/A')} ({holiday.get('date', 'N/A')})")
   
    try:
        with open(OUTPUT_FILE, 'w') as file:
            json.dump(holidays or [], file, indent=2)
        print(f"Saved to {OUTPUT_FILE}")
    except IOError as error:
        print(f"Save failed: {error}")


def main() -> None:
    params = get_inputs()
    if params:
        holidays = fetch_holidays(params)
        process_holidays(holidays)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled")