from scipy import*
import scipy.constants
#=======INPUT Parameter===================================================================================
nxd=1000
w=50.0e-6
beta=1.5459603354640965
#---nc=ref index Cladding, nf=ref index film, ns=ref index substrat---------------------------------------
nc=1.55e0
nf=1.5525e0
ns=1.55e0
emax1=0.0e0
wle=0.5145e-6
df=2.0e-6
dff=0.5*df
k0=2*pi/wle
mu0=scipy.constants.mu_0
c0=scipy.constants.c
pw1=3.0e0
pw2=0.6e0
pw3=1.0e0
kap1=k0*sqrt((nf**2)-(beta**2))
gam1=k0*sqrt((beta**2)-(nc**2))
del1=k0*sqrt((beta**2)-(ns**2))
arg1=-del1/kap1
#=========================================================================================================
def input123():
#====INPUT 1==============================================================================================
	ampn1=4.0e0*(kap1**2)*c0*mu0*pw1
	ampd1=beta*(df+(1.0e0/gam1)+(1.0e0/del1))*((kap1**2)+(del1**2))
	amps1=ampn1/ampd1
	amp1=sqrt(amps1)
	ad1=amp1*(cos(kap1*df)-arg1*sin(kap1*df))
#---Posisi INPUT I LASER----------------------------------------------------------------------------------
	xr0=10.0e-6
#---------------------------------------------------------------------------------------------------------
	for i in range(0,400,1):
		x(i)=((nxd-(i))*(-w/2.0e0)+(i)*(w/2.0e0))/(nxd)
		xr=x(i)+xr0
		if xr<(-df):
			er1=ad1*exp(gam1*(xr+df))
			ei1=0.0e0
		elif xr<=(0.0e0):
			er1=(amp1*(cos(kap1*xr)+arg1*sin(kap1*xr)))
			ei1=0.0e0
		else:
			er1=amp1*exp(-del1*xr)
			ei1=0.0e0
		ef1=((er1**2)+(ei1*2))
		ecom1=abs(ef1)
		if ecom1>emax1:
			emax1=ecom1
		e1(i)=complex(er1,ei1)
		e1=e1(i)
	return e1
#===INPUT 2===============================================================================================
	ampn1=4.0e0*(kap1**2)*c0*mu0*pw2
	ampd1=beta*(df+(1.0e0/gam1)+(1.0e0/del1))*((kap1**2)+(del1**2))
	amps1=ampn1/ampd1
	amp1=sqrt(amps1)
	ad1=amp1*(cos(kap1*df)-arg1*sin(kap1*df))
#---Posisi INPUT II LASER---------------------------------------------------------------------------------
	xr0=6.0e-6
#---------------------------------------------------------------------------------------------------------
	for i in range(401,500,1):
		x(i)=((nxd-(i))*(-w/2.0e0)+(i)*(w/2.0e0))/(nxd)
		xr=x(i)+xr0
		if xr<(-df):
			er1=ad1*exp(gam1*(xr+df))
			ei1=0.0e0
		elif xr<=(0.0e0):
			er1=(amp1*(cos(kap1*xr)+arg1*sin(kap1*xr)))
			ei1=0.0e0
		else:
			er1=amp1*exp(-del1*xr)
			ei1=0.0e0
		ef1=((er1**2)+(ei1*2))
		ecom1=abs(ef1)
		if ecom1>emax1:
			emax1=ecom1
		e1(i)=complex(er1,ei1)
		e1=e1(i)
	return e1
#===INPUT 3===============================================================================================
	ampn1=4.0e0*(kap1**2)*c0*mu0*pw3
	ampd1=beta*(df+(1.0e0/gam1)+(1.0e0/del1))*((kap1**2)+(del1**2))
	amps1=ampn1/ampd1
	amp1=sqrt(amps1)
	ad1=amp1*(cos(kap1*df)-arg1*sin(kap1*df))
#---Posisi INPUT III LASER--------------------------------------------------------------------------------
	xr0=-6.0e-6
#---------------------------------------------------------------------------------------------------------
	for i in range(501,nxd,1):
		x(i)=((nxd-(i))*(-w/2.0e0)+(i)*(w/2.0e0))/(nxd)
		xr=x(i)+xr0
		if xr<(-df):
			er1=ad1*exp(gam1*(xr+df))
			ei1=0.0e0
		elif xr<=(0.0e0):
			er1=(amp1*(cos(kap1*xr)+arg1*sin(kap1*xr)))
			ei1=0.0e0
		else:
			er1=amp1*exp(-del1*xr)
			ei1=0.0e0
		ef1=((er1**2)+(ei1*2))
		ecom1=abs(ef1)
		if ecom1>emax1:
			emax1=ecom1
		e1(i)=complex(er1,ei1)
		e1=e1(i)
	return e1
	
print(el)