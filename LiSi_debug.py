import matplotlib.pyplot as plt
from matplotlib import style
import pybamm
from Chen2020_composite_OG import get_parameter_values

style.use("ggplot")


"Primary Active Material"
rho_si = 2.336 #from ref (supplementary material)
wt_si = .679 #% from ref
"Secondary Active Material"
rho_c6 = 2.255 # (C-NERGYTM KS6L)
wt_c6 = .199
"Inactive Material"
rho_cb = 2.00 #from ref
wt_cb = 0.02 # from ref
rho_lipaa = 1.2 #ref
wt_lipaa = 0.082 # ref
rho_cmc = 1.6 #ref
wt_cmc = 0.002 #ref

v_tot  = wt_si/rho_si + wt_c6/rho_c6 + wt_cb/rho_cb + wt_lipaa/rho_lipaa + wt_cmc/rho_cmc
v_si = wt_si/rho_si
v_c6 = wt_c6/rho_c6
v_im = wt_c6/rho_c6 + wt_lipaa/rho_lipaa + wt_cmc/rho_cmc

eps_si = 0.5 * v_si / v_tot #times 0.5 to account for porosity (eps_ely = 0.5)
eps_c6 = 0.5 * v_c6 / v_tot
eps_am = 0.5* (v_si + v_c6) / v_tot

cell_volume = 0.0124*0.124*(92e-06 + 1.2e-05 + 2.6e-05 + 136e-06 +1.5e-05)

print("Volume fraction of Si: ", eps_si
      , "Volume fraction of C6: ", eps_c6, "Volume fraction of AM: ", eps_am, "cell volume: ", cell_volume)



model = pybamm.lithium_ion.DFN(
    {"particle phases": ("2", "1"),
     "open-circuit potential": (("single", "current sigmoid"), "single"),
    "SEI": "none",
    "lithium plating": "none",
    }
)


param = pybamm.ParameterValues(get_parameter_values())
# param = pybamm.ParameterValues("Chen2020_composite")


param.update(
    {
        "Primary: Negative electrode active material volume fraction": 0.09623602768522001, # primary
        "Secondary: Negative electrode active material volume fraction": 0.31697725057239584,
        "Negative electrode porosity": 0.5,
    }
    )


experiment = pybamm.Experiment(
    [
        (
            "Discharge at C/50 until 3.0 V",
            "Rest for 2 hours",
            "Charge at C/50 until 4.2 V",
        ),
    ]
)




sim = pybamm.Simulation(
    model,
    parameter_values=param,
    experiment = experiment,
    solver=pybamm.CasadiSolver(mode='safe', return_solution_if_failed_early=True)
)
solution = sim.solve()


pybamm.plot_voltage_components(solution)


sim.plot(output_variables=["Voltage [V]", 
                           "Current [A]",
                           "Negative primary particle surface concentration [mol.m-3]",
                           "Negative secondary particle surface concentration [mol.m-3]",
                           "Negative electrode potential [V]",
                           "Positive electrode potential [V]",
                           ])








# plt.figure()
# ltype = ["k-", "r--", "b-.", "g:", "m-", "c--", "y-."]
# t_i = solution["Time [s]"].entries / 3600
# OCP_i = solution["X-averaged negative electrode primary open-circuit potential [V]"].entries
# plt.plot(t_i, OCP_i, ltype[1])
# plt.xlabel("Time [h]")
# plt.ylabel("OCP [V]")
# plt.legend()
# plt.title("Graphite")
# plt.savefig("test.png")
