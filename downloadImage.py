import requests
from PIL import Image
from io import BytesIO

def main():
    url = "https://forecast.weather.gov/meteograms/Plotter.php?lat=34.7442&lon=-86.5084&wfo=HUN&zcode=ALZ006&gset=15&gdiff=7&unit=0&tinfo=CY6&ahour=0&pcmd=11101111110000000000000000000000000000000000000000000000000&lg=en&indu=1!1!1!&dd=&bw=&hrspan=48&pqpfhr=6&psnwhr=6"
    response = requests.get(url)

    success_code = 200
    if response.status_code == success_code:
        image = Image.open(BytesIO(response.content))
        image.save('nws_weather_plot.png')
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    main()