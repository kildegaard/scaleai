import numpy as np
import random
from PyQt5.QtCore import QPointF


def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    curve = []
    for t in np.linspace(0, 1, num_points):
        point = QPointF(0, 0)
        for i, cp in enumerate(control_points):
            bernstein_poly = (
                (
                    np.math.factorial(n)
                    / (np.math.factorial(i) * np.math.factorial(n - i))
                )
                * (t**i)
                * ((1 - t) ** (n - i))
            )
            point.setX(point.x() + cp.x() * bernstein_poly)
            point.setY(point.y() + cp.y() * bernstein_poly)
        curve.append(point)
    return curve


def simulated_annealing(
    points,
    initial_control_points,
    max_iterations=1000,
    initial_temp=100.0,
    cooling_rate=0.99,
):
    def objective(control_points):
        bezier_points = bezier_curve(control_points)
        return sum(
            np.linalg.norm(np.array([p.x(), p.y()]) - np.array([b.x(), b.y()]))
            for p, b in zip(points, bezier_points)
        )

    def neighbor(control_points):
        idx = random.randint(0, len(control_points) - 1)
        new_control_points = control_points[:]
        new_control_points[idx] = QPointF(
            control_points[idx].x() + random.uniform(-10, 10),
            control_points[idx].y() + random.uniform(-10, 10),
        )
        return new_control_points

    current_control_points = initial_control_points
    current_cost = objective(current_control_points)
    best_control_points = current_control_points
    best_cost = current_cost
    temp = initial_temp

    for i in range(max_iterations):
        new_control_points = neighbor(current_control_points)
        new_cost = objective(new_control_points)
        if new_cost < current_cost or random.uniform(0, 1) < np.exp(
            (current_cost - new_cost) / temp
        ):
            current_control_points = new_control_points
            current_cost = new_cost
            if new_cost < best_cost:
                best_control_points = new_control_points
                best_cost = new_cost
        temp *= cooling_rate

    return best_control_points


# Example points to fit
points = [QPointF(x, np.sin(x)) for x in np.linspace(0, 10, 100)]

# Initial control points (randomly chosen for testing)
initial_control_points = [
    QPointF(x, random.uniform(-1, 1)) for x in np.linspace(0, 10, 4)
]

# Run the simulated annealing algorithm
best_control_points = simulated_annealing(points, initial_control_points)

# Print the best control points
print("Best Control Points:")
for cp in best_control_points:
    print(f"({cp.x()}, {cp.y()})")
