from thermopy.iapws import Water

T_db = 25
T_wb = 20

def P_sat(T,P_c=22.10,T_c=647.3):
    k = 4.39553-6.2442*(T/1000) + 9.953*(T/1000)**2 - 5.151*(T/1000)**3
    return P_c*10**(k*(1-T_c/T))*1000

Pg_db = P_sat(T_db+273)
Pg_wb = P_sat(T_wb+273)

omega_prime = 0.622*Pg_wb/(101.3-Pg_wb)

ha_wb = 1.005*T_wb
ha_db = 1.005*T_db
hw_wb = 4.186*T_wb
hg_db = 2501.7 + 1.82*T_db
hg_wb = 2501.7 + 1.82*T_wb

omega = (ha_wb - ha_db + omega_prime*(hg_wb-hw_wb)) / (hg_db - hw_wb)
rh = omega*101.325/(0.622*Pg_db + omega*Pg_db)
h = ha_db + omega*hg_db
P_v = rh*Pg_db
w = Water(P_v*1000,T_db+273)
T_dp = w.temperature_saturation(P_v*1000)

print(f'{Pg_db}\n{Pg_wb}')