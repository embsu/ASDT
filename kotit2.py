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

# Funktio, joka piirtää juoksijan
def animate_runner(runner_name, position, speed, step_size, interval, color, sound_freq):
    global run_animation, start_time, current_positions
    
    if run_animation and position < 100:
        ax.cla()  # tyhjennä akseli
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 30)
        ax.set_yticklabels([])
        ax.set_xlabel("Metrit")

        # piirrä juoksijat
        for name, pos in current_positions.items():
            y_position = 10 if name == 'Ernu' else 20  # eri y-koordinaatti 
            ax.plot(pos, y_position, 'ro' if name == 'Ernu' else 'bo', label=name)  # piirrä juoksija

        kuvaaja_canvas.draw()  # uudelleenpiirrä kuvaaja
        winsound.Beep(sound_freq, 100)
        current_positions[runner_name] = position + step_size # päivitä juoksijan sijainti
        
        # seuraava askel
        ikkuna.after(interval, animate_runner, runner_name, current_positions[runner_name], speed, step_size, interval, color, sound_freq)

    elif position >= 100:  # maaliin tulo
        run_animation = False
        end_time = time.time()  # tallenna lopetusaika
        total_time = end_time - start_time
        print(f"{runner_name} juoksi 100 metriä {total_time:.2f} sekunnissa")  # printtaa tulos
        ax.text(50,30, f"{runner_name} juoksi 100 metriä {total_time:.2f} sekunnissa", fontsize=12, ha='center')
        ax.text(50, 15, f"{runner_name} voitti!", fontsize=12, ha='center') # printtaa voittaja
        kuvaaja_canvas.draw()

#ernestin juoksu
def ernu_juoksee():
    global start_time, run_animation
    current_positions['Ernu'] = 0
    speed = 2  # 2 metriä per sekunti
    step_size = 1
    interval = int(1000 / speed)
    start_time = time.time()
    run_animation = True
    animate_runner('Ernu', current_positions['Ernu'], speed, step_size, interval, 'ro', 440)  # juoksijan nimi, sijainti, nopeus, askel, aikaväli, väri, äänen taajuus (välitetään animate_runner-funktiolle)

#kernestin juoksu
def kernu_juoksee():
    global start_time, run_animation
    current_positions['Kernu'] = 0
    speed = 3  # 3 metriä per sekunti
    step_size = 1
    interval = int(1000 / speed) 
    start_time = time.time()
    run_animation = True
    animate_runner('Kernu', current_positions['Kernu'], speed, step_size, interval, 'bo', 600)  

#kumpikin juoksee
def start_both_runners():
    global start_time, run_animation
    run_animation = True
    current_positions['Ernu'] = 0
    current_positions['Kernu'] = 0
    ernu_juoksee()
    kernu_juoksee()

# pääikkuna
ikkuna=tk.Tk() #luodaan ikkuna
ikkuna.title("Juoksukilpailu") #ikkunan otsikko
ikkuna.geometry("600x600+500+300") #määritellään ikkunan koko ja sijainti

# sijainti ja animaatio
current_positions = {
    'Ernu': 0,
    'Kernu': 0
}
run_animation_ernu = False
start_time_ernu = 0

# luodaan kuvaaja
fig=Figure(figsize=(5,5), dpi=100)
ax=fig.add_subplot(111)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel("Metrit")
ax.set_yticklabels([])


# upotetaan kuvaaja tkinteriin
kuvaaja_canvas=FigureCanvasTkAgg(fig, master=ikkuna)
kuvaaja_canvas.draw()
kuvaaja_canvas.get_tk_widget().place(x=10, y=100)

# napit
ernuNappi=tk.Button(ikkuna, text="Ernu", command=ernu_juoksee)
ernuNappi.place(x=200, y=60)

kernuNappi=tk.Button(ikkuna, text="Kernu", command=kernu_juoksee)
kernuNappi.place(x=100, y=60)

yhteisJuoksuNappi=tk.Button(ikkuna, text="Yhteisjuoksu", command=start_both_runners)
yhteisJuoksuNappi.place(x=300, y=60)

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