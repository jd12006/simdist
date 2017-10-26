import numpy as np

def simulate_distribution(samples, distribution, n=10, p=0.5, lam=1.0):
    """
    Simulate numbers from a given distribution, output as numpy array.

    Input parameters
    samples: number of samples.
    distribution: Normal, Binomial or Poisson (string).
    n: number of trials; optional if Binomial chosen; >= 0; default = 10.
    p: probability of each trial; optional if Binomial chosen; >= 0 and <=1; default = 0.5.
    lam: lambda; optional if Poisson chosen; default = 1.0.

    """
    if distribution.lower() == "normal":
        return np.random.normal(loc = 0.0, scale = 1.0, size = samples)

    if distribution.lower() == "binomial":
        print("Parameters used: n =", n, "p =", p)
        return np.random.binomial(n, p, size = samples)

    if distribution.lower() == "poisson":
        print("Parameters used: lambda =", lam)
        return np.random.poisson(lam = lam, size = samples)

    else:
        print("Please specify a distribution")