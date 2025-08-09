import pybamm
model = pybamm.lithium_ion.DFN()

model.print_parameter_info()

sim = pybamm.Simulation(model)
sim.solve([0, 3600])
output_variables = [
    "Negative secondary particle surface concentration [mol.m-3]",
    "Electrolyte concentration [mol.m-3]",
    "Positive particle surface concentration [mol.m-3]",
    "Secondary: negative electrode potential [V]",
    "Electrolyte potential [V]",
    "Positive electrode potential [V]",
    "Voltage [V]",
]


sim.plot()