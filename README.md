***Setting up***

1. Download Docker and open Docker Desktop: 
        
- Visit the official Docker website at [https://www.docker.com/get-started](https://www.docker.com/get-started) and follow the instructions to download and install Docker for your operating system.

2. Clone the repository: 


        git clone https://github.com/nadziejapio/calendar.git
        cd calendar


3. Add your API key to uws_calendar/config.py file and save it:


        api_key = 'HERE_IS_YOUR_API_KEY'

4. Build the Docker image: 


        docker build -t uws-calendar .

5. Run the Docker container: 


        docker run -p 8000:8000 uws-calendar

6. Access the application: 

   Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Django application running inside the Docker container.

7. Stop the Docker container: 

   Press `Ctrl+C` in the terminal to stop the running Docker container.
    
8. If you want to run the unit tests for the application, use the following command inside the Docker container or in your local environment:


        python manage.py test


***How to use calendar?***
- Index Page (Monthly View):
    The index page displays a monthly calendar view with events highlighted on the respective dates.
    Navigation:
        Use the "Previous" and "Next" buttons to navigate between different months.
- Search Functionality:
    Use the search bar to filter events based on tags.
    After entering a keyword, the results page will display matching events.
- Event Details:
    Click on any event in the calendar to view detailed information about that event.
