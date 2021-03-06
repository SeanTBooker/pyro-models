# Copyright Contributors to the Pyro project.
# SPDX-License-Identifier: Apache-2.0

# model file: example-models/ARM/Ch.10/ideo_interactions.stan
import torch
import pyro
import pyro.distributions as dist

def init_vector(name, dims=None):
    return pyro.sample(name, dist.Normal(torch.zeros(dims), 0.2 * torch.ones(dims)).to_event(1))



def validate_data_def(data):
    assert 'N' in data, 'variable not found in data: key=N'
    assert 'party' in data, 'variable not found in data: key=party'
    assert 'score1' in data, 'variable not found in data: key=score1'
    assert 'x' in data, 'variable not found in data: key=x'
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]

def transformed_data(data):
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    inter = party * x
    data["inter"] = inter

def init_params(data):
    params = {}
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    # initialize transformed data
    # assign init values for parameters
    params["beta"] = init_vector("beta", dims=(4)) # vector
    params["sigma"] = pyro.sample("sigma", dist.Uniform(0., 100.))

    return params

def model(data, params):
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    # initialize transformed data
    inter = data["inter"]

    # init parameters
    beta = params["beta"]
    sigma = params["sigma"]
    # initialize transformed parameters
    # model block
    with pyro.plate("data", N):
        score1 = pyro.sample('score1', dist.Normal(beta[0] + beta[1] * party + beta[2] * x + beta[3] * inter, sigma), obs=score1)

