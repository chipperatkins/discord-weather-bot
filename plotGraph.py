import requests
import matplotlib.pyplot as plt
import pandas as pd

def requestDataPeriods():
    url = 'https://api.weather.gov/gridpoints/HUN/66,43/forecast/hourly'
    response = requests.get(url)
    return response.json()['properties']['periods']

def main():
    periods = requestDataPeriods()
    hours = [p['startTime'] for p in periods]
    temperature = [p['temperature'] for p in periods]
    precipitation_probability = [p['probabilityOfPrecipitation']['value'] for p in periods]
    humidity = [p['relativeHumidity']['value'] for p in periods]
    wind_speed = [float(p['windSpeed'].split()[0]) if isinstance(p['windSpeed'], str) 
                else p['windSpeed']['value'] for p in periods]

    df = pd.DataFrame({
        'Time': hours,
        'Temperature': temperature,
        'Precipitation Probability (%)': precipitation_probability,
        'Humidity (%)': humidity,
        'Wind Speed (mph)': wind_speed
    })

    df['Time'] = pd.to_datetime(df['Time'])

    plt.figure(figsize=(14, 10))

    plt.subplot(4, 1, 1)
    plt.plot(df['Time'], df['Temperature'], color='orange', label='Temperature')
    plt.ylabel('Temperature (°F)')
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(df['Time'], df['Precipitation Probability (%)'], color='blue', label='Precipitation Probability')
    plt.ylabel('Precipitation Probability (%)')
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(df['Time'], df['Humidity (%)'], color='green', label='Humidity')
    plt.ylabel('Humidity (%)')
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(df['Time'], df['Wind Speed (mph)'], color='purple', label='Wind Speed')
    plt.ylabel('Wind Speed (mph)')
    plt.xlabel('Time')
    plt.legend()

    plt.tight_layout()
    # plt.show()

    plt.savefig('weather_plot.png')

if __name__ == "__main__":
    main()