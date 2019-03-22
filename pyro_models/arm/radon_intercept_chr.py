# model file: example-models/ARM/Ch.12/radon_intercept_chr.stan
import torch
import pyro
import pyro.distributions as dist

def init_vector(name, dims=None):
    return pyro.sample(name, dist.Normal(torch.zeros(dims), 0.2 * torch.ones(dims)).to_event(1))


def validate_data_def(data):
    assert 'N' in data, 'variable not found in data: key=N'
    assert 'J' in data, 'variable not found in data: key=J'
    assert 'county' in data, 'variable not found in data: key=county'
    assert 'y' in data, 'variable not found in data: key=y'
    # initialize data
    N = data["N"]
    J = data["J"]
    county = data["county"]
    y = data["y"]

def init_params(data):
    params = {}
    return params

def model(data, params):
    # initialize data
    N = data["N"]
    J = data["J"]
    county = data["county"].long() - 1
    y = data["y"]

    # model block
    mu_a =  pyro.sample("mu_a", dist.Normal(0., 1.))
    sigma_a =  pyro.sample("sigma_a", dist.HalfCauchy(2.5))
    with pyro.plate("J", J):
        eta =  pyro.sample("eta", dist.Normal(0., 1.))
        
    sigma =  pyro.sample("sigma", dist.HalfCauchy(2.5))
    a = 10 * mu_a + sigma_a * eta
    with pyro.plate("data", N):
        y_hat = a[county]
        y = pyro.sample('y', dist.Normal(y_hat, sigma), obs=y)
