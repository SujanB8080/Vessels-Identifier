# VESSELS Identifier
#### Description: This project will give the information of "Active/Decommissioned" vessel's details by searching it's name.

Vessels are the biggest life line for humans they are transporting large containers of goods, crude oils, petrolium products, and even people from one country to the other or may be one continent to the other.
There are different types of vessels which have different purposes.
There may be Oil Tankers, General Cargo Ships, LPG/LNG Tankers, Chemical Tankers, Dry Bulk Carriers etc.
</br>

I have created a project which will fetch you the details of the vessels like what country the vessel belongs, it's imo and mmsi number, is it active or decommisioned, what type it is , who is the owner/ manager.</br>

## vesselAPI
I have used the [vesselAPI](https://github.com/vessel-api/VesselApi) which provides real time AIS(Automatic Identification System) and maritime data about the vessels in the maritime waters. Instead of integrating multiple data sources and maintaining complex scraping infrastructure, we get a single API endpoint with normalized, reliable data.

It is built for
maritime research and analytics,
trade flow analysis,
fleet monitoring and tracking,
port operations intelligence
supply chain visibility</br>

***base URL*** : ```https://api.vesselapi.com/v1/search/vessels```</br>
**filter by name** : `filter.name` <br/>

## Libraries used
* **requests** : It is a popular third-party HTTP library for Python that simplifies the process of making web requests.
`requests.get(url)` : Retrieves information from a server. the retrieved information. Automatically decodes JSON response content into Python dictionaries.

* **pandas** : Pandas is a powerful, open-source Python library used primarily for data manipulation and analysis. It provides high-performance data structures designed to make working with structured (tabular, multidimensional, or time-series) data both easy and intuitive. `DataFrame`: A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

* **csv** : The csv module is part of the Python Standard Library and does not require installation. used for working with csv(comman separated values) files.

* **tabulate** : a lightweight Python package used to pretty-print tabular data in a human-readable format within terminals or text-based reports. It has only one function `tabulate`


## Implementation

I have created three functions excluding the `main` function namely `get_vessel_info`, `struct_data`, `table`. The first function will make a request to the vesselAPI for the vessel information by taking the name of a vessel/vessels and return the JSON response. The second function will take the JSON response fetches the required data `Columns` from it and converts it into a DataFrame. Finally in the table the data will be beautified and returned to the main.

The user is asked to enter the "name" of a vessel then this will be passed to the filter which will request the vesselAPI for the details. if the name matched more than one vessel all the of it will be returned as response in JSON format which willl be decoded using `response.json()`.

The JSON response will have too many fields , but I have made a column list which will only fetch the required field from the data. the desired data will be converted into the DataFrame using pandas and this will be returned to the table function.

Finally the data will be showed to the user which will have the details of vessel/s of matched name the user has had entered.

The result data will be appended to the `vessel_info.csv` every time the script runs.

## What data return?

vessel data will inclued name, imo(international maritime org) number, mmsi(maritime mobile service identity), type of vessel, country the vessel belongs, country code, operating status of vessel, year the vessel was build, owner/manager of the vessel(which company).

#### Data Table
 ![vessel data example](C:/Data_Science/Vessels%20Tracker/assets/vessel_data.png)

####  No vessel found
 ![If no match found](assets\unsuccessful.png)

#### No internet
 ![If there is no internet connection](assets\internet_error.png) 
