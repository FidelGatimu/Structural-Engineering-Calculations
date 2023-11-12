import math
class CTInput:
    def __init__(self, default):
        self.default = default
        self.value = default  # Set the default value initially

class Input:
    # Input parameters
    t = CTInput(default=160.0)
    b = CTInput(default=230.0)
    h = CTInput(default=350.0)
    l = CTInput(default=6300.0)
    fck = CTInput(default=20.0)
    γc = CTInput(default=1.5)
    fyk = CTInput(default=500.0)
    γs = CTInput(default=1.15)
    a1 = CTInput(default=300.0)
    a2 = CTInput(default=300.0)
    ψ2 = CTInput(default=0.3)

    # Constants
    width = 0.2  # Constant width
    depth = 0.4  # Constant depth

# Get user inputs or use default values
input_data = Input()

# You can replace these inputs with user-provided values
input_data.t.value = float(input("Enter the thickness (t), press Enter to use default: ") or input_data.t.default)
input_data.b.value = float(input("Enter the width (b), press Enter to use default: ") or input_data.b.default)
input_data.h.value = float(input("Enter the height or depth (h), press Enter to use default: ") or input_data.h.default)
input_data.l.value = float(input("Enter the length (l), press Enter to use default: ") or input_data.l.default)
input_data.fck.value = float(input("Enter the characteristic compressive strength of concrete (fck), press Enter to use default: ") or input_data.fck.default)
input_data.γc.value = float(input("Enter the partial safety factor for concrete (γc), press Enter to use default: ") or input_data.γc.default)
input_data.fyk.value = float(input("Enter the characteristic yield strength of steel (fyk), press Enter to use default: ") or input_data.fyk.default)
input_data.γs.value = float(input("Enter the partial safety factor for steel (γs), press Enter to use default: ") or input_data.γs.default)
input_data.a1.value = float(input("Enter the distance a1, press Enter to use default: ") or input_data.a1.default)
input_data.a2.value = float(input("Enter the distance a2, press Enter to use default: ") or input_data.a2.default)
input_data.ψ2.value = float(input("Enter the factor ψ2, press Enter to use default: ") or input_data.ψ2.default)

# Checking the values
#print(f"Thickness (t): {input_data.t.value}")
#print(f"Width (b): {input_data.b.value}")
#print(f"Height or Depth (h): {input_data.h.value}")
#print(f"Length (l): {input_data.l.value}")
#print(f"Concrete Strength (fck): {input_data.fck.value}")
#print(f"Partial Safety Factor for Concrete (γc): {input_data.γc.value}")
#print(f"Steel Yield Strength (fyk): {input_data.fyk.value}")
#print(f"Partial Safety Factor for Steel (γs): {input_data.γs.value}")
#print(f"Distance a1: {input_data.a1.value}")
#print(f"Distance a2: {input_data.a2.value}")
#print(f"Factor ψ2: {input_data.ψ2.value}")



# Given values
#t = 160  # mm
b = 230  # mm
h = 350  # mm
l = 6300  # 
fck = 20  # N/mm^2
γc = 1.5
fyk = 500  # N/mm^2
γs = 1.15
a1 = 300  # mm
a2 = 300  # mm
ψ2 = 0.3

# Effective length
leff = l + min(a1, a2) / 2

# Load and effects
SWb = h * b * 25 / (10 ** 6)  # kN/m
SWc = 1.5  # kN/m
gk = 3.513  # kN/m
γg = 1.35
gd = γg * gk
qk = 2  # kN/m
γq = 1.5
qd = γq * qk
ped = gd + qd
pqp = gk + ψ2 * qk

# Design reinforcement at mid-span
Med = 31.82  # kN·m
Cc = 25  # mm
η = 10  # mm
d = min(300, 0.9 * h - Cc, 50)  # mm
d_prime = 50  # mm
fcd = fck / γc
fyd = fyk / γs

# Compatibility for plastic analysis
ξ_prime_co = 560 / (700 - fyd)
ξ_co = 560 / (700 + fyd)
x_co = ξ_co * d
α = 1
Mu = x_co * b * α * fcd * ((d - x_co) / 2)
xc = d - math.sqrt(d**2 - (2 * Mu) / (b * fcd))

