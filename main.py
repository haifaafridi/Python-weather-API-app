import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E3440")
        self.center_window()

        # API key (you'll need to get your own from openweathermap.org)
        self.api_key = "YOUR_API_KEY_HERE"

        self.setup_ui()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🌤️ Weather Finder",
            font=("Helvetica", 24, "bold"),
            bg="#2E3440",
            fg="#ECEFF4"
        )
        title_label.pack(pady=20)

        # Search frame
        search_frame = tk.Frame(self.root, bg="#2E3440")
        search_frame.pack(pady=10)

        self.city_entry = tk.Entry(
            search_frame,
            font=("Helvetica", 14),
            width=25,
            bg="#3B4252",
            fg="#ECEFF4",
            insertbackground="#ECEFF4",
            relief=tk.FLAT,
            borderwidth=2
        )
        self.city_entry.pack(side=tk.LEFT, padx=5, ipady=8)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())

        search_btn = tk.Button(
            search_frame,
            text="Search",
            command=self.get_weather,
            font=("Helvetica", 12, "bold"),
            bg="#5E81AC",
            fg="#ECEFF4",
            activebackground="#81A1C1",
            activeforeground="#ECEFF4",
            relief=tk.FLAT,
            cursor="hand2",
            width=10,
            height=1
        )
        search_btn.pack(side=tk.LEFT, padx=5)

        # Weather info frame
        self.info_frame = tk.Frame(self.root, bg="#3B4252")
        self.info_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # City name
        self.city_label = tk.Label(
            self.info_frame,
            text="Enter a city name",
            font=("Helvetica", 20, "bold"),
            bg="#3B4252",
            fg="#ECEFF4"
        )
        self.city_label.pack(pady=10)

        # Temperature
        self.temp_label = tk.Label(
            self.info_frame,
            text="--°C",
            font=("Helvetica", 48, "bold"),
            bg="#3B4252",
            fg="#88C0D0"
        )
        self.temp_label.pack(pady=10)

        # Weather description
        self.desc_label = tk.Label(
            self.info_frame,
            text="",
            font=("Helvetica", 16),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.desc_label.pack(pady=5)

        # Details frame
        details_frame = tk.Frame(self.info_frame, bg="#3B4252")
        details_frame.pack(pady=20)

        # Left column
        left_frame = tk.Frame(details_frame, bg="#3B4252")
        left_frame.pack(side=tk.LEFT, padx=20)

        self.feels_like_label = tk.Label(
            left_frame,
            text="Feels like: --°C",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.feels_like_label.pack(anchor=tk.W, pady=3)

        self.humidity_label = tk.Label(
            left_frame,
            text="Humidity: --%",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.humidity_label.pack(anchor=tk.W, pady=3)

        self.pressure_label = tk.Label(
            left_frame,
            text="Pressure: -- hPa",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.pressure_label.pack(anchor=tk.W, pady=3)

        # Right column
        right_frame = tk.Frame(details_frame, bg="#3B4252")
        right_frame.pack(side=tk.LEFT, padx=20)

        self.wind_label = tk.Label(
            right_frame,
            text="Wind: -- m/s",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.wind_label.pack(anchor=tk.W, pady=3)

        self.visibility_label = tk.Label(
            right_frame,
            text="Visibility: -- km",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.visibility_label.pack(anchor=tk.W, pady=3)

        self.clouds_label = tk.Label(
            right_frame,
            text="Clouds: --%",
            font=("Helvetica", 12),
            bg="#3B4252",
            fg="#D8DEE9"
        )
        self.clouds_label.pack(anchor=tk.W, pady=3)

        # Footer
        footer_label = tk.Label(
            self.root,
            text="Powered by OpenWeatherMap API",
            font=("Helvetica", 9),
            bg="#2E3440",
            fg="#4C566A"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)

    def get_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return

        if self.api_key == "YOUR_API_KEY_HERE":
            messagebox.showerror(
                "API Key Required",
                "Please get a free API key from:\nhttps://openweathermap.org/api\n\n"
                "Then replace 'YOUR_API_KEY_HERE' in the code with your actual API key."
            )
            return

        try:
            # API call
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                messagebox.showerror("Error", "City not found!")
            else:
                messagebox.showerror("Error", f"Error: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Connection error:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    def display_weather(self, data):
        # Extract data
        city_name = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        visibility = data['visibility'] / 1000  # Convert to km
        clouds = data['clouds']['all']
        description = data['weather'][0]['description'].title()

        # Update labels
        self.city_label.config(text=f"{city_name}, {country}")
        self.temp_label.config(text=f"{temp}°C")
        self.desc_label.config(text=description)
        self.feels_like_label.config(text=f"Feels like: {feels_like}°C")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.pressure_label.config(text=f"Pressure: {pressure} hPa")
        self.wind_label.config(text=f"Wind: {wind_speed} m/s")
        self.visibility_label.config(text=f"Visibility: {visibility} km")
        self.clouds_label.config(text=f"Clouds: {clouds}%")


def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
