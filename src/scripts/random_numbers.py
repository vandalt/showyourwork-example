import matplotlib.pyplot as plt
import numpy as np
import paths

rng = np.random.default_rng()
random_numbers = rng.standard_normal((100, 10))

fig = plt.figure(figsize=(7, 6))
plt.plot(random_numbers)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(paths.figures / "random_numbers.pdf", bbox_inches="tight", dpi=300)
