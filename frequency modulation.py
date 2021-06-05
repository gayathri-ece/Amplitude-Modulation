import numpy as np
import matplotlib.pyplot as plt

Am=float(input('Enter Modulating Signal amplitude : '))
Ac=float(input('Enter Carrier Signal amplitude : '))
fm=float(input('Enter Modulating Signal frequency : '))
fc=float(input('Enter Carrier Signal frequency : '))
d=float(input('Enter Frequency deviation : '))
mi=d/fm
t=np.linspace(0,5,1000)
carrier=Ac*np.sin(2*np.pi*fc*t)
modulating=Am*np.sin(2*np.pi*fm*t)
modulated=Ac*np.cos(2*np.pi*fc*t+mi*np.sin(2*np.pi*fm*t))

plt.subplot(3,1,1)
plt.plot(modulating,'r')
plt.title('Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3,1,2)
plt.plot(carrier,'b')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3,1,3)
plt.plot(modulated,'g')
plt.title('Frequency Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)
