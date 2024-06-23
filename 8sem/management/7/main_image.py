import skimage
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = imread('cars2.jpg')
# plt.imshow(image)
# plt.show()

image2 = skimage.img_as_float(image)
print(image2.shape)

image3 = np.reshape(image2, newshape=(image2.shape[0] * image2.shape[1], image2.shape[2]))
print(image3)

kmeans = KMeans(n_clusters=10, random_state=242, init='k-means++').fit(image3)
print(kmeans.labels_)

image4 = image3.copy()

# image4[:, 0] = np.where(np.isin(kmeans.labels_, [0, 3, 5, 6]), 255, np.where(np.isin(kmeans.labels_, [1, 2, 4]), 0, 100))
# image4[:, 1] = np.where(np.isin(kmeans.labels_, [1, 3, 4, 6]), 255, np.where(np.isin(kmeans.labels_, [0, 2, 5]), 0, 100))
# image4[:, 2] = np.where(np.isin(kmeans.labels_, [2, 4, 5, 6]), 255, np.where(np.isin(kmeans.labels_, [0, 1, 3]), 0, 100))


image4[:, 0] = np.where(np.isin(kmeans.labels_, [0, 3, 6, 8]), 255, np.where(np.isin(kmeans.labels_, [1, 2, 5]), 0, 100))
image4[:, 1] = np.where(np.isin(kmeans.labels_, [1, 4, 6, 9]), 255, np.where(np.isin(kmeans.labels_, [0, 3, 2]), 0, 100))
image4[:, 2] = np.where(np.isin(kmeans.labels_, [2, 5, 7, 9]), 255, np.where(np.isin(kmeans.labels_, [0, 5, 7]), 0, 100))

# image4[:, 0] = np.where(np.isin(kmeans.labels_, [0, 2, 4]), 255, np.where(np.isin(kmeans.labels_, [1, 3]), 0, 100))
# image4[:, 1] = np.where(np.isin(kmeans.labels_, [1, 3, 4]), 255, np.where(np.isin(kmeans.labels_, [0, 2]), 0, 100))
# image4[:, 2] = np.where(np.isin(kmeans.labels_, [2, 3, 4]), 255, np.where(np.isin(kmeans.labels_, [0, 1]), 0, 100))

image5 = image4.reshape(image2.shape)
plt.imshow(image5 / 255)
plt.show()
