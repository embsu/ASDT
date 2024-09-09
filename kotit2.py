import matplotlib.pyplot as plt
import tkinter as tk #käyttöliittymäkirjasto
import winsound
import time 
# jotta voit käyttää matplotlibiä näppärästi tkinterissä
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# runData = { 
# "world_records": {
#     1921: {"time": 10.6, "athlete": "Bob Hayes"},
#     1930: {"time": 10.3, "athlete": "Jesse Owens"},
#     1950: {"time": 9.9, "athlete": "Harrison Dillard"},
#     1960: {"time": 9.8, "athlete": "Wilma Rudolph"},
#     1970: {"time": 9.7, "athlete": "Jim Hines"},
#     1980: {"time": 9.5, "athlete": "Carl Lewis"},
#     1990: {"time": 9.4, "athlete": "Ben Johnson"},
#     2000: {"time": 9.3, "athlete": "Usain Bolt"},
#     2010: {"time": 9.2, "athlete": "Usain Bolt"},
#     2020: {"time": 9.2, "athlete": "Usain Bolt"}
# },
# "lion_speeds": {
#     "jukka": 50,    # km/h
#     "kalle": 53,
#     "matti": 48,
#     "simba": 50,
#     "mufasa": 51,
#     "scar": 52,
#     "rafiki": 47,
#     "timon": 49,
#     "pumba": 52,
#     "nala": 51
# }
# }

def ernu_juoksee():
    global current_position_ernu, speed_ernu, run_animation_ernu, start_time_ernu
    current_position_ernu = 0
    speed_ernu = 2  # Speed of Ernu (2 meters per second)
    step_size_ernu = 1  # 1 meter per step
    interval_ernu = int(1000 / speed_ernu)  # Interval in milliseconds
    start_time_ernu = time.time()  # Start time
    run_animation_ernu = True
    animate_ernu(step_size_ernu, interval_ernu)  # Start Ernu's animation

def animate_ernu(step_size, interval):
    global current_position_ernu, run_animation_ernu, start_time_ernu
    if run_animation_ernu and current_position_ernu < 100:
        ax.cla()  # Clear the plot
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_yticklabels([])
        ax.set_xlabel("Metrit")
        
        # Plot Ernu's position
        ax.plot(current_position_ernu, 10, "ro")  # "ro" means red dot
        kuvaaja_canvas.draw()  # Redraw the canvas
        
        winsound.Beep(440, 100)  # Beep sound for Ernu's step

        # Update position
        current_position_ernu += step_size
        
        # Call this function again after interval
        ikkuna.after(interval, animate_ernu, step_size, interval)
    elif current_position_ernu >= 100:  # Ernu has finished
        run_animation_ernu = False
        end_time = time.time()  # Stop the time
        total_time = end_time - start_time_ernu
        print(f"Ernun juoksu kesti {total_time:.2f} sekuntia")  # Print total time


# def kernu_juoksee():
#     global speed, step_size, interval, juoksuaani, current_position, run_animation, start_time, current_position
#     current_position = 0
#     speed = 3
#     step_size = 1
#     interval = int(1000 / speed)
#     juoksuaani = winsound.Beep(600, 300)
#     ax.plot(current_position, 20, "bo") # piirretään kernu
#     run_animation = True


  
# pääikkuna
ikkuna=tk.Tk() #luodaan ikkuna
ikkuna.title("Juoksukilpailu") #ikkunan otsikko
ikkuna.geometry("600x600+500+300") #määritellään ikkunan koko ja sijainti

# sijainti ja animaatio
current_position_ernu = 0
run_animation_ernu = False
start_time_ernu = 0



# luodaan kuvaaja
fig=Figure(figsize=(5,5), dpi=100)
ax=fig.add_subplot(111)
ax.set_xlim(0, 100)
ax.set_xlabel("Metrit")
ax.set_yticklabels([])


# upotetaan kuvaaja tkinteriin
kuvaaja_canvas=FigureCanvasTkAgg(fig, master=ikkuna)
kuvaaja_canvas.draw()
kuvaaja_canvas.get_tk_widget().place(x=10, y=100)

# napit
ernuNappi=tk.Button(ikkuna, text="Ernu", command=ernu_juoksee)
ernuNappi.place(x=200, y=60)
# kernuNappi=tk.Button(ikkuna, text="Kernu", command=kernu_juoksee)
# kernuNappi.place(x=100, y=60)

ikkuna.mainloop() #käynnistetään ikkuna




# #juoksugraafi
# years = list(range(1900, 2051))
# times = []
# athletes = []

# for year in years:
#     if year in runData["world_records"]:
#         times.append(runData["world_records"][year]["time"])
#         athletes.append(runData["world_records"][year]["athlete"])

# # Piirretään graafi
# plt.figure(figsize=(12, 6))
# plt.plot(years, times, marker='o', linestyle='-', color='b')
# plt.title('100 Metriä Maailmanennätysaikojen Kehitys (1900-2050)')
# plt.xlabel('Vuosi')
# plt.ylabel('Aika (sekunteina)')
# plt.grid(True)
# plt.show()