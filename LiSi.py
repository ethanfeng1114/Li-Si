import os
import timeit
import matplotlib.pyplot as plt
from matplotlib import style
import pybamm
from Durdel2023 import get_parameter_values

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

print("Volume fraction of Si: ", eps_si
      , "Volume fraction of C6: ", eps_c6, "Volume fraction of AM: ", eps_am)



start = timeit.default_timer()
model = pybamm.lithium_ion.DFN(
    {"particle phases": ("2", "1"),
     "open-circuit potential": (("single", "current sigmoid"), "single"),
    }
)

param_dict = get_parameter_values()
param = pybamm.ParameterValues(param_dict)



#Cycling

experiment = pybamm.Experiment(
    [
        (
            "Discharge at C/50 until 3.0 V",
            "Charge at C/50 until 4.2 V",
        ),
    ]
)


solution = []
# param.update(
# {
#         "Primary: Negative electrode active material volume fraction": (1 - eps_si)
#         * eps_am,  # primary (graphite)
#         "Secondary: Negative electrode active material volume fraction": eps_si
#         * eps_am, # secondary (silicon)
#      }
# )
#????????


 
sim = pybamm.Simulation(
    model,
    experiment=experiment,
    parameter_values=param,
    solver=pybamm.CasadiSolver(dt_max=1, atol=1e-8, rtol=1e-8),
)
solution = sim.solve()
stop = timeit.default_timer()
print("running time: " + str(stop - start) + "s")

plt.figure()
ltype = ["k-", "r--", "b-.", "g:", "m-", "c--", "y-."]

t_i = solution["Time [s]"].entries / 3600
V_i = solution["Voltage [V]"].entries
plt.plot(t_i, V_i, ltype[1], label="$V_\mathrm{si}=$" + str(v_si))
plt.xlabel("Time [h]")
plt.ylabel("Voltage [V]")
plt.legend()
plt.savefig("LiSi.png")
