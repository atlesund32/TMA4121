"""
Forfatter: Atle Sund og Synne Alstergren
"""
import numpy as np
import matplotlib.pyplot as plt


k = 100 #diffusiviteten -> hvor effektiv varmespredningen er
nodes = 20 #antall noder
length = 100 #størrelse på grid
time = 10 #aniimasjonens tidsforløp
dx = length/nodes
dy = length/nodes

# tidssteget for simuleringen. NB! følger kravene for numerisk stabilitet
dt = min(dx**2 / (4*k), dy**2 / (4*k)) 

current_temp = np.zeros((nodes, nodes)) +20 #initialiserer et rutenett på 20 grader
current_temp[10,:] = 100 #Setter en "stang" i midten til 100 grader

#visualisering
fig, axis = plt.subplots()
pcm = axis.pcolormesh(current_temp, cmap = plt.cm.rainbow, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

#Simulasjon
counter = 0
while counter < time:
    #kopierer temperaturen fra forrige tidssteg
    previous_temp = current_temp.copy()
    for i in range(1, nodes -1):

        for j in range(1, nodes -1):
            #Forward Time-Centered Space metoden
            #d^2T /(dx**2)
            dd_ux = (previous_temp[i-1,j] - 2*previous_temp[i,j] + previous_temp[i+1,j])/dx**2
            #d^2T /(dy**2)
            dd_uy = (previous_temp[i,j-1] - 2*previous_temp[i,j] + previous_temp[i,j+1])/dy**2
            current_temp[i,j] = dt * k * (dd_ux + dd_uy) + previous_temp[i,j]
            current_temp[10,:] = 100 #holder den midterste stangen ved konstant 100 grader
    counter += dt
    
    pcm.set_array(current_temp) #oppdaterer varmefordelingen
    axis.set_title("Varmefordeling ved tid t:{:.2f} [s]".format(counter))
    plt.pause(0.01) #pauser for å bedre visualiseringen
plt.show()