# This is my algorithm for the k-means machine learning model. My approach to this problem was to first do research
# on the topic and try to get an understanding of how it works. Although I found it very difficult, I now have a
# better understanding of how it all works together. It required using a lot of different resources in order to get
# it to work, and this is how I managed to piece together my solution, which I am happy with.

# Imports needed for the program to run.
import csv
import random
from math import sqrt
import matplotlib.pyplot as plt


# Function that computes the Euclidean distance between two different data points.
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Function that reads the data from the csv files
def read_csv_file(file):
    open_csv = open(file, 'r')
    read_file = csv.reader(open_csv, delimiter=',')
    next(read_file)

    csv_data = [[row[0], [float(row[1]), float(row[2])]] for row in read_file]

    open_csv.close()
    return csv_data


# Function that is used to calculate the mean of the data that is passed into it.
def calculate_mean(points):
    x_data, y_data = get_x_y_data(points)
    x = sum(x_data)
    y = sum(y_data)
    return [x / len(points), y / len(points)]


# Function that loops through the first and second elements in the data passed in, in order to get the 'x_data'
# and 'y_data'.
def get_x_y_data(points):
    x_data = [point[0] for point in points]
    y_data = [point[1] for point in points]
    return x_data, y_data


# Function that loops through each fo the cluster points in the data and returns a list of countries that belong to
# each cluster.
def get_countries(cluster_points, data):
    countries_list = []
    for i, value in enumerate(data):
        if value[1] in cluster_points:
            countries_list.append(data[i][0])
    return countries_list


# Function that plots the data and centroids on a chart.
def plot_data():
    for cluster in clusters:
        x, y = get_x_y_data(cluster)
        plt.scatter(x, y)

    for i in range(user_num_clusters):
        plt.scatter(centroids[i][0], centroids[i][1], marker="*", s=200, c="k")

    plt.xlabel("Birth rate (Per 1000)")
    plt.ylabel("Life expectancy")
    plt.title("Birth rate and life expectancy")
    plt.show()


# Function that generates a readable printout of the data.
def generate_output():
    print("-------------------------------")
    print("Total number of countries for each of the clusters.")
    print("-------------------------------\n")

    # Prints the number of countries that belong to each of the clusters.
    for num in range(user_num_clusters):
        print(f"Cluster {num}: {len(clusters[num])} has countries.")

    print("\n-----------------------------------")
    print("List of countries that belong to each of the clusters.")
    print("-----------------------------------\n")

    # Prints a list of countries that belong to each cluster
    for num in range(user_num_clusters):
        print(f"Cluster {num}: \n {get_countries(clusters[num], extracted_csv_data)}")

    print("\n-----------------------------------------------")
    print("The average birth rate and life expectancy for each cluster.")
    print("-----------------------------------------------\n")

    # Prints the average birth rate and average life expectancy for each cluster
    for num in range(user_num_clusters):
        print(f"Cluster {num}: The average birth rate is {round(centroids[num][0], 2)}; "
              f"The average life expectancy is {round(centroids[num][1], 2)}.")

    # Calling 'plot_data' to plot the data and centroids.
    plot_data()


# Function that lets the user select the csv file they want to use.
def choose_file():
    selected_file = int(input("Please type the number for the file you wish to "
                              "select from the options below."
                              "\n1. 'data1953.csv'"
                              "\n2. 'data2008.csv'"
                              "\n3. 'dataBoth.csv'"
                              "\nEnter your input here please: "))

    file = ""

    if selected_file == 1:
        file = "data1953.csv"
    elif selected_file == 2:
        file = "data2008.csv"
    elif selected_file == 3:
        file = "dataBoth.csv"
    else:
        print("Please enter a valid file selection only.")

    return file


# ========================
# Initialisation procedure
# ========================


# Read in data from a csv file
extracted_csv_data = read_csv_file(choose_file())

# Extract the birth rate and life expectancy form the data.
data_points = [list[1] for list in extracted_csv_data]

# Take in a user-defined number of clusters and iterations
user_num_clusters = int(input("Enter the number of clusters you would like: "))
user_num_iterations = int(input("Enter the maximum number of iterations you would like: "))

# Randomly select initial centroids from the data points
centroids = random.sample(data_points, user_num_clusters)

# ==================
# Implement the K-means algorithm
# ==================

# Sets the starting iterations to 0 as a way to exit the loop when it is the same as 'user_num_iterations'
iterations = 0

# Repeat while 'user_num_iterations' has not been reached
while True:

    # Increases iterations each time the while loop runs.
    iterations += 1

    # Stores the closest points to each cluster.
    clusters = [[] for i in range(user_num_clusters)]

    # Repeat for each data point in 'data_points'
    for point in data_points:

        # Stores the distances from each point to each centroid
        all_distances = []

        # Calculates the point's distance to each centroid
        for i in range(user_num_clusters):
            all_distances.append(euclidean_distance(centroids[i], point))

        # Assigns each point to its nearest centroid
        for i, value in enumerate(all_distances):
            if value == min(all_distances):
                clusters[i].append(point)

    # Calculates the mean for the new centroids
    for i in range(user_num_clusters):
        centroids[i] = calculate_mean(clusters[i])

    # Exits the while loop if the number of iterations has reached 'user_num_iterations'.
    if iterations == user_num_iterations:
        print(f"All {user_num_clusters} iterations have been completed, below are the results after all iterations.")
        break

# Calls 'generate_output' to print the outputs and plot the data with the centroid.
generate_output()

# Refences I made use of.
# https://www.youtube.com/watch?v=EItlUEPCIzM&t=7s
# https://www.youtube.com/watch?v=fl0PH6uQDIw
# https://www.youtube.com/watch?v=iNlZ3IU5Ffw
# https://www.youtube.com/watch?v=9991JlKnFmk&t=1515s

# https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a
# https://towardsdatascience.com/k-means-clustering-how-it-works-finding-the-optimum-number-of-clusters-in-the-data-13d18739255c