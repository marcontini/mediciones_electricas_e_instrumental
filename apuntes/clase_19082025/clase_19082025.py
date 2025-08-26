import estadistica as st
import numpy as np

v = [5.007, 4.994, 5.005, 4.990, 4.999]  # V
i = [19.663, 19.639, 19.640, 19.685, 19.678]  # mA

err_inst = 0.001

# TENSIÓN
# TIPO A
v_med = st.mean(v)
v_std = st.std(v)
v_u_i = st.u_i(v)

# TIPO B
v_semrng, v_neg_semrng, v_pos_semrng = st.semrng(v, err_inst=err_inst)
v_u_j = st.u_j(v, sem=v_semrng, k=3)

# CORRIENTE
# TIPO A
i_med = st.mean(i)
i_std = st.std(i)
i_u_i = st.u_i(i)

# TIPO B
i_semrng, i_neg_semrng, i_pos_semrng = st.semrng(i, err_inst=err_inst)
i_u_j = st.u_j(i, sem=i_semrng, k=3)

print(f"err_inst:{f'{err_inst*100:0.4f}':>10} %")

print(f"\nEVALUACIÓN TIPO A:")
st.fprint(title="v_u_i", value=v_u_i, unit="V")
st.fprint(title="i_u_i", value=i_u_i, unit="mA")

print(f"\nEVALUACIÓN TIPO B:")
st.fprint(title="v_u_i", value=v_u_j, unit="V")
st.fprint(title="i_u_i", value=i_u_j, unit="mA")

# INCERTIDUMBRE COMBINADA DE LA RESISTENCIA
r = np.corrcoef(v, i)
auto = r[0, 0]
r = r[0, 1]
print(f"r:      {f'{r:0.4f}':>10}")
print(f"auto:   {f'{auto}':>10}")
dr_dv = 1 / i_med
dr_di = -v_med / (i_med**2)

u_r = np.sqrt(
    (v_u_i * dr_di) ** 2
    + (i_u_i * dr_dv) ** 2
    + (i_u_j * dr_di) ** 2
    + (v_u_j * dr_dv) ** 2
    + (2 * dr_dv * dr_di * r * v_u_i * i_u_i)
)

print(f"\nINCERTIDUMBRE COMBINADA:")
print(f"u_r:      {f'{1000*u_r:0.4f}':>10} Ω")

R = 1000 * (v_med / i_med)
print(f"R:        {f'{R:0.4f}':>10} Ω")

# Como estoy trabajando con 4 distribuciones y los ui de las variables
# son menores a los uj considero k de expanción normal

# Con un 68% de confianza podemos decir que R = (254.2 +- 2.1) Ω
# Si queremos un 95.44% de confianza nos queda un R = (254.2 +- 4.2) Ω
