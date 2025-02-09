import numpy as np
import matplotlib.pyplot as plt
data=np.load('micro69.npy')
lonlats=np.load('micro69xy.npy')

dt=0.002;
[nt,nx]=data.shape

for ii in lonlats:
	plt.plot(float(ii[0]),float(ii[1]),'v',color='r',markersize=15)
plt.ylabel('Latitude (deg)'); plt.xlabel('Longitude (deg)');plt.title('Coordinates of the 69 stations');
plt.savefig('micro69xy.png')
plt.show()

plt.imshow(data,aspect='auto',clim=(-0.02, 0.02),extent=[0,nx,dt*(nt-1),0]);
plt.ylabel('Time (s)'); plt.xlabel('Station NO #');plt.title('Irregular data to be interpolated');
plt.savefig('micro69.png')
plt.show()

