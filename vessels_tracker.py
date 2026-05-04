import os
import requests
import pandas as pd
from tabulate import tabulate
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VESSEL_API_KEY")

BASE_URL = "https://api.vesselapi.com/v1/search/vessels"

COLUMNS = [
    "name",
    "imo",
    "mmsi",
    "vessel_type",
    "country",
    "country_code",
    "operating_status",
    "year_built",
    "owner_name",
]


def get_vessel_info(name: str) -> dict | None:
    """Fetch vessel data from the vesselAPI by vessel name.
    Returns the JSON response dict, or None on failure.
    """
    if not API_KEY:
        print("Error: VESSEL_API_KEY not found.")
        return None

    try:
        response = requests.get(
            BASE_URL,
            params={"filter.name": name},
            headers={"Authorization": API_KEY},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Try again.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected request error: {e}")

    return None


def structure_data(response: dict) -> pd.DataFrame | None:
    """Extract relevant fields from the API response into a DataFrame."""
    if response is None:
        return None

    try:
        vessels = response.get("vessels", [])
        if not vessels:
            print("No vessels found for that name.")
            return None

        rows = []
        for vessel in vessels:
            row = {col: vessel.get(col, "N/A") for col in COLUMNS}
            rows.append(row)

        return pd.DataFrame(rows, columns=COLUMNS)

    except (KeyError, TypeError) as e:
        print(f"Error reading API response: {e}")
        return None


def display_table(df: pd.DataFrame) -> str | None:
    """print the DataFrame as a table and save it to CSV."""
    if df is None:
        return None
    
    output_file = "vessel_info.csv"
    file_exists = os.path.isfile(output_file)
    df.to_csv(output_file, index = False, mode = 'a', header = not file_exists)
    print(f"Data saved to {output_file}")

    return tabulate(df, headers="keys", tablefmt="simple", showindex=False)


def main():
    vessel_name = input("Enter the name of the ship: ").strip()

    if not vessel_name:
        print("No name entered. Exiting.")
        return

    print(f"\nSearching for '{vessel_name}'...\n")

    raw_data = get_vessel_info(vessel_name)
    df = structure_data(raw_data)
    result = display_table(df)

    if result:
        print(result)
    else:
        print("No data to display.")


if __name__ == "__main__":
    main()