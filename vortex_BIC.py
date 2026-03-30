import meep as mp
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation parameters (all in μm)
# -----------------------------
P = 0.380        # period
slab_t = 0.120   # slab thickness
D = 0.280        # hole diameter
n_slab = 2.02    # slab index

Nx_periods = 50
Ny_periods = 50

# -----------------------------
# Simulation cell (with 1 μm buffer)
# -----------------------------
sx = Nx_periods*P + 2
sy = Ny_periods*P + 2
sz = slab_t + 2

cell = mp.Vector3(sx, sy, sz)

# -----------------------------
# Resolution (memory safe)
# -----------------------------
resolution = 50  # pixels/μm, safe for 16GB RAM

# -----------------------------
# Geometry: slab + holes
# -----------------------------
geometry = [mp.Block(size=mp.Vector3(mp.inf, mp.inf, slab_t),
                     center=mp.Vector3(0,0,0),
                     material=mp.Medium(index=n_slab))]

x_start = -(Nx_periods-1)*P/2
y_start = -(Ny_periods-1)*P/2

for ix in range(Nx_periods):
    for iy in range(Ny_periods):
        x0 = x_start + ix*P
        y0 = y_start + iy*P
        geometry.append(mp.Cylinder(radius=D/2, height=slab_t+1,
                                    center=mp.Vector3(x0,y0,0),
                                    material=mp.Medium(index=1.0)))

# -----------------------------
# Gaussian beam source
# -----------------------------
beam_w = 7.5/2  # waist radius in μm
freq = 1/0.532  # μm^-1
df = 1/0.0532   # frequency width

sources = [mp.Source(mp.GaussianSource(frequency=freq, fwidth=df),
                     component=mp.Ez,
                     center=mp.Vector3(0,0,-sz/2+0.5),
                     size=mp.Vector3(sx, sy, 0))]

# -----------------------------
# Simulation setup
# -----------------------------
sim = mp.Simulation(cell_size=cell,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution,
                    boundary_layers=[mp.PML(1.0)])

# -----------------------------
# Run simulation shortly to get field
# -----------------------------
sim.run(until=200)

# -----------------------------
# XY plane at slab top
# -----------------------------
nf_z = slab_t/2
ez_xy = sim.get_array(center=mp.Vector3(0,0,nf_z),
                      size=mp.Vector3(sx, sy, 0),
                      component=mp.Ez)

plt.figure(figsize=(6,5))
plt.imshow(np.abs(ez_xy.T)**2,
           extent=[-sx/2, sx/2, -sy/2, sy/2],
           origin='lower')
plt.xlabel("x (μm)")
plt.ylabel("y (μm)")
plt.title("XY intensity at z = {:.2f} μm".format(nf_z))
plt.colorbar(label="|Ez|^2 (a.u.)")
plt.show()

# -----------------------------
# XZ side-view (center y)
# -----------------------------
ez_xz = sim.get_array(center=mp.Vector3(0,0,0),
                      size=mp.Vector3(sx, 0, sz),
                      component=mp.Ez)

plt.figure(figsize=(6,5))
plt.imshow(np.abs(ez_xz.T)**2,
           extent=[-sx/2, sx/2, -sz/2, sz/2],
           origin='lower')
plt.xlabel("x (μm)")
plt.ylabel("z (μm)")
plt.title("XZ side-view intensity at y = 0")
plt.colorbar(label="|Ez|^2 (a.u.)")
plt.show()