import numpy as np
import matplotlib.pyplot as plt


def compute_B_loop(R_loop, x0, z_points, I, mu_r, segments=1000):
    mu0 = 4 * np.pi * 1e-7
    thetas = np.linspace(0, 2*np.pi, segments, endpoint=False)
    dl = R_loop * (2*np.pi/segments)
    x_loop = R_loop * np.cos(thetas)
    y_loop = R_loop * np.sin(thetas)
    dl_vectors = np.vstack((-np.sin(thetas), np.cos(thetas), np.zeros(segments))).T * dl

    Bz = np.zeros_like(z_points)
    for i, z in enumerate(z_points):
        obs = np.array([x0, 0.0, z])
        r_vecs = obs - np.vstack((x_loop, y_loop, np.zeros(segments))).T
        r_norms = np.linalg.norm(r_vecs, axis=1)
        cross = np.cross(dl_vectors, r_vecs)
        dB = mu0 * mu_r * I * cross / (4*np.pi * r_norms**3)[:, None]
        Bz[i] = np.sum(dB[:, 2])
    return Bz


def get_input(prompt, default, cast=float):
    s = input(f"{prompt} [{default}]: ").strip()
    return cast(s) if s else default


I = get_input("Ток I (A)", 1.0)
mu_r_list_str = input("Список μr через запятую [1,50,200]: ").strip()
if mu_r_list_str:
    mu_r_values = [float(x) for x in mu_r_list_str.split(',')]
else:
    mu_r_values = [1, 50, 200]

R_toroid = get_input("Радиус тора R_toroid (м)", 0.1)
R_cylinder = get_input("Радиус цилиндрической петли R_cylinder (м)", 0.05)
x0 = get_input("Смещение оси наблюдения x0 (м)", R_toroid/2)
z_min = get_input("Минимум по z (м)", -0.2)
z_max = get_input("Максимум по z (м)", 0.2)
n_points = int(get_input("Число точек по z", 200, cast=int))

z = np.linspace(z_min, z_max, n_points)

plt.figure(figsize=(10, 6))
for mu_r in mu_r_values:
    B_toroid = compute_B_loop(R_toroid, x0, z, I, mu_r)
    B_cylinder = compute_B_loop(R_cylinder, x0, z, I, mu_r)
    plt.plot(z, B_toroid,      label=f'Тороид, μr={mu_r}')
    plt.plot(z, B_cylinder, '--', label=f'Цилиндр, μr={mu_r}')

plt.xlabel('z (м)')
plt.ylabel('B_z (Тл)')
plt.title('Зависимость B_z по оси, смещённой на R/2')
plt.legend()
plt.grid(True)

output_filename = "Bz_plot.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"График сохранён в {output_filename}")

plt.show()
