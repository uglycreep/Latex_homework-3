from pathlib import Path
import matplotlib.pyplot as plt
from search import linear_search, binary_search


# папка с рисунками находится рядом с папкой кода
folder = Path(__file__).resolve().parent.parent / "images"
folder.mkdir(exist_ok=True)
sizes = [8, 16, 32, 64, 128, 256, 512, 1024]
linear = []
binary = []
for n in sizes:
    data = list(range(n))
    linear.append(linear_search(data, n)[1])
    binary.append(binary_search(data, n)[1])

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
ax.plot(sizes, linear, "o-", label="Линейный поиск")
ax.plot(sizes, binary, "s--", label="Бинарный поиск")
ax.set_xscale("log", base=2)
ax.set_yscale("log", base=2)
ax.set_xticks(sizes, labels=sizes)
ax.set_xlabel("Количество элементов n")
ax.set_ylabel("Количество шагов")
ax.grid(alpha=0.3)
ax.legend()
fig.savefig(folder / "steps.png", dpi=180)
plt.close(fig)

ratio = [a / b for a, b in zip(linear, binary)]
fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
ax.bar([str(n) for n in sizes], ratio, color="#365f91")
ax.set_xlabel("Количество элементов n")
ax.set_ylabel("Отношение числа шагов")
ax.set_ylim(0, 110)
for i, value in enumerate(ratio):
    ax.text(i, value + 2, f"{value:.1f}", ha="center")
ax.grid(axis="y", alpha=0.3)
fig.savefig(folder / "ratio.png", dpi=180)
plt.close(fig)
