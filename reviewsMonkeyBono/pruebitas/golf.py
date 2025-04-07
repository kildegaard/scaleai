import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # gravity (m/s^2)
rho = 1.225  # air density (kg/m^3)
Cd = 0.47  # drag coefficient
Cl = 0.15  # lift coefficient
Cm = 0.15  # Magnus effect coefficient
A = 0.001432  # cross-sectional area of a golf ball (m^2)
m = 0.0459  # mass of a golf ball (kg)


def magnus_effect(vx, vy, vz, omega):
    return (
        Cm
        * rho
        * A
        * np.array(
            [
                -vy * omega[2] + vz * omega[1],
                vx * omega[2] - vz * omega[0],
                -vx * omega[1] + vy * omega[0],
            ]
        )
    )


def equations_of_motion(t, y, v0, theta, omega, wind_speed, wind_direction):
    vx, vy, vz, x, y_pos, z = y
    v = np.sqrt(vx**2 + vy**2 + vz**2)

    Fd = -0.5 * Cd * rho * A * v * np.array([vx, vy, vz])
    Fl = 0.5 * Cl * rho * A * v**2 * np.array([-np.sin(theta), 0, np.cos(theta)])
    Fm = magnus_effect(vx, vy, vz, omega)

    wind_angle = np.deg2rad(wind_direction)
    Fw = (
        0.5
        * rho
        * A
        * wind_speed**2
        * np.array([np.cos(wind_angle), 0, np.sin(wind_angle)])
    )

    ax = (Fd[0] + Fl[0] + Fm[0] + Fw[0]) / m
    ay = (Fd[1] + Fl[1] + Fm[1] + Fw[1] - m * g) / m
    az = (Fd[2] + Fl[2] + Fm[2] + Fw[2]) / m

    return [ax, ay, az, vx, vy, vz]


def calculate_trajectory(v0, theta, spin_rate, wind_speed, wind_direction):
    theta = np.deg2rad(theta)
    omega = np.array([0, 0, spin_rate * 2 * np.pi / 60])  # convert RPM to rad/s

    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    vz0 = 0

    initial_conditions = [vx0, vy0, vz0, 0, 0, 0]
    t_max = 100  # seconds
    t_eval = np.linspace(0, t_max, 500)

    sol = solve_ivp(
        equations_of_motion,
        [0, t_max],
        initial_conditions,
        args=(v0, theta, omega, wind_speed, wind_direction),
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-8,
    )

    vx, vy, vz, x, y, z = sol.y
    t_flight = sol.t[-1]

    return x, y, z, t_flight


def plot_trajectory(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    plt.show()


def animate_trajectory(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    (line,) = ax.plot([], [], [])

    def init():
        ax.set_xlim(min(x), max(x))
        ax.set_ylim(min(y), max(y))
        ax.set_zlim(min(z), max(z))
        return (line,)

    def animate(i):
        line.set_data(x[:i], y[:i])
        line.set_3d_properties(z[:i])
        return (line,)

    ani = animation.FuncAnimation(
        fig, animate, frames=len(x), init_func=init, interval=50
    )
    plt.show()


def main():
    v0 = float(input("Enter initial velocity (m/s): "))
    theta = float(input("Enter launch angle (degrees): "))
    spin_rate = float(input("Enter spin rate (RPM): "))
    wind_speed = float(input("Enter wind speed (m/s): "))
    wind_direction = float(input("Enter wind direction (degrees): "))

    x, y, z, t_flight = calculate_trajectory(
        v0, theta, spin_rate, wind_speed, wind_direction
    )

    print("Total distance: {:.2f} m".format(x[-1]))
    print("Maximum height: {:.2f} m".format(np.max(y)))
    print("Flight time: {:.2f} s".format(t_flight))

    plot_trajectory(x, y, z)
    animate_trajectory(x, y, z)


if __name__ == "__main__":
    main()
