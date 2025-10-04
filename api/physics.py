import math

def simulate_impact(mass, velocity, angle):
    # Simplified physics (not real-world accurate!)
    kinetic_energy = 0.5 * mass * velocity**2  # Joules

    # Estimate crater diameter (very rough empirical model)
    crater_diameter = (kinetic_energy ** 0.25) / 1000  # km

    # Estimate blast radius (shockwave range in km)
    blast_radius = (kinetic_energy ** 0.17)

    return {
        "kinetic_energy": kinetic_energy,
        "crater_diameter_km": crater_diameter,
        "blast_radius_km": blast_radius,
        "impact_angle": angle
    }
