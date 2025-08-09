import os
import timeit
import matplotlib.pyplot as plt
from matplotlib import style
import pybamm

style.use("ggplot")

start = timeit.default_timer()
model = pybamm.lithium_ion.DFN(
    {"particle phases": ("2", "1"),
     "open-circuit potential": (("single", "current sigmoid"), "single"),
    }
)

param = pybamm.ParameterValues("Chen2020_composite")

param.update({"Upper voltage cut-off [V]": 4.5})
param.update({"Lower voltage cut-off [V]": 2.5})

param.update(
    {
        "Primary: Maximum concentration in negative electrode [mol.m-3]": 28700,
        "Primary: Initial concentration in negative electrode [mol.m-3]": 23000,
        "Primary: Negative particle diffusivity [m2.s-1]": 5.5e-14,
        "Secondary: Negative particle diffusivity [m2.s-1]": 1.67e-14,
        "Secondary: Initial concentration in negative electrode [mol.m-3]": 277000,
        "Secondary: Maximum concentration in negative electrode [mol.m-3]": 278000,
    }
)

C_rate = 0.5
capacity = param["Nominal cell capacity [A.h]"]
I_load = C_rate * capacity

t_eval = [0, 10000]

param["Current function [A]"] = I_load

v_si = [0.001, 0.04, 0.1]
total_am_volume_fraction = 0.75
solution = []  

for v in v_si:
    param.update(
        {
            "Primary: Negative electrode active material volume fraction": (1 - v)
            * total_am_volume_fraction,  # primary
            "Secondary: Negative electrode active material volume fraction": v
            * total_am_volume_fraction,
        }
    )
    print(v)
    sim = pybamm.Simulation(
        model,
        parameter_values=param,
    )
    solution.append(sim.solve(t_eval=t_eval))
stop = timeit.default_timer()
print("running time: " + str(stop - start) + "s")



ltype = ["k-", "r--", "b-.", "g:", "m-", "c--", "y-."]
for i in range(0, len(v_si)):
    t_i = solution[i]["Time [s]"].entries / 3600
    V_i = solution[i]["Voltage [V]"].entries
    plt.plot(t_i, V_i, ltype[i], label="$V_\mathrm{si}=$" + str(v_si[i]))
plt.xlabel("Time [h]")
plt.ylabel("Voltage [V]")
plt.legend()
plt.savefig("composite_ocvs.png")

plt.figure()
for i in range (0, len(v_si)):
    t_i = solution[i]["Time [s]"].entries / 3600
    OCP_i = solution[i]["X-averaged negative electrode primary open-circuit potential [V]"].entries
    plt.plot(t_i, OCP_i, ltype[i], label="$V_\mathrm{si}=$" + str(v_si[i]))
plt.xlabel("Time [h]")
plt.ylabel("OCP [V]")
plt.legend()
plt.title("Graphite")
plt.savefig("graphite_ocp.png")

plt.figure()
for i in range (0, len(v_si)):
    t_i = solution[i]["Time [s]"].entries / 3600
    OCP_i = solution[i]["X-averaged negative electrode secondary open-circuit potential [V]"].entries
    plt.plot(t_i, OCP_i, ltype[i], label="$V_\mathrm{si}=$" + str(v_si[i]))
plt.xlabel("Time [h]")
plt.ylabel("OCP [V]")
plt.legend()
plt.title("Silicon")
plt.savefig("silicon_ocp.png")

plt.figure()
for i in range (0, len(v_si)):
    t_i = solution[i]["Time [s]"].entries / 3600
    OCP_i = solution[i]["X-averaged positive electrode open-circuit potential [V]"].entries
    plt.plot(t_i, OCP_i, ltype[i], label="$V_\mathrm{si}=$" + str(v_si[i]))
plt.xlabel("Time [h]")
plt.ylabel("OCP [V]")
plt.legend()
plt.title("NMC811")
plt.savefig("NMC_ocp.png")

#Cycling

experiment = pybamm.Experiment(
    [
        (
            "Discharge at C/2 until 3.0 V",
            "Rest for 1 hour",
            "Charge at C/2 until 4.2 V",
            "Rest for 1 hour",
        ),
    ]
)


solution = []
for v in v_si:
    param.update(
        {
            "Primary: Negative electrode active material volume fraction": (1 - v)
            * total_am_volume_fraction,  # primary
            "Secondary: Negative electrode active material volume fraction": v
            * total_am_volume_fraction,
        }
    )
    print(v)
    sim = pybamm.Simulation(
        model,
        experiment=experiment,
        parameter_values=param,
    )
    solution.append(sim.solve())
stop = timeit.default_timer()
print("running time: " + str(stop - start) + "s")

plt.figure()
for i in range(0, len(v_si)):
    t_i = solution[i]["Time [s]"].entries / 3600
    V_i = solution[i]["Voltage [V]"].entries
    plt.plot(t_i, V_i, ltype[i], label="$V_\mathrm{si}=$" + str(v_si[i]))
plt.xlabel("Time [h]")
plt.ylabel("Voltage [V]")
plt.legend()
plt.savefig("composite_cycling_ocvs.png")
