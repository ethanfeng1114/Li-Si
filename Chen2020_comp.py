import os

import numpy as np

import pybamm


def graphite_LGM50_electrolyte_exchange_current_density_Chen2020(
    c_e, c_s_surf, c_s_max, T
):
    """
    Exchange-current density for Butler-Volmer reactions between graphite and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 6.48e-7  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 35000
    arrhenius = np.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5


def silicon_ocp_lithiation_Mark2016(sto):
    """
    silicon Open-circuit Potential (OCP) as a a function of the
    stoichiometry. The fit is taken from the Enertech cell [1], which is only accurate
    for 0 < sto < 1.

    References
    ----------
    .. [1] Verbrugge M, Baker D, Xiao X. Formulation for the treatment of multiple
    electrochemical reactions and associated speciation for the Lithium-Silicon
    electrode[J]. Journal of The Electrochemical Society, 2015, 163(2): A262.

    Parameters
    ----------
    sto: double
       stoichiometry of material (li-fraction)

    Returns
    -------
    :class:`pybamm.Symbol`
        OCP [V]
    """
    p1 = -96.63
    p2 = 372.6
    p3 = -587.6
    p4 = 489.9
    p5 = -232.8
    p6 = 62.99
    p7 = -9.286
    p8 = 0.8633

    U_lithiation = (
        p1 * sto**7
        + p2 * sto**6
        + p3 * sto**5
        + p4 * sto**4
        + p5 * sto**3
        + p6 * sto**2
        + p7 * sto
        + p8
    )
    return U_lithiation


def silicon_ocp_delithiation_Mark2016(sto):
    """
    silicon Open-circuit Potential (OCP) as a a function of the
    stoichiometry. The fit is taken from the Enertech cell [1], which is only accurate
    for 0 < sto < 1.

    References
    ----------
    .. [1] Verbrugge M, Baker D, Xiao X. Formulation for the treatment of multiple
    electrochemical reactions and associated speciation for the Lithium-Silicon
    electrode[J]. Journal of The Electrochemical Society, 2015, 163(2): A262.

    Parameters
    ----------
    sto: double
       stoichiometry of material (li-fraction)

    Returns
    -------
    :class:`pybamm.Symbol`
        OCP [V]
    """
    p1 = -51.02
    p2 = 161.3
    p3 = -205.7
    p4 = 140.2
    p5 = -58.76
    p6 = 16.87
    p7 = -3.792
    p8 = 0.9937

    U_delithiation = (
        p1 * sto**7
        + p2 * sto**6
        + p3 * sto**5
        + p4 * sto**4
        + p5 * sto**3
        + p6 * sto**2
        + p7 * sto
        + p8
    )
    return U_delithiation


def silicon_ocp_average_Mark2016(sto):
    return (
        silicon_ocp_lithiation_Mark2016(sto) + silicon_ocp_delithiation_Mark2016(sto)
    ) / 2


def silicon_LGM50_electrolyte_exchange_current_density_Chen2020(
    c_e, c_s_surf, c_s_max, T
):
    """
    Exchange-current density for Butler-Volmer reactions between silicon and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """

    m_ref = (
        6.48e-7 * 28700 / 278000
    )  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 35000
    arrhenius = np.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5


def nmc_LGM50_ocp_Chen2020(sto):
    """
    LG M50 NMC open-circuit potential as a function of stoichiometry, fit taken
    from [1].

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stoichiometry

    Returns
    -------
    :class:`pybamm.Symbol`
        Open-circuit potential
    """

    u_eq = (
        -0.8090 * sto
        + 4.4875
        - 0.0428 * np.tanh(18.5138 * (sto - 0.5542))
        - 17.7326 * np.tanh(15.7890 * (sto - 0.3117))
        + 17.5842 * np.tanh(15.9308 * (sto - 0.3120))
    )

    return u_eq


def nmc_LGM50_electrolyte_exchange_current_density_Chen2020(c_e, c_s_surf, c_s_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between NMC and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 3.42e-6  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 17800
    arrhenius = np.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5


def electrolyte_diffusivity_Nyman2008(c_e, T):
    """
    Diffusivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1]

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

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

    D_c_e = 8.794e-11 * (c_e / 1000) ** 2 - 3.972e-10 * (c_e / 1000) + 4.862e-10

    # Nyman et al. (2008) does not provide temperature dependence

    return D_c_e


