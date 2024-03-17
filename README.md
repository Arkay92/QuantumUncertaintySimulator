# Quantum Uncertainty Simulator

This Python-based tool provides an interactive simulation and visualization of the Heisenberg Uncertainty Principle, utilizing Gaussian wave packets. It demonstrates the fundamental quantum mechanics concept that the more precisely the position of some particle is determined, the less precisely its momentum can be predicted, and vice versa.

## Installation

To use this tool, ensure you have Python installed on your system. Clone this repository and install the required dependencies:

```bash
git clone https://github.com/Arkay92/QuantumUncertaintySimulator.git
cd QuantumUncertaintySimulator
pip install -r requirements.txt
```

## Usage
Run the python script provided in the repository to start the interactive simulation:

```
python main.py
```

or

```
jupyter notebook Quantum_Uncertainty_Simulator.ipynb
```

Adjust the sigma_x parameter using the slider to see how it affects the uncertainties in position and momentum, and observe the corresponding changes in the wave packet visualizations in position and momentum spaces.

## Features
- Interactive slider to adjust the width of the Gaussian wave packet.
- Visualization of probability densities in both position and momentum spaces.
- Calculation and display of uncertainties in position and momentum, and their product, to validate the Heisenberg Uncertainty Principle.

## Requirements
This tool relies on the following Python libraries:

- numpy for numerical operations.
- matplotlib for plotting and visualization.
- scipy for scientific computations and integration.
- ipywidgets for interactive Jupyter Notebook widgets.

## Contributing
Contributions to improve the Quantum Uncertainty Simulator are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
