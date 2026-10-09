import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

if len(sys.argv) < 2:
	print("usage:")
	print("python visualize.py spectrum.csv")
	exit()

csv_path = Path(sys.argv[1])

df = pd.read_csv(csv_path)

freq = df["freq"]
mag = df["mag"]

plt.figure(figsize=(12,6))
plt.plot(freq, mag)

plt.title(csv_path.stem)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.show()


