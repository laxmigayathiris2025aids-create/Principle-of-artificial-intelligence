
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Step 1: Define Variables
distance = np.arange(0, 11, 1)  # Distance: 0 to 10 km
speed = np.arange(0, 31, 1)     # Speed: 0 to 30 km/h

# Step 2: Membership Functions

# Distance
small = fuzz.trimf(distance, [0, 0, 5])
medium = fuzz.trimf(distance, [0, 5, 10])
large = fuzz.trimf(distance, [5, 10, 10])

# Speed
low = fuzz.trimf(speed, [0, 0, 15])
steady = fuzz.trimf(speed, [5, 15, 25])
high = fuzz.trimf(speed, [15, 30, 30])

# Step 3: Plot Membership Functions

plt.figure(figsize=(10, 4))
plt.plot(distance, small, label="Small")
plt.plot(distance, medium, label="Medium")
plt.plot(distance, large, label="Large")
plt.title("Distance Membership Functions")
plt.xlabel("Distance (km)")
plt.ylabel("Membership")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(speed, low, label="Low")
plt.plot(speed, steady, label="Steady")
plt.plot(speed, high, label="High")
plt.title("Speed Membership Functions")
plt.xlabel("Speed (km/h)")
plt.ylabel("Membership")
plt.legend()
plt.grid()
plt.show()

# Step 4: Input
distance_input = float(input("Enter distance (0 to 10 km): "))

# Step 5: Fuzzification
small_level = fuzz.interp_membership(
    distance, small, distance_input
)
medium_level = fuzz.interp_membership(
    distance, medium, distance_input
)
large_level = fuzz.interp_membership(
    distance, large, distance_input
)

print("\nDistance Membership Values")
print("Small:", round(small_level, 2))
print("Medium:", round(medium_level, 2))
print("Large:", round(large_level, 2))

# Step 6: Apply Rules

# Rule 1: Small distance -> Low speed
speed_low = np.fmin(small_level, low)

# Rule 2: Medium distance -> Steady speed
speed_steady = np.fmin(medium_level, steady)

# Rule 3: Large distance -> High speed
speed_high = np.fmin(large_level, high)

# Combine all rules
combined = np.fmax(
    speed_low,
    np.fmax(speed_steady, speed_high)
)

# Step 7: Defuzzification
if np.sum(combined) == 0:
    print("Cannot calculate recommended speed.")
else:
    recommended_speed = fuzz.defuzz(
        speed, combined, "centroid"
    )

    # Step 8: Plot Result
    plt.figure(figsize=(10, 4))
    plt.plot(speed, low, label="Low")
    plt.plot(speed, steady, label="Steady")
    plt.plot(speed, high, label="High")
    plt.fill_between(
        speed, combined, alpha=0.5,
        label="Recommended Speed"
    )
    plt.axvline(
        recommended_speed, linestyle="--",
        label="Recommended Speed"
    )
    plt.title("Output Result")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Membership")
    plt.legend()
    plt.grid()
    plt.show()

    print(
        "\nRecommended Speed =",
        round(recommended_speed, 2),
        "km/h"
    )
