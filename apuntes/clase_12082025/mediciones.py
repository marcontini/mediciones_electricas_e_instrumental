import numpy as np

arr_muestra = np.array(
    [
        11.331,
        11.352,
        11.352,
        11.341,
        11.353,
        11.337,
        11.342,
        11.343,
        11.344,
        11.338,
    ]
)

i_med = arr_muestra.mean()
i_std = arr_muestra.std(ddof=1)
u_i = i_std / np.sqrt(len(arr_muestra))

print(f"\nRESULTADOS:")
print(f"Media:    {f'{i_med:0.4f}':>10} mA")
print(f"Des. Std: {f'{i_std:0.4f}':>10} mA")
print(f"u_i:      {f'{u_i:0.4f}':>10} mA")
