import cadquery as cq
import math

g_ratio = 10
# =========================
# PARAMETERS (mm)
# =========================
N = g_ratio+1          # number of rollers
R = 35.0        # roller pitch circle radius
Rr = 5.0        # roller radius
E = 1.5         # eccentricity
thickness = 7.0  # disc thickness
steps = 720     # curve resolution (higher = smoother)

print(f"Ratio = {N-1}")

# =========================
# CYCLOID POINT GENERATION
# =========================
points = []

for i in range(steps + 1):
    t = 2 * math.pi * i / steps

    phi = math.atan(
        math.sin((1 - N) * t) /
        ((R / (E * N)) - math.cos((1 - N) * t))
    )

    x = (R * math.cos(t)) \
        - (Rr * math.cos(t + phi)) \
        - (E * math.cos(N * t))

    y = (-R * math.sin(t)) \
        + (Rr * math.sin(t + phi)) \
        + (E * math.sin(N * t))

    points.append((x, y))

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
cq.exporters.export(disc, "cycloidal_disc.step")
