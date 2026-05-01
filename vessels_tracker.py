import requests
import pandas as pd
import csv
from tabulate import tabulate


def get_vessel_info(name):
    try:
        response = requests.get(
            "https://api.vesselapi.com/v1/search/vessels",
            params={"filter.name":name},
            headers={"Authorization": "Bearer ab2874fbb8f4a35c67219bacc5907e079a2fe04ff00ef34d2fee46ddedfc8379"}
        )
    except requests.RequestException:
        print("An error occurred while making the API request.")
        return None

    return response.json()


def strct_data(res):

    try:
        vessels_info = res
        info = vessels_info["vessels"]
        Columns = ["name", "imo","mmsi","vessel_type","country","country_code","operating_status","owner_name"]
        df = pd.DataFrame(info, columns = Columns)
        return df

    except KeyError:
        print("Couldn't read response")


def table(df):
    try:
        df.to_csv("vessel_info.csv", index=False)
        file = "vessel_info.csv"
        data =[]
        with open(file, "a") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return (tabulate(df, headers="keys", tablefmt="simple"))

    except AttributeError:
        return None

def main():
    vessel_name = input("Enter the name of the ship: ")
    vessel_data = get_vessel_info(vessel_name)
    structured_data = strct_data(vessel_data)
    print(table(structured_data))


if __name__ == "__main__":
    main()
