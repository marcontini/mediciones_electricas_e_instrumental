import numpy as np

arr_muestra = np.array(
    [
        11.331,
        12.134,
        10.678,
        11.352,
        11.341,
        12.337,
        10.023,
        11.343,
        12.344,
        11.008,
    ]
)

i_med = arr_muestra.mean()
i_std = arr_muestra.std(ddof=1)
u_i = i_std / np.sqrt(len(arr_muestra))

print(f"\nEVALUACIÓN TIPO A:")
print(f"Media:    {f'{i_med:0.4f}':>10} mA")
print(f"Des. Std: {f'{i_std:0.4f}':>10} mA")
print(f"u_i:      {f'{u_i:0.4f}':>10} mA")

# ESTUDIO TIPO B

ex_inst = 0.002

semirango = i_med * ex_inst
semirango_neg = i_med - semirango
semirango_pos = i_med + semirango

u_j = semirango / np.sqrt(3)

print(f"\nEVALUACIÓN TIPO B:")
print(f"ex_inst:  {f'{ex_inst*100:0.4f}':>10} %")
print(f"u_j:      {f'{u_j:0.4f}':>10} mA")

u_c = np.sqrt(u_i**2 + u_j**2)
print(f"\nINCERTIDUMBRE COMBINADA:")
print(f"u_c:      {f'{u_c:0.4f}':>10} mA")

v_eff = (u_c**4) / ((u_i**4) / (len(arr_muestra) - 1))
print(f"\nGL EFECTIVOS:")
print(f"v_eff:    {f'{v_eff:0.0f}':>10} gl")
