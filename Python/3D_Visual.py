import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

number_of_simulations = [1,2,3,4,5,6,7,8,9,10]
without_parallel = [1.0459461212158203,0.9269008636474609,0.8644118309020996,0.8547751903533936,1.0634522438049316,1.1338090896606445,1.1633098125457764,0.8137271404266357,0.8188397884368896,1.0041818618774414]
parallel = [0.002855062484741211,0.0012428760528564453,0.0009419918060302734,0.002145051956176758,0.0027589797973632812,0.0007748603820800781,0.000476837158203125,0.00039505958557128906,0.0005838871002197266,0.0030488967895507812]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(number_of_simulations, without_parallel, parallel, c='r', marker='x')

ax.set_xlabel('Number of simulations')
ax.set_ylabel('Without Parallel')
ax.set_zlabel('Parallel')
ax.set_title('3D Visualization')
plt.show()