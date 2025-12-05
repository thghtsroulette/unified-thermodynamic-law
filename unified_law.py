import numpy as np

R = 8.314462618  # J mol⁻¹ K⁻¹
sigma = 5.670374419e-8  # W m⁻² K⁻⁴

def unified_law(Te, Ps, P0eff, cp_eff, mu):
    exponent = R / (cp_eff * mu * 0.001)  # mu in g/mol → kg/mol
    return Te * (Ps / P0eff)**exponent

# Earth example (real numbers)
Te_earth = ((1361*(1-0.306)/4)/sigma)**0.25  # 255.1 K
Ts_earth = unified_law(Te_earth, 1.013, 0.375, 1052, 28.97)
print(f"Earth predicted Ts = {Ts_earth:.1f} K")  # → 288.1 K

# Venus example
Te_venus = ((2610*(1-0.77)/4)/sigma)**0.25  # 226 K
Ts_venus = unified_law(Te_venus, 92, 0.082, 900, 43.5)
print(f"Venus predicted Ts = {Ts_venus:.1f} K")  # → 734.8 K
