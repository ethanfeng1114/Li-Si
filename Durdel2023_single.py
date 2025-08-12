import numpy as np

import pybamm



def silicon_ocp_lithiation_Durdel2023(sto):

    silicon_lith_ocp_sto = np.array([0.03869, 0.03965, 0.04061, 0.04158, 0.04158, 0.0435, 0.0435, 0.04447, 0.0464, 0.04736, 0.05025, 0.05121, 0.05411, 0.05989, 0.06663, 0.07434, 0.08013, 0.09555, 0.10229, 0.11386, 0.12831, 0.13892, 0.14566, 0.15723, 0.17265, 0.17747, 0.18999, 0.2006, 0.21216, 0.22758, 0.23818, 0.24493, 0.25553, 0.26517, 0.2748, 0.29119, 0.29601])
    silicon_lith_ocp_volt = np.array([0.994, 0.9, 0.714, 0.62, 0.572, 0.54, 0.526, 0.504, 0.48, 0.456, 0.434, 0.412, 0.388, 0.356, 0.338, 0.322, 0.318, 0.306, 0.304, 0.298, 0.288, 0.282, 0.278, 0.274, 0.264, 0.262, 0.258, 0.252, 0.248, 0.238, 0.232, 0.23, 0.222, 0.214, 0.204, 0.19, 0.184])

    return pybamm.Interpolant(silicon_lith_ocp_sto, silicon_lith_ocp_volt, sto, name="silicon_lith_ocp", interpolator="linear", extrapolate=False)




def silicon_ocp_delithiation_Durdel2023(sto):

    silicon_delith_ocp_sto = np.array([0.03676, 0.0329, 0.03001, 0.02712, 0.02519, 0.02423, 0.0223, 0.02134, 0.02037, 0.01941, 0.01845, 0.01748, 0.03985, 0.04254, 0.04736, 0.05218, 0.057, 0.06374, 0.07049, 0.0782, 0.08687, 0.09651, 0.10615, 0.11579, 0.12542, 0.13506, 0.1447, 0.15434, 0.16397, 0.17361, 0.18325, 0.19289, 0.20252, 0.21216, 0.2218, 0.23144, 0.24107, 0.25071, 0.26035, 0.26999, 0.27962, 0.28637, 0.29215, 0.29601, 0.2989, 0.30083, 0.30275, 0.30468, 0.30661, 0.30661])
    silicon_delith_ocp_volt = np.array([0.77, 0.79, 0.81, 0.83, 0.85, 0.87, 0.89, 0.91, 0.93, 0.95, 0.97, 0.99, 0.75333, 0.736, 0.716, 0.696, 0.676, 0.656, 0.636, 0.616, 0.596, 0.576, 0.558, 0.542, 0.53, 0.518, 0.506, 0.496, 0.488, 0.48, 0.474, 0.466, 0.458, 0.452, 0.442, 0.434, 0.424, 0.412, 0.4, 0.386, 0.366, 0.346, 0.326, 0.306, 0.286, 0.266, 0.246, 0.226, 0.206, 0.186])

    return pybamm.Interpolant(silicon_delith_ocp_sto, silicon_delith_ocp_volt, sto, name="silicon_delith_ocp", interpolator="linear", extrapolate=False)


def silicon_ocp_average_Durdel2023(sto):
    return (
        silicon_ocp_lithiation_Durdel2023(sto) + silicon_ocp_delithiation_Durdel2023(sto)
    ) / 2


