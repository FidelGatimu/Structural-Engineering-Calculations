# Reinforced Concrete Beam Design According to Eurocode

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

# Example usage
print(f"Thickness (t): {input_data.t.value}")
print(f"Width (b): {input_data.b.value}")
print(f"Height or Depth (h): {input_data.h.value}")
print(f"Length (l): {input_data.l.value}")
print(f"Concrete Strength (fck): {input_data.fck.value}")
print(f"Partial Safety Factor for Concrete (γc): {input_data.γc.value}")
print(f"Steel Yield Strength (fyk): {input_data.fyk.value}")
print(f"Partial Safety Factor for Steel (γs): {input_data.γs.value}")
print(f"Distance a1: {input_data.a1.value}")
print(f"Distance a2: {input_data.a2.value}")
print(f"Factor ψ2: {input_data.ψ2.value}")


# Input parameters
span_length = 5.0  # Length of the beam in meters
load = 30.0  # Uniformly distributed load in kN/m
fck = 25.0  # Characteristic compressive strength of concrete in MPa
fyk = 500.0  # Characteristic yield strength of steel in MPa
gamma_c = 1.5  # Partial safety factor for concrete
gamma_s = 1.15  # Partial safety factor for steel

# Constants
width = 0.2  # Width of the beam in meters
depth = 0.4  # Overall depth of the beam in meters

# Calculate design moments
moment_due_to_dead_load = 0.5 * load * span_length ** 2
moment_due_to_live_load = (load * span_length ** 2) / 8

total_design_moment = moment_due_to_dead_load + moment_due_to_live_load

# Determine effective depth
d_eff = depth - 0.04  # Assuming cover of 40 mm

# Calculate lever arm
lever_arm = 0.95 * d_eff

# Calculate design shear force
shear_force = (load * span_length) / 2

# Calculate design bending stress
bending_stress = total_design_moment / (width * d_eff ** 2)

# Calculate required area of tension reinforcement
area_tension_reinforcement = (total_design_moment * 10 **6) / (0.87 * fyk * lever_arm)

# Check for minimum and maximum reinforcement requirements
area_tension_min = 0.26 / 100 * width * d_eff
area_tension_max = 4.0 / 100 * width * d_eff

# Adjust the required area if it falls below the minimum or above the maximum
if area_tension_reinforcement < area_tension_min:
    area_tension_reinforcement = area_tension_min
elif area_tension_reinforcement > area_tension_max:
    area_tension_reinforcement = area_tension_max

# Print results
print("Design Moments:")
print(f"  Moment due to Dead Load: {moment_due_to_dead_load} kNm")
print(f"  Moment due to Live Load: {moment_due_to_live_load} kNm")
print(f"  Total Design Moment: {total_design_moment} kNm")

print("\nDesign Shear Force:")
print(f"  Shear Force: {shear_force} kN")

print("\nDesign Bending Stress:")
print(f"  Bending Stress: {bending_stress} MPa")

print("\nReinforcement Requirements:")
print(f"  Required Area of Tension Reinforcement: {area_tension_reinforcement} cm^2")
print(f"  Minimum Area of Tension Reinforcement: {area_tension_min} cm^2")
print(f"  Maximum Area of Tension Reinforcement: {area_tension_max} cm^2")
