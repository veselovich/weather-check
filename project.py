import argparse
import csv
import geocoder
import re
import requests
import sys

from datetime import date, timedelta, datetime

API_KEY = "f98ea158c9cac4a3630fbb458bd0dbaa"


class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, location, units):
        params = {"q": location, "appid": self.api_key, "units": units}
        try:
            r = requests.get(self.base_url, params=params)
        except requests.RequestException:
            return {}
        else:
            return r.json()

    def get_weather(self, location, units="metric"):
        data = self.fetch_weather(location, units)

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The weather in {location} is {temp:.1f}°{self.units_to_temp(units)} with {description}."
        else:
            return "Weather not available."

    def units_to_temp(self, units):
        match units:
            case "metric":
                return "C"
            case "imperial":
                return "F"
            case _:
                return "Unknown units"

    def __str__(self):
        return "Weather from https://openweathermap.org/"


class Forecast(Weather):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.base_url = "http://api.openweathermap.org/data/2.5/forecast"

    def fetch_forecast(self, location, units):
        params = {"q": location, "appid": self.api_key, "units": units}
        try:
            r = requests.get(self.base_url, params=params)
        except requests.RequestException:
            return {}
        else:
            return r.json()

    def is_tomorrow(self, d: dict):
        tomorrow = date.today() + timedelta(days=1)
        return datetime.fromisoformat(d["dt_txt"]).date() == tomorrow

    def get_forecast(self, location, units="metric"):
        data = self.fetch_forecast(location, units)

        if data["cod"] == "200":
            temps = []
            precipitation = []
            forecast = filter(self.is_tomorrow, data["list"])
            for item in forecast:
                temps.append(item["main"]["temp"])
                precipitation.append(item["weather"][0]["main"])
            return (
                f"Temperature will be up to {max(temps):.1f}°{self.units_to_temp(units)}"
                + (
                    "\nAnd don't forget an umbrella!☔️"
                    if "Rain" in precipitation
                    else ""
                )
            )
        else:
            return "Forecast not available."


def main():
    log()

    parser = argparse.ArgumentParser(description="Shows the weather")
    parser.add_argument(
        "-l",
        "--location",
        nargs="+",
        default=my_location(),
        help="location: <city>[, <state>[, <country>]]",
        type=str,
    )
    parser.add_argument(
        "-u",
        "--units",
        default="metric",
        help="temperature measurement: metric/imperial",
        type=str,
    )
    args = parser.parse_args()

    location = " ".join(args.location).strip()
    check_location(location)

    if not args.units in ["metric", "imperial"]:
        sys.exit("Invalid units.")

    weather = Weather(API_KEY)
    forecast = Forecast(API_KEY)

    print()
    print(weather.get_weather(location, args.units))
    print("\nTomorrow's forecast:\n" + forecast.get_forecast(location, args.units))
    log_success()


def my_location():
    location = geocoder.ip("me")

    city = location.city if location.city else sys.exit("City is not available")
    state = location.state if location.state else sys.exit("State is not available")
    country = (
        location.country if location.country else sys.exit("Country is not available")
    )
    return [city + ",", state + ",", country]


def check_location(location):
    if not re.match(
        r"^([A-Za-z\s]+)(?:,\s*([A-Za-z\s]+))?(?:,\s*([A-Za-z\s]+))?$", location
    ):
        sys.exit("Invalid city name.")


def log():
    total_requests = 0
    today_requests = 0
    fieldnames = [
        "total_requests",
        "today_requests",
        "datetime",
        "arguments",
        "success",
    ]

    try:
        with open("log.csv", "r") as file:
            reader = list(csv.DictReader(file))
            last_row = reader[-1]
            total_requests = int(last_row["total_requests"])
            today_requests = (
                int(last_row["today_requests"])
                if datetime.fromisoformat(last_row["datetime"]).date() == date.today()
                else 0
            )
    except FileNotFoundError:
        with open("log.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    with open("log.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(
            {
                "total_requests": (total_requests + 1),
                "today_requests": (today_requests + 1),
                "datetime": datetime.today(),
                "arguments": " ".join(sys.argv[1:]),
                "success": 0,
            }
        )


def log_success():
    with open("log.csv", "rb+") as file:
        file.seek(-3, 2)
        file.write(b"1")


if __name__ == "__main__":
    main()
