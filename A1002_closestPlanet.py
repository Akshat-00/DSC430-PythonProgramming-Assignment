# Name: Akshat Gaur
# Student ID: 2176685
# Date : 11/21/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/RxR1d80wpfw

import pandas as pd
import matplotlib.pyplot as plt
from A1001_planet import Planet,distance

def simulateThousandYears(planets,p_name,days):
    """
    Calls distance from planet to compute distance b/w each pair of planets
    Updates the matrix with the average distance values
    Returns the matrix
    """
    num_planets = len(planets)                                     
    distances = [[0] * num_planets for _ in range(num_planets)]     # Creating a 2-D Matrix and filling it with 0

    for day in days:
        for i in range(num_planets):
            for j in range(i + 1, num_planets):
                dist = distance(planets[i], planets[j], day)        # Calling distance function from planet
                distances[i][j] += dist                             # Updating matrix with distance value
                distances[j][i] += dist

    # Calculate average distances
    for i in range(num_planets):
        for j in range(i + 1, num_planets):
            distances[i][j] /= len(days)
            distances[j][i] /= len(days)
    
    printAvgDistanceMatrix(distances, p_name)                       # Print the average distance matrix

def printAvgDistanceMatrix(average_distances, planet_names):
    """
    Prints the 8*8 chart
    """
    # Print the matrix with each row on a separate line
    print("Average Distance Matrix (in CM):\n")
    print("\t" + "\t".join(planet_names))
    
    for i, row_name in enumerate(planet_names):
        row_data = f"{row_name}\t"
        for j, col_name in enumerate(planet_names):
            row_data += f"{average_distances[i][j]:.2f}\t"
        print(row_data)

def simulateThousandDays(mercury,venus,mars,earth,days,data):
    """
    Calculates the distance between mercury, venus, mars & earth over a span of 1000 days
    """
    for d in days:
        distance_mercury = distance(mercury, earth, d)              # Distance between mercury and earth
        distance_venus = distance(venus, earth, d)                  # Distance between venus and earth
        distance_mars = distance(mars, earth, d)                    # Distance between mars and earth

        # Appends the distance for each day in different columns
        data['Distance to Mercury'].append(distance_mercury)
        data['Distance to Venus'].append(distance_venus)
        data['Distance to Mars'].append(distance_mars)
    
    return data

def plot(df):
    """
    Plots the distance from Earth to Mercury, Venus, and Mars over time.
    """
    
    plt.figure(figsize=(12, 6))                                                 # Size of plot

    for planet in ["Mercury", "Venus", "Mars"]:
        plt.plot(df['Day'], df[f'Distance to {planet}'], label=planet)          # Plot distance for each planet

    plt.xlabel("Days")                                                          # X axis
    plt.ylabel("Distance from Earth")                                           # Y axis
    plt.title("Distance from Earth to Mercury, Venus, and Mars over 1000 Days") # Title of plot
    plt.legend()                                                                # Legend of the plot
    plt.savefig("planet_plot.png") 
    plt.show()                                                                  # Display plot                                                                  

def main():

    # Creating instances of planets
    mercury = Planet(3.5, 88)
    venus = Planet(6.7, 225)
    earth = Planet(9.3, 365)
    mars = Planet(14.2, 687)
    jupiter = Planet(48.4, 4333)
    saturn = Planet(88.9, 10759)
    uranus = Planet(179, 30687)
    neptune = Planet(288, 60190)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune] 
    planets_name = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

    # Simulation for 1000 years
    print("Simulation for 1000 years\n")

    days = range(1000*365)
    simulateThousandYears(planets,planets_name, days)     # Computing average distance between each pair of planets

    # Simulation for 1000 days
    print("\nSimulation for 1000 Days")

    days = range(1000)
    data = {'Day': days, 'Distance to Mercury': [], 'Distance to Venus': [], 'Distance to Mars': []}
    distance_data = simulateThousandDays(mercury,venus,mars,earth,days,data)

    df = pd.DataFrame(distance_data)                            # Creating a DataFrame and writing to CSV
    df.to_csv("daily_distances.csv", sep='\t', index=False)     # Writing distances to a CSV file

    plot(df)                                                    # Plotting time series

if __name__ == "__main__":
    main()

