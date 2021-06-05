import numpy as np
import matplotlib.pyplot as plt
while(True):
    Am=float(input("Enter Modulating Signal Amplitude : "))
    Ac=float(input("Enter Carrier Signal Amplitude : "))
    fm=float(input("Enter Modulating Signal Frequency : "))
    fc=float(input("Enter Carrier Signal Frequency : "))
    mi=float(input("Enter Modulation Index : "))
    if(mi>=0 and mi<=1):
        break
    else:
        print("Please enter modulation index value in range of 0 and 1")
t=np.linspace(0,5,1000)
carrier=Ac*np.sin(2*np.pi*fc*t)
modulating=Am*np.sin(2*np.pi*fm*t)
modulated=Ac*(1+mi*np.sin(2*np.pi*fm*t))*np.sin(2*np.pi*fc*t)

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
plt.title('Amplitude Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)
