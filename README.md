# 🌤️ Weather Finder App (Tkinter + OpenWeatherMap)

A simple and modern **Python Tkinter-based Weather App** that allows users to search for real-time weather information of any city using the **OpenWeatherMap API**.

This app displays:
- Temperature
- Weather description
- Feels-like temperature
- Humidity
- Pressure
- Wind speed
- Visibility
- Cloud percentage

---

## 🖥️ Preview

**UI Highlights**
- Clean and minimal design
- Dark theme with soft colors
- Centered window on launch
- Keyboard support (`Enter` key to search)

---

## 🚀 Features

- Search weather by city name
- Real-time weather data
- Beautiful and responsive UI
- Error handling for:
  - Empty input
  - Invalid city
  - API issues
  - No internet connection

---

## 📦 Requirements

Make sure you have **Python 3.x** installed, then install the required package:

<img width="371" height="469" alt="image" src="https://github.com/user-attachments/assets/58849943-1ac7-470e-849e-07a6178baeb5" />

pip install requests
Modules used:

tkinter

requests

datetime

🔑 How to Get an API Key
This app uses the OpenWeatherMap API.

Go to: https://openweathermap.org/api

Create a free account

Generate an API key

Replace this line in the code:

python
Copy code
self.api_key = "YOUR_API_KEY_HERE"
With your real API key:

python
Copy code
self.api_key = "your_actual_api_key_here"
▶️ How to Run the App
Save the file as weather_app.py

Open terminal / command prompt

Run the program:

bash
Copy code
python weather_app.py
📂 File Structure
Copy code
Weather-App/
│
├── weather_app.py
└── README.md
📌 Example Usage
Type a city name (e.g. Islamabad, London, New York)

Press Enter or click Search

See the live weather details on the screen

🛠️ Possible Improvements (Future Ideas)
Add forecast for next 5 days

Add weather icons

Add unit toggle (°C / °F)

Save search history

👩‍💻 Author
Haifa Afridi
Software Engineering Student
Learning Python & GUI Development

Feel free to use and modify this project for learning purposes 🌟

⚖️ License
This project is for educational use. You may reuse and modify it for practice or portfolio projects.
