import csv

def classify_aqi(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 200:
        return "Unhealthy"
    else:
        return "Hazardous"

def main():
    with open("sample_input.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            pm25 = float(row["PM2.5"])
            category = classify_aqi(pm25)
            
            print("PM2.5:", pm25)
            print("AQI Category:", category)
            print("----------------------")

if __name__ == "__main__":
    main()
