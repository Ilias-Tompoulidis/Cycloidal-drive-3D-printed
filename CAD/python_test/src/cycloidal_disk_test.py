import cadquery as cq
from math import atan, sin, cos, pi

g_ratio = 8
# =========================
# PARAMETERS (mm)
# =========================
N = g_ratio+1          # number of rollers
R = 25.0        # roller pitch circle radius
Rr = 5.0       # roller radius
E = 1.5         # eccentricity
thickness = 6.0  # disc thickness
steps = 720     # curve resolution (higher = smoother)
scale = 0.98

print(f"Ratio = {N-1}")

# =========================
# CYCLOID POINT GENERATION
# =========================
points = []

for i in range(steps + 1):
    t = 2 * pi * i / steps

    phi = atan(
        sin((1 - N) * t) /
        ((R / (E * N)) - cos((1 - N) * t))
    )

    x = (R*cos(t))-(Rr*cos(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
    y = (-R*sin(t))+(Rr*sin(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))
    x_scaled = x * scale
    y_scaled = y * scale

    points.append((x_scaled, y_scaled))

# =========================
# BUILD CAD MODEL
# =========================
disc = (
    cq.Workplane("XY")
    .spline(points)
    .close()
    .extrude(thickness)
)

# =========================
# EXPORT
# =========================
cq.exporters.export(disc, "cycloidal_disc_scaled.step")