def nca_ocp_delithiation_Durdel2023(sto):

    nca_delith_ocp_sto = np.array([0.13762, 0.14125, 0.1509, 0.16054, 0.17019, 0.17983, 0.18947, 0.19912, 0.20876, 0.2184, 0.22805, 0.23769, 0.24734, 0.25698, 0.26662, 0.27627, 0.28591, 0.29555, 0.3052, 0.31484, 0.32448, 0.33413, 0.34377, 0.35342, 0.36306, 0.3727, 0.38235, 0.39199, 0.40163, 0.41128, 0.42092, 0.43057, 0.44021, 0.44985, 0.4595, 0.46914, 0.47878, 0.48843, 0.49807, 0.50771, 0.51736, 0.527, 0.53665, 0.54629, 0.55593, 0.56558, 0.57522, 0.58486, 0.59451, 0.60415, 0.6138, 0.62344, 0.63308, 0.64273, 0.65237, 0.66201, 0.67166, 0.6813, 0.69094, 0.70059, 0.71023, 0.71988, 0.72952, 0.73916, 0.74881, 0.75845, 0.76809, 0.77774, 0.78738, 0.79486, 0.80386, 0.81245, 0.8221, 0.83174, 0.84139, 0.85103, 0.86067, 0.86559, 0.86646, 0.86742, 0.86839, 0.86935])
    nca_delith_ocp_volt = np.array([4.39318, 4.36647, 4.32641, 4.29436, 4.26632, 4.24228, 4.22226, 4.20623, 4.19421, 4.17819, 4.16617, 4.14614, 4.13012, 4.1141, 4.09807, 4.08205, 4.06602, 4.05, 4.03798, 4.02596, 4.00994, 3.99792, 3.98991, 3.97789, 3.96588, 3.95386, 3.94184, 3.92982, 3.9178, 3.90579, 3.89377, 3.88175, 3.86973, 3.85772, 3.8457, 3.83769, 3.82166, 3.81365, 3.80564, 3.79362, 3.78561, 3.7776, 3.76958, 3.76157, 3.75356, 3.74555, 3.74154, 3.73353, 3.72552, 3.72151, 3.7135, 3.70549, 3.70148, 3.68947, 3.68546, 3.67745, 3.66944, 3.66142, 3.65341, 3.64139, 3.63338, 3.62137, 3.61335, 3.60534, 3.59733, 3.58932, 3.58131, 3.57329, 3.56929, 3.56528, 3.55994, 3.55727, 3.55326, 3.54926, 3.54125, 3.53323, 3.52923, 3.51721, 3.40104, 3.32092, 3.16068, 3.0405])

    return pybamm.Interpolant(nca_delith_ocp_sto, nca_delith_ocp_volt, sto, name="nca_delith_ocp", interpolator="linear", extrapolate=False)


def nca_ocp_lithiation_Durdel2023(sto):

    nca_lith_ocp_sto = np.array([0.13933, 0.14801, 0.15765, 0.16729, 0.17694, 0.18658, 0.19622, 0.20587, 0.21551, 0.22515, 0.2348, 0.24444, 0.25409, 0.26373, 0.27337, 0.28302, 0.29266, 0.3023, 0.31195, 0.32159, 0.33124, 0.34088, 0.35052, 0.36017, 0.36981, 0.37945, 0.3891, 0.39874, 0.40838, 0.41803, 0.42767, 0.43732, 0.44696, 0.4566, 0.46625, 0.47589, 0.48553, 0.49518, 0.50482, 0.51447, 0.52411, 0.53375, 0.5434, 0.55304, 0.56268, 0.57233, 0.58197, 0.59161, 0.60126, 0.6109, 0.62055, 0.63019, 0.63983, 0.64948, 0.65912, 0.66876, 0.67841, 0.6977, 0.70734, 0.71698, 0.72663, 0.73627, 0.74591, 0.75556, 0.7652, 0.77484, 0.78449, 0.79614, 0.80763, 0.81728, 0.82692, 0.83656, 0.84621, 0.85585, 0.8655, 0.87803, 0.8896, 0.89346, 0.89635, 0.89828, 0.89925, 0.90214])
    nca_lith_ocp_volt = np.array([4.37849, 4.33843, 4.30638, 4.27433, 4.2503, 4.23027, 4.21424, 4.19822, 4.1822, 4.16617, 4.15015, 4.13412, 4.1181, 4.10208, 4.08605, 4.07003, 4.05401, 4.04199, 4.02997, 4.01795, 4.00193, 3.98991, 3.97789, 3.96988, 3.95786, 3.94585, 3.93383, 3.92181, 3.90979, 3.89777, 3.88576, 3.87374, 3.86172, 3.8497, 3.83769, 3.82567, 3.81365, 3.80564, 3.79763, 3.78961, 3.7816, 3.77359, 3.76558, 3.75757, 3.74955, 3.74154, 3.73353, 3.72953, 3.72151, 3.71751, 3.7095, 3.70148, 3.69347, 3.68947, 3.68145, 3.66944, 3.65742, 3.64139, 3.63338, 3.62537, 3.61736, 3.60935, 3.60134, 3.59332, 3.58531, 3.58131, 3.57329, 3.56528, 3.56128, 3.55326, 3.54926, 3.54525, 3.54125, 3.53323, 3.51721, 3.46113, 3.38501, 3.29688, 3.21677, 3.15668, 3.12062, 3.01246])

    return pybamm.Interpolant(nca_lith_ocp_sto, nca_lith_ocp_volt, sto, name="nca_lith_ocp", interpolator="linear", extrapolate=False)

