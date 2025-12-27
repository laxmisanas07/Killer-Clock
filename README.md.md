⏰ Killer Clock (Python Digital Clock)

"Time is what we want most, but what we use worst."



Killer Clock is a sleek, high-contrast Digital Clock application built using Python and Tkinter. It displays the current time (12-hour format) and date in a modern "Hacker/Cyberpunk" aesthetic.



Designed to be lightweight and efficient, this tool serves as a perfect desktop widget for developers who want a clean time display without clutter.



🚀 Features

* Live Time Tracking: Updates every second with precision.



* Indian Standard Format: 12-Hour format (AM/PM) with Seconds.



* Date Display: Shows Day, Date, Month, and Year dynamically.



* Neon Aesthetic: High-visibility Neon Green text on a Pitch Black background.



* No Lag: optimized using Python's after() method for smooth refreshing.



* Zero Dependencies: Built using standard Python libraries (no pip install needed for the main app).



🛠️ Tech Stack



* Language: Python 3.x



* GUI Library: Tkinter (Standard GUI toolkit)



* Modules: time, datetime



Run the Application



python killer\_clock.py



🧠 Code Logic



def update\_time():

&nbsp;   current\_time = strftime('%I:%M:%S %p') # 12-Hour Format

&nbsp;   time\_label.config(text=current\_time)

&nbsp;   time\_label.after(1000, update\_time) # Recursion



🔮 Future Improvements

\[ ] Add Alarm functionality.



\[ ] Add a Stopwatch/Timer mode.



\[ ] Allow users to change themes (Red/Blue/Green).



🤝 Connect with Me

Created with ❤️ by Laxmi Sanas 

