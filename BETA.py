#=======INPUT Parameter=====================================================================================
#---n1=ref index Core, n2=ref index cladding kiri, n3=ref index cladding kanan---------------------------
from scipy import*
n1=1.55e0
n2=1.545e0
n3=1.545e0
wle=1.55e-6
nmoda=1
range=4000
lim=(n1)-0.00001
kk=0
k=1
#
#=======mencari fx1(x)====================================================================================
def fx1(x):
	vf1=k0*sqrt(n1*n1-n2*n2)
	vf2=k0*sqrt(n1*n1-n3*n3)
	fx1=fx1=2.0e0*t*k0*sqrt(n1*n1-x*x)-(arctan(sqrt(vf1*vf1-k0*k0*(n1*n1-x*x))/(k0*sqrt(n1*n1-x*x))))-(arctan(sqrt(vf2*vf2-k0*k0*(n1*n1-x*x))/(k0*sqrt(n1*n1-x*x))))-kk*pi
	return fx1			
#=======mencari dne=======================================================================================
def dne():
	a=(n2)+0.0000001
	b=(n1)
	e=1.0e-10
	npn=(log10((b-a)/e))/(log10((2.0e0)+0.5e0))
	fa=fx1(a)
	for m in (i,npn):
		c=(a+b)/2.0e0
		fc=fx1(c)
	if (fa*fc)<0.0:
		b=c
	else:
		a=c
	dne=c
	return dne
#=======Perhitungan LOOP Moda-moda--- MAIN PROGRAM========================================================
for i in (kk,nmoda):
	df=0.5e-6
	for j in (k,range):
		df=df+0.01e-6
		k0=2*pi/wle
		t=df/2.0
		if dne()<lim:
			print(df,dne)
#			write
	
