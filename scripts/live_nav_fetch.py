import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# url = "https://api.mfapi.in/mf/125497"
# response = requests.get(url)
for scheme_name, amfi_code in schemes.items(): 
    url = f"https://api.mfapi.in/mf/{amfi_code}"
    response = requests.get(url)
    print(f"Fetching {scheme_name}...")

    if response.status_code == 200:
        print("Data fetched successfully")
    
        data = response.json()
    
        print (data.keys())
    
        print (data["meta"])
    
        nav_df= pd.DataFrame(data["data"])

        print (nav_df.head())

        nav_df.to_csv(
            f"data/raw/{scheme_name}_live_nav.csv",
            index=False
        )
        print ("CSV saved successfully")
    
    else:
        print("Error:", response.status_code)