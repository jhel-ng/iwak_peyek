from scipy import*
import scipy.constants as scon
from numpy import*
from cmath import sqrt as sr
e1=zeros((1000),dtype=complex)
x1=zeros(1000)
#=====INPUT Parameter=====================================================================================
nxd=1000
w=50.0e-6
beta=1.5459603354640965
#---nc=ref index Cladding, nf=ref index film, ns=ref index substrat---------------------------------------
nc=1.55e0
nf=1.5525e0
ns=1.55e0
wle=0.5145e-6
df=2.0e-6
dff=0.5*df
k0=2*pi/wle
mu0=scon.mu_0
c0=scon.c
n01=beta
pw1=3.0e0
pw2=0.6e0
pw3=1.0e0
gap=0.0e0
dl1=250.0e-6
dl=dl1+dl1
#=========================================================================================================
def refrac():
	for i in range(1,nxd-1,1):
#=====dl1=================================================================================================
		if z<dl1:
			alpha(i)=0.0e0
#-------df ke-11------------------------------------------------------------------------------------------
#--------sudut tetha=0.6 deg=0.010472 rad-----------------------------------------------------------------
			if x(i)<((z-dl1)*0.010472-(df+gap)):
				refr1=nc**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==((z-dl1)*0.010472-(df+gap)):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
			elif x(i)<((z-dl1)*0.010472-gap):
				refr1=nf**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==((z-dl1)*0.010472-gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
#-------df ke-12------------------------------------------------------------------------------------
			elif x(i)<(-z*0.0+gap):
				refr1=nc**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(-z*0.0+gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
			elif x(i)<(-z*0.0+df+gap):
				refr1=nf**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(-z*0.0+df+gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
			else
				refr1=nc**2-n01**2
				alpha(i)=0.0e0
		else
#=====dl2==================================================================================================
#-------df ke-21------------------------------------------------------------------------------------------
			if x(i)<(-(z-dl1)*0.010472-(df+gap)):
				refr1=nc**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(-(z-dl1)*0.010472-(df+gap)):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
			elif x(i)<(-(z-dl1)*0.010472-gap):
				refr1=nf**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(-(z-dl1)*0.010472-gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
#-------df ke-22-------------------------------------------------------------------------------------------
			elif x(i)<(z*0.0+gap):
				refr1=nc**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(z*0.0+gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
			elif x(i)<(z*0.0+df+gap):
				refr1=nf**2-n01**2
				alpha(i)=0.0e0
			elif x(i)==(z*0.0+df+gap):
				refr1=(nc**2+nf**2)/2-n01**2
				alpha(i)=0.0e0
		refi1=0.0
		retcl1(i)=complex(refr1,refi1)
		
	return refrac()