# Requirement steel area
ϕ = 12  # mm
ϕ_sw = 6  # mm
Asreq = xc * b * α * fcd / fyd
Arebars = math.pi * (ϕ**2) / 4
n = Asreq / Arebars
As = Arebars * n

# Provide depth
d_real = h - Cc - ϕ_sw - η
x_creall = As * fyd / (b * α * fcd)

# Display results
print(f"Effective Length (leff): {leff} mm")
print(f"Load Combination for ULS Analysis (ped): {ped} kN/m")
print(f"Load Combination for SLS Analysis (pqp): {pqp} kN/m")
print(f"Design Reinforcement at Mid-Span (Med): {Med} kN·m")
print(f"Real Depth (d_real): {d_real} mm")
print(f"Real Neutral Axis (x_creall): {x_creall} mm")

# Given values for the second part of the design
Med_support = 80.80  # kN·m

# Effective depth for support
d_support = min(300, 0.9 * h - Cc, 50)
d_prime_support = 50

# Design strength for support
fcd_support = fck / γc
fyd_support = fyk / γs

# Compatibility for plastic analysis for support
ξ_prime_co_support = 560 / (700 - fyd_support)
ξ_co_support = 560 / (700 + fyd_support)
x_co_support = ξ_co_support * d_support
Mu_support = x_co_support * b * α * fcd_support * ((d_support - x_co_support) / 2)
xc_support = d_support - math.sqrt((d_support**2) - (2 * Mu_support) / (b * fcd_support))

# Requirement steel area for support
Asreq_support = xc_support * b * α * fcd_support / fyd_support
Arebars_support = math.pi * (ϕ**2) / 4
n_support = Asreq_support / Arebars_support
As_support = Arebars_support * n_support

# Provide depth for support
d_real_support = h - Cc - ϕ_sw - η
x_creall_support = As_support * fyd_support / (b * α * fcd_support)

# Plasticity check for support
ρsl_support = As_support / (b * d_real_support)
fctm_support = 0.3 * math.sqrt(fck)
ρs1min_support = max(0.13 / 100, 0.26 * (fctm_support / fyk) / 1000)
ρslmax_support = 4 / 100
ζ_support = max(20, ϕ)  # mm
bmin_support = 2 * (Cc + ϕ_sw + ζ_support) * n_support * ϕ * ((n_support - 1) / n_support)
Mrd_support = x_creall_support * b * α * fcd_support * ((d_real_support - x_creall_support) / 2)
performance_support = Med_support / Mrd_support

# Display results for support
print("\nSupport Design:")
print(f"Real Depth (d_real_support): {d_real_support} mm")
print(f"Real Neutral Axis (x_creall_support): {x_creall_support} mm")
print(f"Plasticity Check: {x_creall_support / d_real_support:.3f}")
print(f"Required Steel Area (As_support): {As_support} mm2")
print(f"Number of Rebars (n_support): {n_support}")
print(f"Performance: {performance_support:.3f}")

# Given values for the third part
Ved = 50.09  # kN
d_shear = 303  # mm

# Additional variables for the third part
αcw = 1.0

# Shear design
K = min(1 + (200 / d_shear), 2.0)
bw_shear = 230  # mm
ρρ_shear = min(As_support / (bw_shear * d_shear), 0.02)
ν = 0.6 * (1 - fck / 250) ** 0.5
VRdc_shear = min(27.77, 0.18 / γc * K * (100 * ρρ_shear * fck) ** (1 / 3) / (bw_shear * d_shear * ν) ** 0.5)
Mrd_shear = x_creall_support * bw_shear * α * fcd_support * ((d_real_support - x_creall_support) / 2)
performance_shear = Med_support / Mrd_shear

# Shear reinforcement
ϕ_sw_shear = 6  # mm
Asw_shear = 2 * math.pi * (ϕ_sw_shear ** 2) / 4
Sreq_shear = Asw_shear * fyd_support / Ved
Z_shear = 0.9 * d_shear
VRdmax_shear = αcw * bw_shear * Z_shear * ν * fcd_support * 0.5 / 1000  # kN
ρwmin = 0.08 * fck / fyk / 7.155e-4
ρwmax = 0.5 * αcw / ((1 - math.cos(0.5 * math.pi))) / fcd_support / ν / 0.008
Smin_shear = Asw_shear / (ρwmax * bw_shear)
Smax1_shear = 0.75 * d_shear
Smax2_shear = Asw_shear / (ρwmin * bw_shear)
Smax_shear = min(Smax1_shear, Smax2_shear)
Sprovide_shear = 220  # mm

