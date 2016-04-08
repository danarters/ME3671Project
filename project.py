#trey, insert puns here
from math import *
F_app = 39.21
Handle_r = 6.
n_1 = 84.
T_in = F_app*Handle_r
hp_in = T_in*n_1*2.*(3.1415926)/(12.*33000.)

def printNumbers(gear):
	for (name, number) in gear.iteritems():
		print chr(9),name, ' : ', number

#DANS MECHANISM
vel_ratio = 4.
P_d = 10.
b = 1.
p_angle = 20.
K_a = 1.25
K_m = 1.6
K_l = 1.
Q = 8.
K_v = 1.05
R_g = 1.0 # 99% reliable 
num_cycles = (365.*8.*60.*84.) #assuming maximum operation would be 1/4 the time
v = 0.3
E = 30.*10.**6.
G = 11.5*10.**6.
S_u = 80000
S_f = S_u/2.

allowable_stress = S_u-((S_u-S_f)/log(10.**10., 10.))*log(num_cycles, 10.)
print 'allowable stress = ', allowable_stress, chr(10)


print 'material = '
print 'b = ', b

gear1 = {}
gear2 = {}

gear1['teeth'] = 21.
gear2['teeth'] = gear1['teeth']*vel_ratio

gear1['rpm'] = n_1
gear2['rpm'] = gear1['rpm']/vel_ratio

gear1['radius'] = gear1['teeth']/(P_d*2.)
gear2['radius'] = gear2['teeth']/(P_d*2.)

gear1['J'] = 0.24
gear2['J'] = 0.28

gear1['tangential force'] = T_in/gear1['radius']
gear2['tangential force'] = T_in/gear2['radius']

gear1['base stress'] = gear1['tangential force']*P_d*K_m*K_v*K_l*K_a/(b*gear1['J'])
gear2['base stress'] = gear2['tangential force']*P_d*K_m*K_v*K_l*K_a/(b*gear2['J'])


mg = gear1['radius']/gear2['radius']

I = sin(p_angle*(pi/90.))*cos(p_angle*(pi/90.))*mg/(2.*(mg+1.))
Cp = sqrt(1./(pi*(((1.-(v**2.))/E))+((1.-(v**2.))/E)))

gear1['surface fatigue'] = Cp*sqrt(gear1['tangential force']/(b*2.*gear1['radius']*I)*K_a*K_v*K_m)
gear2['surface fatigue'] = Cp*sqrt(gear2['tangential force']/(b*2.*gear2['radius']*I)*K_a*K_v*K_m)

# gear1['base stress cycles'] = 10.**(S_u-gear1['base stress'])/((S_u-S_f)/log(10.^10.))
# gear2['base stress cycles'] = 10.**(S_u-gear2['base stress'])/((S_u-S_f)/log(10.^10.))

# gear1['surface fatigue cycles'] = 10.**(S_u-gear1['surface fatigue'])/((S_u-S_f)/log(10.^10.))
# gear2['surface fatigue cycles'] = 10.**(S_u-gear2['surface fatigue'])/((S_u-S_f)/log(10.^10.))


print 'gear 1: '
printNumbers(gear1)

print 'gear 2: '
printNumbers(gear2)


shaft_radius = 0.5 #maybe?
K_t = 1.3 # for annealed 1.6 for hardened
print 'shaft radius = ', shaft_radius

key1 = {}
key2 = {}

key1['l'] = 0.75
key2['l'] = 0.75 #assuming it should be marginally smaller than the gear width

key1['h'] = shaft_radius/2.
key2['h'] = shaft_radius/2.

key1['w'] = key1['h']
key2['w'] = key2['h']

key1['tangential force'] = gear1['tangential force']*gear1['radius']/shaft_radius
key2['tangential force'] = gear2['tangential force']*gear2['radius']/shaft_radius

key1['shear stress'] = 2.*key1['tangential force']*shaft_radius/(2.*shaft_radius*key1['w']*key1['l']*0.557)
key2['shear stress'] = 2.*key2['tangential force']*shaft_radius/(2.*shaft_radius*key2['w']*key2['l']*0.557)

key1['bearing stress'] = 4.*key1['tangential force']*shaft_radius/(2.*shaft_radius*key1['h']*key1['l'])
key2['bearing stress'] = 4.*key2['tangential force']*shaft_radius/(2.*shaft_radius*key2['h']*key2['l'])

# key1['allowable stress'] = 2.*shaft_radius*key1['w']*key1['l']*T_in/2.
# key2['allowable stress'] = 2.*shaft_radius*key2['w']*key1['l']*T_in/2.

allowable_shaft_stress = T_in*16.*K_t/(pi*((2.*shaft_radius)**3.))

print 'stress on the shaft: ', allowable_shaft_stress


# key1['shear stress cycles'] = 10.**(S_u-key1['shear stress'])/((S_u-S_f)/log(10.^10.))
# key2['shear stress cycles'] = 10.**(S_u-key2['shear stress'])/((S_u-S_f)/log(10.^10.))

# key1['bearing stress cycles'] = 10.**(S_u-key1['bearing stress'])/((S_u-S_f)/log(10.^10.))
# key2['bearing stress cycles'] = 10.**(S_u-key2['bearing stress'])/((S_u-S_f)/log(10.^10.))


print 'key 1: '
printNumbers(key1)

print 'key 2: '
printNumbers(key2)