def nca_ocp_average_Durdel2023(sto):
    return (
        nca_ocp_lithiation_Durdel2023(sto) + nca_ocp_delithiation_Durdel2023(sto)
    ) / 2





def salt_diffusivity_Durdel2023(c_e, T):
    """

    (cite durdeL)

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """
    # PyBaMM gives c_e in mol/m^3; convert to mol/L
    c_M = c_e / 1000
    exp = -4.43 - (54 / (T - (229 + 5 * c_M))) - 0.22 * c_M
    D = 1e-4 * 10 ** exp


    return D



def get_final_parameter_values():
    #this is the final parameter set as copied from Durdel 2023
    """
    Parameters for a "Nominal Design" graphite/NCA pouch cell, from the paper
    :footcite:t:`Kim2011`

    .. note::
        Only an effective cell volumetric heat capacity is provided in the paper. We
        therefore used the values for the density and specific heat capacity reported in
        the Marquis2019 parameter set in each region and multiplied each density by the
        ratio of the volumetric heat capacity provided in smith to the calculated value.
        This ensures that the values produce the same effective cell volumetric heat
        capacity. This works fine for thermal models that are averaged over the
        x-direction but not for full (PDE in x direction) thermal models. We do the same
        for the planar effective thermal conductivity.

    SEI parameters are example parameters for SEI growth from the papers
    :footcite:t:`Ramadass2004`, :footcite:t:`Ploehn2004`,
    :footcite:t:`Single2018`, :footcite:t:`Safari2008`, and
    :footcite:t:`Yang2017`

    .. note::
        This parameter set does not claim to be representative of the true parameter
        values. Instead these are parameter values that were used to fit SEI models to
        observed experimental data in the referenced papers.
    """

    return {
        "chemistry": "lithium_ion",
        # sei
        "Ratio of lithium moles to SEI moles": 2.0,
        "SEI partial molar volume [m3.mol-1]": 9.585e-05,
        "SEI reaction exchange current density [A.m-2]": 1.5e-07,
        "SEI resistivity [Ohm.m]": 200000.0,
        "SEI solvent diffusivity [m2.s-1]": 2.5e-22,
        "Bulk solvent concentration [mol.m-3]": 2636.0,
        "SEI open-circuit potential [V]": 0.4,
        "SEI electron conductivity [S.m-1]": 8.95e-14,
        "SEI lithium interstitial diffusivity [m2.s-1]": 1e-20,
        "Lithium interstitial reference concentration [mol.m-3]": 15.0,
        "Initial SEI thickness [m]": 5e-09,
        "EC initial concentration in electrolyte [mol.m-3]": 4541.0,
        "EC diffusivity [m2.s-1]": 2e-18,
        "SEI kinetic rate constant [m.s-1]": 1e-12,
        "SEI growth activation energy [J.mol-1]": 0.0,
        "Negative electrode reaction-driven LAM factor [m3.mol-1]": 0.0,
        "Positive electrode reaction-driven LAM factor [m3.mol-1]": 0.0,
        # cell
        "Negative current collector thickness [m]": 1.2e-05, #supplementary material
        "Negative electrode thickness [m]": 92e-06, ##supplementary material
        "Separator thickness [m]": 2.6e-05, ##supplementary material
        "Positive electrode thickness [m]": 136e-06, #supplementary material
        "Positive current collector thickness [m]": 1.5e-05, #supplementary material
        "Electrode height [m]": 0.0124, #Supplementary material (causes weird behavior)
        "Electrode width [m]": 0.0124, #Supplementary material
        "Negative tab width [m]": 0.044,
        "Negative tab centre y-coordinate [m]": 0.013,
        "Negative tab centre z-coordinate [m]": 0.2,
        "Positive tab width [m]": 0.044,
        "Positive tab centre y-coordinate [m]": 0.137,
        "Positive tab centre z-coordinate [m]": 0.2,
        "Cell cooling surface area [m2]": 0.0561,
        "Cell volume [m3]": 1e-06, #cr2032
        "Negative current collector conductivity [S.m-1]": 59600000.0,
        "Positive current collector conductivity [S.m-1]": 37800000.0,
        "Negative current collector density [kg.m-3]": 11544.75,
        "Positive current collector density [kg.m-3]": 3490.24338,
        "Negative current collector specific heat capacity [J.kg-1.K-1]": 385.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 897.0,
        "Negative current collector thermal conductivity [W.m-1.K-1]": 267.467,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 158.079,
        "Nominal cell capacity [A.h]": 5.809e-3, #Supplementary material 
        "Current function [A]": 5.809e-3, #
        "Contact resistance [Ohm]": 0,
        # negative electrode
        "Negative electrode conductivity [S.m-1]": 33.0, #3.4
        "Maximum concentration in negative electrode [mol.m-3]": 322067.0, #Table A2
        "Negative particle diffusivity [m2.s-1]": 2e-15, #3.6
        "Negative electrode lithiation OCP [V]": silicon_ocp_lithiation_Durdel2023,
        "Negative electrode delithiation OCP [V]": silicon_ocp_delithiation_Durdel2023,
        "Negative electrode OCP [V]": silicon_ocp_average_Durdel2023,
        "Negative electrode porosity": 0.5, #Table A2
        "Negative electrode active material volume fraction": 0.31697725057239584, #calculated for si
        "Negative particle radius [m]": 2.25e-06, #Table A2
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5, #from chen2020
        "Negative electrode Bruggeman coefficient (electrode)": 0, #from chen2020
        "Negative electrode charge transfer coefficient": 0.5, #Table A2
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Negative electrode exchange-current density [A.m-2]": 2.2, #Table 2
        "Negative electrode density [kg.m-3]": 2336.0, #supplementary material
        "Negative electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Negative electrode thermal conductivity [W.m-1.K-1]": 1.1339,
        "Negative electrode OCP entropic change [V.K-1]": 0.0,
        # positive electrode
        "Positive electrode conductivity [S.m-1]": 100, #3.4
        "Maximum concentration in positive electrode [mol.m-3]": 46400.0, #Table A2
        "Positive particle diffusivity [m2.s-1]": 6e-15, #3.6
        "Positive electrode lithiation OCP [V]": nca_ocp_lithiation_Durdel2023,
        "Positive electrode delithiation OCP [V]": nca_ocp_delithiation_Durdel2023,
        "Positive electrode OCP [V]": nca_ocp_average_Durdel2023,
        "Positive electrode porosity": 0.32, #Table A2
        "Positive electrode active material volume fraction": 0.61, #Table A2
        "Positive particle radius [m]": 3.0755e-06, #Table A2
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5, #from chen2020
        "Positive electrode Bruggeman coefficient (electrode)": 0, #from chen2020
        "Positive electrode charge transfer coefficient": 0.5, #Table A2
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode exchange-current density [A.m-2]": 9.11, #Table 2
        "Positive electrode density [kg.m-3]": 4730.0, #Supplementary material,
        "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Positive electrode thermal conductivity [W.m-1.K-1]": 1.4007,
        "Positive electrode OCP entropic change [V.K-1]": 0.0,
        # separator
        "Separator porosity": 0.93, #supplementary material
        "Separator Bruggeman coefficient (electrolyte)": 2.0,
        "Separator density [kg.m-3]": 511.86798,
        "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
        "Separator thermal conductivity [W.m-1.K-1]": 0.10672,
        # electrolyte
        "Initial concentration in electrolyte [mol.m-3]": 1200.0,
        "Cation transference number": 0.38, #Table A2
        "Thermodynamic factor": 1.0,
        "Electrolyte diffusivity [m2.s-1]": salt_diffusivity_Durdel2023, #Table A2
        "Electrolyte conductivity [S.m-1]": 0.6398, #3.3
        # experiment
        "Reference temperature [K]": 298.15,
        "Negative current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Positive current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Negative tab heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Positive tab heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Edge heat transfer coefficient [W.m-2.K-1]": 0.3,
        "Total heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]": 2.8,
        "Upper voltage cut-off [V]": 4.2,
        "Open-circuit voltage at 0% SOC [V]": 2.8,
        "Open-circuit voltage at 100% SOC [V]": 4.2,
        "Initial concentration in negative electrode [mol.m-3]": 0.1732 * 3.22067e5,
        "Initial concentration in positive electrode [mol.m-3]": 0.4675 * 4.6400e4,
        "Initial temperature [K]": 298.15,
        # citations
        "citations": ["Kim2011"],
    }












