# # import matplotlib.pyplot as plt
# # from sklearn.cluster import KMeans
# # from sklearn.datasets import make_blobs  # Example dataset
# # import matplotlib.animation as animation

# # # Generate sample data (replace with your actual dataset)
# # X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# # # Create a figure and axes for the plots
# # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# # # Lists to store inertia values and K values
# # inertia = []
# # k_values = range(1, 11)  # Test K values from 1 to 10


# # # Function to update the plots for each frame of the animation
# # def animate(i):
# #     global inertia
# #     k = k_values[i]
# #     kmeans = KMeans(n_clusters=k, random_state=42)
# #     kmeans.fit(X)
# #     inertia.append(kmeans.inertia_)

# #     # Update the elbow plot
# #     ax1.clear()
# #     ax1.plot(k_values[: i + 1], inertia[: i + 1], marker="o")
# #     ax1.set_title("Elbow Method for Optimal k")
# #     ax1.set_xlabel("Number of Clusters (k)")
# #     ax1.set_ylabel("Inertia")

# #     # Update the cluster visualization plot
# #     ax2.clear()
# #     ax2.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
# #     ax2.set_title(f"K-means Clustering (k={k})")
# #     ax2.set_xlabel("Feature 1")
# #     ax2.set_ylabel("Feature 2")


# # # Create the animation
# # ani = animation.FuncAnimation(
# #     fig, animate, frames=len(k_values), interval=500, blit=False
# # )

# # plt.tight_layout()
# # plt.show()

# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs  # Example dataset
# import matplotlib.animation as animation

# # Generate sample data (replace with your actual dataset)
# X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# # Create a figure and axes for the plots
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# # Lists to store inertia values and K values
# inertia = []
# k_values = range(1, 11)  # Test K values from 1 to 10


# # Function to update the plots for each frame of the animation
# def animate(i):
#     global inertia
#     k = k_values[i]
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X)
#     inertia.append(kmeans.inertia_)

#     # Update the elbow plot
#     ax1.clear()
#     ax1.plot(k_values[: i + 1], inertia, marker="o")
#     ax1.set_title("Elbow Method for Optimal k")
#     ax1.set_xlabel("Number of Clusters (k)")
#     ax1.set_ylabel("Inertia")

#     # Update the cluster visualization plot
#     ax2.clear()
#     ax2.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
#     ax2.set_title(f"K-means Clustering (k={k})")
#     ax2.set_xlabel("Feature 1")
#     ax2.set_ylabel("Feature 2")


# # Create the animation
# ani = animation.FuncAnimation(
#     fig, animate, frames=len(k_values), interval=500, blit=False
# )

# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs  # Example dataset
import matplotlib.animation as animation

# Generate sample data (replace with your actual dataset)
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# Create a figure and axes for the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Lists to store inertia values and K values
inertia = []
k_values = range(1, 11)  # Test K values from 1 to 10


# Function to update the plots for each frame of the animation
def animate(i):
    global inertia
    k = k_values[i]
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

    # Update the elbow plot
    ax1.clear()
    ax1.plot(k_values[: i + 1], inertia[: i + 1], marker="o")
    ax1.set_title("Elbow Method for Optimal k")
    ax1.set_xlabel("Number of Clusters (k)")
    ax1.set_ylabel("Inertia")

    # Update the cluster visualization plot
    ax2.clear()
    ax2.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
    ax2.set_title(f"K-means Clustering (k={k})")
    ax2.set_xlabel("Feature 1")
    ax2.set_ylabel("Feature 2")


# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=len(k_values), interval=500, blit=False
)

plt.tight_layout()
plt.show()
