import tkinter as tk
from time import strftime

# 1. Window setup
root = tk.Tk()
root.title("Killer Clock 🇮🇳")
root.geometry("600x250") # Thoda height badhaya taki date bhi aa sake
root.configure(bg="black")
root.resizable(False, False)

# 2. Function to update time
def update_time():
    # %I = 12 Hour format (01-12)
    # %M = Minutes
    # %S = Seconds
    # %p = AM / PM
    current_time = strftime('%I:%M:%S %p') 
    
    # %A = Full Day Name (Monday)
    # %d = Date (25)
    # %b = Month Short Name (Dec)
    # %Y = Year (2025)
    current_date = strftime('%A, %d %b %Y')

    # Labels ko update karna
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Har 1 second (1000ms) baad update karega
    time_label.after(1000, update_time)

# 3. Design for TIME (Bada aur Green)
time_label = tk.Label(root, font=('calibri', 80, 'bold'),
                      background='black',
                      foreground='#00FF00') # Neon Green
time_label.pack(anchor='center', pady=(30, 0)) # Upar se thoda gap

# 4. Design for DATE (Chota aur White/Orange)
date_label = tk.Label(root, font=('calibri', 20, 'bold'),
                      background='black',
                      foreground='orange') # Orange (Indian Flag Vibe)
date_label.pack(anchor='center')

# 5. Start
update_time()
root.mainloop()