# Stirrups space
Sprovide_middle_span = 220  # mm
Sprovide_support = 120  # mm

# Display results for shear design
print("\nShear Design:")
print(f"Shear Force (Ved): {Ved} kN")
print(f"Design Size Factor (K): {K}")
print(f"Reinforcement Ratio (ρρ): {ρρ_shear}")
print(f"Concrete Shear Stress (ν): {ν}")
print(f"Design Shear Resistance (VRdc): {VRdc_shear} kN")
print(f"Required Shear Resistance (Mrd_shear): {Mrd_shear} kN·m")
print(f"Performance: {performance_shear:.3f}")

# Display results for shear reinforcement
print("\nShear Reinforcement:")
print(f"Shear Reinforcement Area (Asw): {Asw_shear} mm2")
print(f"Required Shear Reinforcement Spacing (Sreq): {Sreq_shear} mm")
print(f"Maximum Design Shear Resistance (VRdmax): {VRdmax_shear} kN")
print(f"Minimum Stirrups Spacing (Smin): {Smin_shear} mm")
print(f"Maximum Stirrups Spacing (Smax): {Smax_shear} mm")
print(f"Stirrups Spacing in the Middle Span (Sprovide): {Sprovide_middle_span} mm")
print(f"Stirrups Spacing at the Support (Sprovide): {Sprovide_support} mm")



# Given values for the fourth part
Mcr_sls = 15.169  # kN·m 
Mqp_sls = 49.67  # kN·m
h_sls = 350  # mm
b_sls = 230  # mm
d_sls = 303  # mm
As_sls = 791.681  # mm2
Es_sls = 200  # kN/mm2
leff_sls = 200  # mm
xi2_sls = 152.709  # mm

# Combination factor
zeta_prime = 1 - 0.5 * (Mcr_sls / Mqp_sls)**2
zeta_prime = max(0.827, zeta_prime)  # Ensure it's not less than 0.827

# Calculated deformations
kEC = zeta_prime * (5.557 * 10**-6) / 1  # Assuming 1 for k1
eEC = zeta_prime * (26.622 + (1 - zeta_prime))  # Assuming 1 for e1

# Verification
emax = leff_sls / 200  # Assuming 200 for leff
verification_ok = emax > eEC

# Crack width analysis
epsilon_s = 0.001
epsilon_c = 2.479 * 10**-4

hc_eff = min(2.5 * (h_sls - d_sls) / (h_sls - xi2_sls)**3 - h_sls / 2, 79.153)
A_ceff = hc_eff * b_sls * (1.821 * 10**4)
epsilon_sc = epsilon_s * A_ceff / (Es_sls * As_sls)
rho_rho_eff = As_sls / A_ceff

# Durability of loads
kt = 0.4
delta_epsilon = epsilon_s - kt * epsilon_sc - kt * epsilon_c

# Maximal distance between two neighboring cracks
c = 25
k1 = 0.8
k2 = 0.5
phi = 12
Sr_max = 3.4 * c / (0.425 * k1 * k2 * phi * rho_rho_eff)
max_distance_between_cracks = Sr_max * delta_epsilon

# Crack width
wk = Sr_max * delta_epsilon

# SLS analysis at support
print("\nSLS Analysis at Support:")
print(f"Shear Force (Mqp): {Mqp_sls} kN·m")
# ... (rest of the properties for SLS analysis at support)

# Display results
print("\nResults:")
print(f"Combination Factor (ζ'): {zeta_prime}")
print(f"Calculated Deformations (kEC): {kEC} mm")
print(f"Calculated Deformations (eEC): {eEC} mm")
print(f"Verification: {'Ok' if verification_ok else 'Not Ok'}")
print(f"Maximal Distance Between Two Neighboring Cracks: {max_distance_between_cracks} mm")
print(f"Crack Width (wk): {wk} mm")

