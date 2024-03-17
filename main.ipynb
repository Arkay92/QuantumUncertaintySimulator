import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, pi
from scipy.integrate import simps
from scipy.fft import fft, fftfreq
from ipywidgets import interact, FloatSlider

def simulate_uncertainty(sigma_x):
    # Define parameters
    x = np.linspace(-1e-9, 1e-9, 1000)  # Position array

    # Position-space wave function: Gaussian wave packet
    psi_x = np.exp(-x**2 / (4 * sigma_x**2)) / (np.sqrt(2 * pi * sigma_x**2))
    psi_x /= np.sqrt(simps(abs(psi_x)**2, x))  # Normalize the wave function in position space

    # Fourier transform to momentum-space wave function
    psi_p = fft(psi_x)
    p = fftfreq(x.size, d=x[1] - x[0]) * 2 * pi * hbar
    psi_p = np.fft.fftshift(psi_p)  # Shift zero frequency to center
    p = np.fft.fftshift(p)  # Shift zero momentum to center

    # Correct normalization of the momentum-space wave function
    dx = x[1] - x[0]  # Grid spacing in position space
    psi_p *= dx / (2 * pi * hbar) ** 0.5

    # Calculate uncertainties
    delta_x = np.sqrt(simps(x**2 * abs(psi_x)**2, x) - (simps(x * abs(psi_x)**2, x))**2)
    delta_p = np.sqrt(simps(p**2 * abs(psi_p)**2, p) - (simps(p * abs(psi_p)**2, p))**2)

    # Validate the Uncertainty Principle
    uncertainty_product = delta_x * delta_p
    tolerance = 1e-36  # Tolerance factor to account for numerical inaccuracies
    print(f"Uncertainty in position (Δx): {delta_x:.2e} m")
    print(f"Uncertainty in momentum (Δp): {delta_p:.2e} kg m/s")
    print(f"Product of uncertainties (ΔxΔp): {uncertainty_product:.2e} Js")
    print(f"Heisenberg limit (hbar/2): {hbar/2:.2e} Js")
    assert uncertainty_product + tolerance >= hbar/2, "Uncertainty Principle violated!"

    # Plotting
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot position-space wave function and probability density
    axs[0].plot(x, abs(psi_x)**2, label='Probability Density in Position Space')
    axs[0].set_title('Position Space')
    axs[0].set_xlabel('Position (m)')
    axs[0].set_ylabel('Probability Density')
    axs[0].legend()

    # Plot momentum-space wave function and probability density
    axs[1].plot(p, abs(psi_p)**2, label='Probability Density in Momentum Space', color='orange')
    axs[1].set_title('Momentum Space')
    axs[1].set_xlabel('Momentum (kg m/s)')
    axs[1].set_ylabel('Probability Density')
    axs[1].legend()

    plt.tight_layout()
    plt.show()

# Interactive exploration of the Uncertainty Principle with varying sigma_x
interact(simulate_uncertainty, sigma_x=FloatSlider(min=1e-11, max=1e-9, step=1e-12, value=1e-10, description='Sigma_x (m):', readout_format='.1e'))
