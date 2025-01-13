# Weather Bestie AI 🌦️🌍

Welcome to **Weather Bestie AI**, your personalized weather assistant and travel buddy! This program helps you plan a spontaneous holiday based on current and forecasted weather conditions for your chosen destinations. Your hilarious, weather-smart BFF for all things adventure and planning!! 🗣🌞

### Features ✨
* **Real-Time Weather Insights**: Get up-to-date weather conditions for your chosen city.
* **Weather Forecasts**: Plan a trip for 3 days ahead with forecasted temperature and weather descriptions.
* **Activity Suggestions**: Fun activity recommendations based on the weather.
* **Sunrise & Sunset Planning**: Know when to catch a beautiful sunrise or sunset at your destination.
* **Multi-City Travel**: Plan visits to two cities, with detailed weather data and suggested plans.
* **Quirky Travel Notes**: Automatically creates a fun holiday plan summary in a text file.

---
  
### How It Works 🛠️
1. **Start with a City**: Input your name and the first city you want to explore.
2. **Choose Your First Holiday Destination**: Select where you want to go in 3 days, and get weather forecasts for that date.
3. **Add a Second Destination**: After a day in your first city, choose a second destination for even more fun!
4. **Save Your Holiday Plan**: The program generates a travel summary in a text file (besties_holiday_plan.txt).

--- 
   
### Technologies Used 💻
* **Python**: Core programming language for functionality.
* **OpenWeatherMap API**: Fetches real-time and forecasted weather data.
* **Datetime Module**: Handles date and time operations.
* **File Handling**: Saves your holiday plan as a text file.

---

### Installation 🚀
1. Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/weather-bestie-ai.git
cd weather-bestie-ai

2. Install the required Python libraries:
bash
Copy code
pip install requests

3. Replace the api_key with your own OpenWeatherMap API key. Get it [here] (https://openweathermap.org/appid).

---
   
### Usage 📝
Run the program:

bash
Copy code
python weather_bestie_ai.py

Follow the prompts to:
* Enter cities.
* Get weather details.
* Plan your dream holiday!
Your holiday plan will be saved in besties_holiday_plan.txt.

---

### Example Output 🎉
vbnet
Copy code

Hey!🦾🤪 I am your weather AI bestie! What's your name?: Elizabeth
Hi Elizabeth 💐🥰!

Which city are you interested in looking at first?: London
Nice! So the general weather in London is sunny ☀️☀️.
The current temperature there is: 15°C, and feels like: 13°C (could be worse!!)

SO! As your BFFL, if we were to go on holiday in 3 days time, which city should we go to? (somewhere hot please!!): Barcelona
Nice choice bestie!!! On 2024-03-20, the temperature in Barcelona will be 22°C and the weather will be clear sky 🌤 - not bad at all!
...

This will be soo cute! If we get to Madrid before 07:15am, we'll get to see the sun rise 🌇☄️. But if we miss that, we can still watch the sun set at 07:45pm. How cute! 🌗🌙

### File Summary 📂
* weather_bestie_ai.py: The main program script.
* besties_holiday_plan.txt: A generated file summarizing your planned trip.
  
### Contributing 🤝
Feel free to fork this repository and make improvements. Submit a pull request with your changes!
