# Real-Time Weather Monitoring System
- This Python application retrieves and logs real-time weather data for a specified city from the OpenWeatherMap API. Weather data, including temperature and conditions, are retrieved every 5 minutes and displayed in the console. This project is designed with flexibility to extend for data storage and alert functionalities.

## Table of Contents
1. Project Overview
2. Design Choices
3. Dependencies
4. Setup and Installation
5. Running the Application
6. Future Improvements
7. License
8. Contact

   
## Project Overview
-This weather monitoring system:

  - Fetches current weather data for a specified city (in this case, Delhi) from the OpenWeatherMap API.
  - Logs temperature (in Celsius), weather conditions, and timestamp every 5 minutes.
  - Continuously monitors weather data and prints each entry to the console for quick inspection.
  
## Design Choices
 - Programming Language
   - Python was selected for its versatility and ease of working with APIs and scheduling tasks.

-Data Source
 - The OpenWeatherMap API provides accurate real-time weather data. The application calls the API every 5 minutes to retrieve updated information.

-Scheduler
 - The schedule library is used for clean and flexible periodic execution of tasks, allowing the program to fetch data at regular intervals without manual intervention.

-Data Handling
 - Currently, the data is stored in memory within a Python list (weather_data) for simple demonstration purposes. However, this design can easily be extended to save data in a database like SQLite for long-term storage and analysis.

## Dependencies
 - To run this application, ensure you have the following installed:

    1. Python 3.6+ - The application requires Python 3.6 or higher.
    2. Python Libraries:
       - requests: For API requests.
       - schedule: For periodic task scheduling.
       - pandas: For handling timestamps.
       - Install all required packages using:
         -. pip install requests schedule pandas


## Setup and Installation
 -1. Clone the Repository:
    - git clone https://github.com/your-username/weather-monitoring.git
    - cd weather-monitoring
 -2. API Key Configuration:
    - Obtain a free API key from OpenWeatherMap.
    - Replace the API_KEY variable in the code with your actual OpenWeatherMap API key.
 -3. Install Dependencies:
    - pip install -r requirements.txt

## Running the Application
 - To start the application:
     -. python weather_monitor.py
      - Upon running, the application will output logged weather data every 5 minutes to the console.

## Future Improvements
- This application can be enhanced in various ways:

  -. Database Integration: Save weather data to a database (e.g., SQLite, PostgreSQL) for historical analysis.
  -. Alert System: Add alerts when certain weather conditions or temperature thresholds are met.
  -. Web Interface: Implement a web interface to visualize and interact with the logged weather data.

## License
 - This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
 - For questions, suggestions, or contributions, please reach out to:

    -. Fathima Farheen  
    -. GitHub: FATHIMAFARHEEN2002