def get_test_parameter_values():
    #this is the testing stage where I change parameters individually to sim and debug
    """
    Parameters for a "Nominal Design" graphite/NCA pouch cell, from the paper
    :footcite:t:`Kim2011`

    .. note::
        Only an effective cell volumetric heat capacity is provided in the paper. We
        therefore used the values for the density and specific heat capacity reported in
        the Marquis2019 parameter set in each region and multiplied each density by the
        ratio of the volumetric heat capacity provided in smith to the calculated value.
        This ensures that the values produce the same effective cell volumetric heat
        capacity. This works fine for thermal models that are averaged over the
        x-direction but not for full (PDE in x direction) thermal models. We do the same
        for the planar effective thermal conductivity.

    SEI parameters are example parameters for SEI growth from the papers
    :footcite:t:`Ramadass2004`, :footcite:t:`Ploehn2004`,
    :footcite:t:`Single2018`, :footcite:t:`Safari2008`, and
    :footcite:t:`Yang2017`

    .. note::
        This parameter set does not claim to be representative of the true parameter
        values. Instead these are parameter values that were used to fit SEI models to
        observed experimental data in the referenced papers.
    """

    return {
        "chemistry": "lithium_ion",
        # sei
        "Ratio of lithium moles to SEI moles": 2.0,
        "SEI partial molar volume [m3.mol-1]": 9.585e-05,
        "SEI reaction exchange current density [A.m-2]": 1.5e-07,
        "SEI resistivity [Ohm.m]": 200000.0,
        "SEI solvent diffusivity [m2.s-1]": 2.5e-22,
        "Bulk solvent concentration [mol.m-3]": 2636.0,
        "SEI open-circuit potential [V]": 0.4,
        "SEI electron conductivity [S.m-1]": 8.95e-14,
        "SEI lithium interstitial diffusivity [m2.s-1]": 1e-20,
        "Lithium interstitial reference concentration [mol.m-3]": 15.0,
        "Initial SEI thickness [m]": 5e-09,
        "EC initial concentration in electrolyte [mol.m-3]": 4541.0,
        "EC diffusivity [m2.s-1]": 2e-18,
        "SEI kinetic rate constant [m.s-1]": 1e-12,
        "SEI growth activation energy [J.mol-1]": 0.0,
        "Negative electrode reaction-driven LAM factor [m3.mol-1]": 0.0,
        "Positive electrode reaction-driven LAM factor [m3.mol-1]": 0.0,
        # cell
        "Negative current collector thickness [m]": 1.2e-05, #supplementary material
        "Negative electrode thickness [m]": 92e-06, ##supplementary material
        "Separator thickness [m]": 2.6e-05, ##supplementary material
        "Positive electrode thickness [m]": 136e-06, #supplementary material
        "Positive current collector thickness [m]": 1.5e-05, #supplementary material
        "Electrode height [m]": 0.0124, #Supplementary material (causes weird behavior)
        "Electrode width [m]": 0.0124, #Supplementary material
        "Negative tab width [m]": 0.044,
        "Negative tab centre y-coordinate [m]": 0.013,
        "Negative tab centre z-coordinate [m]": 0.2,
        "Positive tab width [m]": 0.044,
        "Positive tab centre y-coordinate [m]": 0.137,
        "Positive tab centre z-coordinate [m]": 0.2,
        "Cell cooling surface area [m2]": 0.0561,
        "Cell volume [m3]": 1e-06, #cr2032
        "Negative current collector conductivity [S.m-1]": 59600000.0,
        "Positive current collector conductivity [S.m-1]": 37800000.0,
        "Negative current collector density [kg.m-3]": 11544.75,
        "Positive current collector density [kg.m-3]": 3490.24338,
        "Negative current collector specific heat capacity [J.kg-1.K-1]": 385.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 897.0,
        "Negative current collector thermal conductivity [W.m-1.K-1]": 267.467,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 158.079,
        "Nominal cell capacity [A.h]": 5.809e-3, #Supplementary material (causes weird behavior-- default is 5)
        "Current function [A]": 5.809e-3, #??
        "Contact resistance [Ohm]": 0,
        # negative electrode
        "Negative electrode conductivity [S.m-1]": 33.0, #3.4
        "Maximum concentration in negative electrode [mol.m-3]": 322067.0, #Table A2
        "Negative particle diffusivity [m2.s-1]": 2e-15, #3.6
        "Negative electrode lithiation OCP [V]": silicon_ocp_lithiation_Durdel2023,
        "Negative electrode delithiation OCP [V]": silicon_ocp_delithiation_Durdel2023,
        "Negative electrode OCP [V]": silicon_ocp_average_Durdel2023,
        "Negative electrode porosity": 0.5, #Table A2
        "Negative electrode active material volume fraction": 0.31697725057239584, #calculated for si
        "Negative particle radius [m]": 2.25e-06, #Table A2
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5, #from chen2020
        "Negative electrode Bruggeman coefficient (electrode)": 0, #from chen2020
        "Negative electrode charge transfer coefficient": 0.5, #Table A2
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Negative electrode exchange-current density [A.m-2]": 2.2, #Table 2
        "Negative electrode density [kg.m-3]": 2336.0, #supplementary material
        "Negative electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Negative electrode thermal conductivity [W.m-1.K-1]": 1.1339,
        "Negative electrode OCP entropic change [V.K-1]": 0.0,
        # positive electrode
        "Positive electrode conductivity [S.m-1]": 100, #3.4
        "Maximum concentration in positive electrode [mol.m-3]": 46400.0, #Table A2
        "Positive particle diffusivity [m2.s-1]": 6e-15, #3.6
        "Positive electrode lithation OCP [V]": nca_ocp_lithiation_Durdel2023,
        "Positive electrode delithation OCP [V]": nca_ocp_delithiation_Durdel2023,
        "Positive electrode OCP [V]": nca_ocp_average_Durdel2023,
        "Positive electrode porosity": 0.32, #Table A2
        "Positive electrode active material volume fraction": 0.61, #Table A2
        "Positive particle radius [m]": 3.0755e-06, #Table A2
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5, #from chen2020
        "Positive electrode Bruggeman coefficient (electrode)": 0, #from chen2020
        "Positive electrode charge transfer coefficient": 0.5, #Table A2
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode exchange-current density [A.m-2]": 9.11, #Table 2
        "Positive electrode density [kg.m-3]": 4730.0, #Supplementary material,
        "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Positive electrode thermal conductivity [W.m-1.K-1]": 1.4007,
        "Positive electrode OCP entropic change [V.K-1]": 0.0,
        # separator
        "Separator porosity": 0.93, #supplementary material
        "Separator Bruggeman coefficient (electrolyte)": 2.0,
        "Separator density [kg.m-3]": 511.86798,
        "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
        "Separator thermal conductivity [W.m-1.K-1]": 0.10672,
        # electrolyte
        "Initial concentration in electrolyte [mol.m-3]": 1200.0,
        "Cation transference number": 0.38, #Table A2
        "Thermodynamic factor": 1.0,
        "Electrolyte diffusivity [m2.s-1]": salt_diffusivity_Durdel2023, #Table A2
        "Electrolyte conductivity [S.m-1]": 0.6398, #3.3
        # experiment
        "Reference temperature [K]": 298.15,
        "Negative current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Positive current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Negative tab heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Positive tab heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Edge heat transfer coefficient [W.m-2.K-1]": 0.3,
        "Total heat transfer coefficient [W.m-2.K-1]": 25.0,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]": 2.8,
        "Upper voltage cut-off [V]": 4.2,
        "Open-circuit voltage at 0% SOC [V]": 2.7,
        "Open-circuit voltage at 100% SOC [V]": 4.2,
        "Initial concentration in negative electrode [mol.m-3]": 18081.0,
        "Initial concentration in positive electrode [mol.m-3]": 20090.0,
        "Initial temperature [K]": 298.15,
        # citations
        "citations": ["Kim2011"],
    }









