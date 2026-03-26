import numpy as np
import pandas as pd
import math
import matplotlib as plt
from scipy.stats import norm

print("\n=== STOCHASTIC DIGITAL TWIN ===")

try:
    n_days = int(
        input("Simulasyon kac gun sursun? (Varsayilan: 365): ") or 365)
    avg_demand = int(
        input("Gunluk ortalama talep beklentisi nedir? (Varsayilan: 15): ") or 15)
    lead_time = int(
        input("Kargo/Tedarik suresi kac gundur? (Varsayilan: 5): ") or 5)
    sl_input = float(
        input("Hedeflenen Servis Seviyesi % kactir? (Orn: 95): ") or 95)
    sl = sl_input / 100.0
except ValueError:
    print("\n[!] Hatali bir harf girdiniz. Varsayilan degerlerle devam ediliyor...")
    n_days = 365
    avg_demand = 15
    lead_time = 5
    sl = 0.95
print("Simulasyon motoru calisiyor...")

# generating poisson demand
demand_data = np.random.poisson(lam=avg_demand, size=n_days)
df = pd.DataFrame({'day': range(1, n_days + 1), 'demand': demand_data})
