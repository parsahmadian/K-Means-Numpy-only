# """
# The dataset was intentionally designed with correlated features, noise,
# and overlapping clusters to better reflect real-world housing markets,
# where perfect separability is unrealistic.
# """

# import numpy as np
# import pandas as pd

# np.random.seed(42)
# n = 1200
# file_name = f"housing_market_segmentation_dataset_{n}.csv"

# # --- Distance to center (km)
# distance = np.random.exponential(scale=5, size=n).clip(0.2, 25)

# # --- Area depends on distance (center -> smaller houses)
# area = (
#     np.random.normal(140, 35, n)
#     - distance * np.random.uniform(2.5, 4.0, n)
# ).clip(45, 300)

# # --- Rooms correlated with area (but noisy)
# rooms = (area / 35 + np.random.normal(0, 0.8, n)).round().clip(1, 6)

# # --- Building age correlated with distance
# age = (
#     np.random.normal(15 + distance, 6, n)
# ).clip(0, 40).astype(int)

# # --- Floor correlated with area (bigger houses -> higher floors)
# floor = (
#     np.random.normal(area / 30, 3, n)
# ).clip(0, 20).astype(int)

# # --- Elevator (probabilistic, not deterministic)
# elevator_prob = np.clip((floor - 2) / 10, 0, 1)
# elevator = np.random.binomial(1, elevator_prob)

# # --- Parking (depends on area and distance)
# parking_prob = np.clip(0.3 + area / 300 - distance / 20, 0.1, 0.9)
# parking = np.random.binomial(1, parking_prob)

# df = pd.DataFrame({
#     "Area": area.astype(int),
#     "Rooms": rooms.astype(int),
#     "BuildingAge": age,
#     "DistanceToCenter": distance.round(2),
#     "Floor": floor,
#     "Elevator": elevator,
#     "Parking": parking
# })

# df.to_csv(file_name, index=False)
# print(f"{file_name} saved ✅")