def electrolyte_conductivity_Nyman2008(c_e, T):
    """
    Conductivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1].

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

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

    sigma_e = (
        0.1297 * (c_e / 1000) ** 3 - 2.51 * (c_e / 1000) ** 1.5 + 3.329 * (c_e / 1000)
    )

    # Nyman et al. (2008) does not provide temperature dependence

    return sigma_e


# # Load data in the appropriate format
# path, _ = os.path.split(os.path.abspath(__file__))
# graphite_ocp_Enertech_Ai2020_data = pybamm.parameters.process_1D_data(
#     "graphite_ocp_Enertech_Ai2020.csv", path=path
# )

graphite_ocp_sto = np.array([
    0, 0.0005, 0.00127041, 0.00152479, 0.00190595, 0.002223558,
    0.004060547, 0.004820151, 0.006463943, 0.00741337, 0.008616506,
    0.009123417, 0.010768226, 0.012665046, 0.014118344, 0.017786752,
    0.02069469, 0.023983799, 0.030502175, 0.036001135, 0.039606662,
    0.059148083, 0.061297942, 0.071349833, 0.080265526, 0.119208079,
    0.128120548, 0.134253707, 0.141584594, 0.150874177, 0.160609131,
    0.170345957, 0.189747769, 0.209222253, 0.21901773, 0.228756579,
    0.238552575, 0.248349231, 0.258084023, 0.267821184, 0.28741535,
    0.297209811, 0.307004942, 0.316798396, 0.326534032, 0.336321558,
    0.346061758, 0.355856392, 0.365593044, 0.375388012, 0.385120781,
    0.394915577, 0.404717479, 0.414512102, 0.424244871, 0.434039331,
    0.44377024, 0.453564862, 0.463298139, 0.473034456, 0.482766544,
    0.492564552, 0.502302892, 0.512042595, 0.521833161, 0.531572182,
    0.541369033, 0.551104831, 0.5608998, 0.570635608, 0.580434806,
    0.590235692, 0.599977407, 0.609716266, 0.619517822, 0.629313635,
    0.639049108, 0.648790152, 0.658584104, 0.668320248, 0.67805504,
    0.687851869, 0.69764938, 0.707389072, 0.717188097, 0.726977148,
    0.736776336, 0.746515866, 0.756259106, 0.766055091, 0.775789039,
    0.785537861, 0.79532979, 0.805080646, 0.814827099, 0.824570003,
    0.834370889, 0.844173289, 0.853913187, 0.86365051, 0.873392073,
    0.883126865, 0.892918286, 0.902708516, 0.912443308, 0.922232533,
    0.932019724, 0.941812832, 0.951602392, 0.961392795, 0.970177652,
    0.976051358, 0.980413449, 0.983887804, 0.986792703, 0.989255096,
    0.991401407, 0.993359929, 0.995130154, 0.996776304, 0.99822944,
    0.999241066, 0.999746961, 0.999936448, 1
])

graphite_ocp_volt = np.array([
    3.5, 3, 1.04, 1.01, 0.972653837, 0.94249055,
    0.816240592, 0.780280928, 0.71896262, 0.691374757, 0.661391781,
    0.649962232, 0.6165173, 0.583310858, 0.560830783, 0.512439476,
    0.48025136, 0.448495867, 0.39598881, 0.359507681, 0.338477981,
    0.256319558, 0.25117361, 0.236055324, 0.231009217, 0.2232966,
    0.218284244, 0.213273859, 0.208228362, 0.203209739, 0.198620985,
    0.193816376, 0.184166915, 0.176790532, 0.173830441, 0.170963261,
    0.167903501, 0.164649979, 0.161491332, 0.15859383, 0.153399157,
    0.151002319, 0.14886213, 0.146918911, 0.145328142, 0.144002109,
    0.142902125, 0.142014262, 0.141316008, 0.140759105, 0.140314323,
    0.139942322, 0.139617851, 0.139325406, 0.139051014, 0.138779297,
    0.138517413, 0.138258897, 0.137981293, 0.137672226, 0.137329325,
    0.136903224, 0.136390244, 0.135757581, 0.134947101, 0.133923235,
    0.132621681, 0.130989474, 0.128964924, 0.126549987, 0.123742878,
    0.120770834, 0.117929634, 0.115379983, 0.113205423, 0.111366477,
    0.109855495, 0.108578952, 0.107520678, 0.106632536, 0.105893758,
    0.105260613, 0.104713189, 0.104254365, 0.103845625, 0.103477119,
    0.103153932, 0.102856541, 0.102587443, 0.102338279, 0.102101986,
    0.101880905, 0.101676423, 0.101465878, 0.101264171, 0.101062635,
    0.10087041, 0.10068096, 0.100489223, 0.100300437, 0.100099718,
    0.099877104, 0.099628985, 0.099332616, 0.098958419, 0.098442542,
    0.097683643, 0.096492, 0.094510791, 0.091136817, 0.086115186,
    0.081078748, 0.07604037, 0.070991535, 0.065898328, 0.060844047,
    0.055810118, 0.050670698, 0.045562401, 0.040392663, 0.035261272,
    0.030242658, 0.024850768, 0.019251502, 0.004994678
])


def graphite_ocp_Enertech_Ai2020(sto):
    #name, (x, y) = graphite_ocp_Enertech_Ai2020_data
    return pybamm.Interpolant(graphite_ocp_sto, graphite_ocp_volt, sto, name="graphite_ocp", interpolator="cubic")


# Call dict via a function to avoid errors when editing in place
def get_parameter_values():
    """
    Parameters for a composite graphite/silicon negative electrode, from the paper
    :footcite:t:`Ai2022`, based on the paper :footcite:t:`Chen2020`, and references
    therein.

    SEI parameters are example parameters for composite SEI on silicon/graphite. Both
    phases use the same values, from the paper :footcite:t:`Yang2017`
    """

    return {
        "chemistry": "lithium_ion",
        # sei
        "Primary: Ratio of lithium moles to SEI moles": 2.0,
        "Primary: SEI partial molar volume [m3.mol-1]": 9.585e-05,
        "Primary: SEI reaction exchange current density [A.m-2]": 1.5e-07,
        "Primary: SEI resistivity [Ohm.m]": 200000.0,
        "Primary: SEI solvent diffusivity [m2.s-1]": 2.5e-22,
        "Primary: Bulk solvent concentration [mol.m-3]": 2636.0,
        "Primary: SEI open-circuit potential [V]": 0.4,
        "Primary: SEI electron conductivity [S.m-1]": 8.95e-14,
        "Primary: SEI lithium interstitial diffusivity [m2.s-1]": 1e-20,
        "Primary: Lithium interstitial reference concentration [mol.m-3]": 15.0,
        "Primary: Initial SEI thickness [m]": 5e-09,
        "Primary: EC initial concentration in electrolyte [mol.m-3]": 4541.0,
        "Primary: EC diffusivity [m2.s-1]": 2e-18,
        "Primary: SEI kinetic rate constant [m.s-1]": 1e-12,
        "Primary: SEI growth activation energy [J.mol-1]": 0.0,
        "Secondary: Ratio of lithium moles to SEI moles": 2.0,
        "Secondary: SEI partial molar volume [m3.mol-1]": 9.585e-05,
        "Secondary: SEI reaction exchange current density [A.m-2]": 1.5e-07,
        "Secondary: SEI resistivity [Ohm.m]": 200000.0,
        "Secondary: SEI solvent diffusivity [m2.s-1]": 2.5e-22,
        "Secondary: Bulk solvent concentration [mol.m-3]": 2636.0,
        "Secondary: SEI open-circuit potential [V]": 0.4,
        "Secondary: SEI electron conductivity [S.m-1]": 8.95e-14,
        "Secondary: SEI lithium interstitial diffusivity [m2.s-1]": 1e-20,
        "Secondary: Lithium interstitial reference concentration [mol.m-3]": 15.0,
        "Secondary: Initial SEI thickness [m]": 5e-09,
        "Secondary: EC initial concentration in electrolyte [mol.m-3]": 4541.0,
        "Secondary: EC diffusivity [m2.s-1]": 2e-18,
        "Secondary: SEI kinetic rate constant [m.s-1]": 1e-12,
        "Secondary: SEI growth activation energy [J.mol-1]": 0.0,
        "Positive electrode reaction-driven LAM factor [m3.mol-1]": 0.0,
        # cell
        "Negative current collector thickness [m]": 1.2e-05, #supplementary material
        "Negative electrode thickness [m]": 92e-06, ##supplementary material
        "Separator thickness [m]": 2.6e-05, ##supplementary material
        "Positive electrode thickness [m]": 136e-06, #supplementary material
        "Positive current collector thickness [m]": 1.5e-05, #supplementary material
        "Electrode height [m]": 0.0124, #Supplementary material (causes weird behavior)
        "Electrode width [m]": 0.0124, #Supplementary material
        "Cell cooling surface area [m2]": 0.00531,
        "Cell volume [m3]": 1e-06, #cr2032
        "Cell thermal expansion coefficient [m.K-1]": 1.1e-06,
        "Negative current collector conductivity [S.m-1]": 58411000.0,
        "Positive current collector conductivity [S.m-1]": 36914000.0,
        "Negative current collector density [kg.m-3]": 8960.0,
        "Positive current collector density [kg.m-3]": 2700.0,
        "Negative current collector specific heat capacity [J.kg-1.K-1]": 385.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 897.0,
        "Negative current collector thermal conductivity [W.m-1.K-1]": 401.0,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 237.0,
        "Nominal cell capacity [A.h]": 5.809e-3, #Supplementary material (causes weird behavior-- default is 5)
        "Current function [A]": 5.809e-3, #??
        "Contact resistance [Ohm]": 0,
        # negative electrode
        "Negative electrode conductivity [S.m-1]": 215.0,
        "Primary: Maximum concentration in negative electrode [mol.m-3]": 28700.0,
        "Primary: Initial concentration in negative electrode [mol.m-3]": 27700.0,
        "Primary: Negative particle diffusivity [m2.s-1]": 5.5e-14,
        "Primary: Negative electrode OCP [V]": graphite_ocp_Enertech_Ai2020,
        "Negative electrode porosity": 0.25,
        "Primary: Negative electrode active material volume fraction": 0.735,
        "Primary: Negative particle radius [m]": 5.86e-06,
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Negative electrode Bruggeman coefficient (electrode)": 0,
        "Negative electrode charge transfer coefficient": 0.5,
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Primary: Negative electrode exchange-current density [A.m-2]"
        "": graphite_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Primary: Negative electrode density [kg.m-3]": 1657.0,
        "Negative electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Negative electrode thermal conductivity [W.m-1.K-1]": 1.7,
        "Primary: Negative electrode OCP entropic change [V.K-1]": 0.0,
        "Secondary: Maximum concentration in negative electrode [mol.m-3]": 278000.0,
        "Secondary: Initial concentration in negative electrode [mol.m-3]": 276610.0,
        "Secondary: Negative particle diffusivity [m2.s-1]": 1.67e-14,
        "Secondary: Negative electrode lithiation OCP [V]"
        "": silicon_ocp_lithiation_Mark2016,
        "Secondary: Negative electrode delithiation OCP [V]"
        "": silicon_ocp_delithiation_Mark2016,
        "Secondary: Negative electrode OCP [V]": silicon_ocp_average_Mark2016,
        "Secondary: Negative electrode active material volume fraction": 0.015,
        "Secondary: Negative particle radius [m]": 1.52e-06,
        "Secondary: Negative electrode exchange-current density [A.m-2]"
        "": silicon_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Secondary: Negative electrode density [kg.m-3]": 2650.0,
        "Secondary: Negative electrode OCP entropic change [V.K-1]": 0.0,
        # positive electrode
        "Positive electrode conductivity [S.m-1]": 0.18,
        "Maximum concentration in positive electrode [mol.m-3]": 63104.0,
        "Positive particle diffusivity [m2.s-1]": 4e-15,
        "Positive electrode OCP [V]": nmc_LGM50_ocp_Chen2020,
        "Positive electrode porosity": 0.335,
        "Positive electrode active material volume fraction": 0.665,
        "Positive particle radius [m]": 5.22e-06,
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Positive electrode Bruggeman coefficient (electrode)": 0,
        "Positive electrode charge transfer coefficient": 0.5,
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode exchange-current density [A.m-2]"
        "": nmc_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Positive electrode density [kg.m-3]": 3262.0,
        "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Positive electrode thermal conductivity [W.m-1.K-1]": 2.1,
        "Positive electrode OCP entropic change [V.K-1]": 0.0,
        # separator
        "Separator porosity": 0.47,
        "Separator Bruggeman coefficient (electrolyte)": 1.5,
        "Separator density [kg.m-3]": 397.0,
        "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
        "Separator thermal conductivity [W.m-1.K-1]": 0.16,
        # electrolyte
        "Initial concentration in electrolyte [mol.m-3]": 1000.0,
        "Cation transference number": 0.2594,
        "Thermodynamic factor": 1.0,
        "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity_Nyman2008,
        "Electrolyte conductivity [S.m-1]": electrolyte_conductivity_Nyman2008,
        # experiment
        "Reference temperature [K]": 298.15,
        "Total heat transfer coefficient [W.m-2.K-1]": 10.0,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]": 2.5,
        "Upper voltage cut-off [V]": 4.2,
        "Open-circuit voltage at 0% SOC [V]": 2.5,
        "Open-circuit voltage at 100% SOC [V]": 4.2,
        "Initial concentration in negative electrode [mol.m-3]": 29866.0,
        "Initial concentration in positive electrode [mol.m-3]": 17038.0,
        "Initial temperature [K]": 298.15,
        # citations
        "citations": ["Chen2020", "Ai2022"],
    }