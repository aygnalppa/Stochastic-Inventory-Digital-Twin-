import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

print("\n=== STOCHASTIC DIGITAL TWIN ===")

try:
    n_days = int(
        input("Simulasyon kac gun sursun? (Varsayilan: 365): ") or 365)
except ValueError:
    print("\n[!] Hatali bir harf girdiniz. Varsayilan degerlerle devam ediliyor...")
    n_days = 365
try:
    avg_demand = int(
        input("Gunluk ortalama talep beklentisi nedir? (Varsayilan: 15): ") or 15)
except ValueError:
    print("\n[!] Hatali bir harf girdiniz. Varsayilan degerlerle devam ediliyor...")
    avg_demand = 15
try:
    lead_time = int(
        input("Kargo/Tedarik suresi kac gundur? (Varsayilan: 5): ") or 5)
except ValueError:
    print("\n[!] Hatali bir harf girdiniz. Varsayilan degerlerle devam ediliyor...")
    lead_time = 5
try:
    sl_input = float(
        input("Hedeflenen Servis Seviyesi % kactir? (Orn: 95): ") or 95)
    sl = sl_input / 100.0
except ValueError:
    print("\n[!] Hatali bir harf girdiniz. Varsayilan degerlerle devam ediliyor...")
    sl = 0.9

print("Simulasyon motoru calisiyor...")


# print(lead_time, sl_input, avg_demand, n_days)

# generating poisson demand
demand_data = np.random.poisson(lam=avg_demand, size=n_days)
df = pd.DataFrame({'day': range(1, n_days + 1), 'demand': demand_data})

z = norm.ppf(sl)
d_mean = df['demand'].mean()
d_std = df['demand'].std()

# calculate ss and rop
ss_raw = z * d_std * math.sqrt(lead_time)
rop_raw = (d_mean * lead_time)+ss_raw

ss = math.ceil(ss_raw)
rop = math.ceil(rop_raw)
print(f"Stats -> Mean: {d_mean:.2f}, Std: {d_std:.2f}")
print(f"Results -> ROP: {rop}, SS: {ss}")

# --- simulation loop ---
inv_levels = []
curr_inv = rop + 50
is_ordered = False
days_left = 0
order_qty = 150

for d in df['demand']:
    if is_ordered and days_left == 0:
        curr_inv += order_qty
        is_ordered = False

    curr_inv -= d
    inv_levels.append(curr_inv)

    # print(f"day check: inv={curr_inv}, demand={d}")

    if curr_inv <= rop and not is_ordered:
        is_ordered = True
        days_left = lead_time

    if is_ordered:
        days_left -= 1

df['inventory'] = inv_levels

# --- plotting ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

ax1.plot(df['day'][:100], df['inventory'][:100],
         color='blue', label='Inventory')
ax1.axhline(y=rop, color='red', linestyle='-', label=f'ROP ({rop})')
ax1.axhline(y=ss, color='orange', linestyle='--', label=f'SS ({ss})')
ax1.set_title('Inventory Simulation')
ax1.legend()

ax2.plot(df['day'][:100], df['demand'][:100], color='purple',
         marker='.', alpha=0.6, label='Demand')
ax2.axhline(y=d_mean, color='green', linestyle=':', label='Avg Demand')
ax2.set_title('Daily Demand')
ax2.legend()

plt.tight_layout()
plt.show()
