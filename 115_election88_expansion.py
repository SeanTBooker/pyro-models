# model file: ../example-models/ARM/Ch.19/election88_expansion.stan
import torch
import pyro
from pyro_utils import (to_float, _pyro_sample, _call_func, check_constraints,
init_real, init_vector, init_simplex, init_matrix, init_int, _index_select, to_int, _pyro_assign, as_bool)
def validate_data_def(data):
    assert 'N' in data, 'variable not found in data: key=N'
    assert 'n_age' in data, 'variable not found in data: key=n_age'
    assert 'n_age_edu' in data, 'variable not found in data: key=n_age_edu'
    assert 'n_edu' in data, 'variable not found in data: key=n_edu'
    assert 'n_region' in data, 'variable not found in data: key=n_region'
    assert 'n_state' in data, 'variable not found in data: key=n_state'
    assert 'age' in data, 'variable not found in data: key=age'
    assert 'age_edu' in data, 'variable not found in data: key=age_edu'
    assert 'black' in data, 'variable not found in data: key=black'
    assert 'edu' in data, 'variable not found in data: key=edu'
    assert 'female' in data, 'variable not found in data: key=female'
    assert 'region' in data, 'variable not found in data: key=region'
    assert 'state' in data, 'variable not found in data: key=state'
    assert 'v_prev' in data, 'variable not found in data: key=v_prev'
    assert 'y' in data, 'variable not found in data: key=y'
    # initialize data
    N = data["N"]
    n_age = data["n_age"]
    n_age_edu = data["n_age_edu"]
    n_edu = data["n_edu"]
    n_region = data["n_region"]
    n_state = data["n_state"]
    age = data["age"]
    age_edu = data["age_edu"]
    black = data["black"]
    edu = data["edu"]
    female = data["female"]
    region = data["region"]
    state = data["state"]
    v_prev = data["v_prev"]
    y = data["y"]
    check_constraints(N, low=0, dims=[1])
    check_constraints(n_age, low=0, dims=[1])
    check_constraints(n_age_edu, low=0, dims=[1])
    check_constraints(n_edu, low=0, dims=[1])
    check_constraints(n_region, low=0, dims=[1])
    check_constraints(n_state, low=0, dims=[1])
    check_constraints(age, low=1, high=n_age, dims=[N])
    check_constraints(age_edu, low=1, high=n_age_edu, dims=[N])
    check_constraints(black, low=0, high=1, dims=[N])
    check_constraints(edu, low=1, high=n_edu, dims=[N])
    check_constraints(female, low=0, high=1, dims=[N])
    check_constraints(region, low=1, high=n_region, dims=[n_state])
    check_constraints(state, low=1, high=n_state, dims=[N])
    check_constraints(v_prev, dims=[n_state])
    check_constraints(y, low=0, high=1, dims=[N])

def init_params(data, params):
    # initialize data
    N = data["N"]
    n_age = data["n_age"]
    n_age_edu = data["n_age_edu"]
    n_edu = data["n_edu"]
    n_region = data["n_region"]
    n_state = data["n_state"]
    age = data["age"]
    age_edu = data["age_edu"]
    black = data["black"]
    edu = data["edu"]
    female = data["female"]
    region = data["region"]
    state = data["state"]
    v_prev = data["v_prev"]
    y = data["y"]
    # assign init values for parameters
    params["b_0"] = init_real("b_0") # real/double
    params["b_black"] = init_real("b_black") # real/double
    params["b_female"] = init_real("b_female") # real/double
    params["b_female_black"] = init_real("b_female_black") # real/double
    params["b_v_prev_raw"] = init_real("b_v_prev_raw") # real/double
    params["beta"] = init_vector("beta", dims=(4)) # vector
    params["b_age_edu"] = init_vector("b_age_edu", dims=(n_age_edu)) # vector
    params["b_age_raw"] = init_vector("b_age_raw", dims=(n_age)) # vector
    params["b_edu_raw"] = init_vector("b_edu_raw", dims=(n_edu)) # vector
    params["b_region_raw"] = init_vector("b_region_raw", dims=(n_region)) # vector
    params["b_state_raw"] = init_vector("b_state_raw", dims=(n_state)) # vector
    params["mu"] = init_real("mu") # real/double
    params["mu_age_edu"] = init_real("mu_age_edu") # real/double
    params["sigma_age_raw"] = init_real("sigma_age_raw", low=0) # real/double
    params["sigma_edu_raw"] = init_real("sigma_edu_raw", low=0) # real/double
    params["sigma_region_raw"] = init_real("sigma_region_raw", low=0) # real/double
    params["sigma_state_raw"] = init_real("sigma_state_raw", low=0) # real/double
    params["sigma_age_edu_raw"] = init_real("sigma_age_edu_raw", low=0) # real/double
    params["xi_age"] = init_real("xi_age", low=0) # real/double
    params["xi_edu"] = init_real("xi_edu", low=0) # real/double
    params["xi_age_edu"] = init_real("xi_age_edu", low=0) # real/double
    params["xi_state"] = init_real("xi_state", low=0) # real/double

def model(data, params):
    # initialize data
    N = data["N"]
    n_age = data["n_age"]
    n_age_edu = data["n_age_edu"]
    n_edu = data["n_edu"]
    n_region = data["n_region"]
    n_state = data["n_state"]
    age = data["age"]
    age_edu = data["age_edu"]
    black = data["black"]
    edu = data["edu"]
    female = data["female"]
    region = data["region"]
    state = data["state"]
    v_prev = data["v_prev"]
    y = data["y"]
    # INIT parameters
    b_0 = params["b_0"]
    b_black = params["b_black"]
    b_female = params["b_female"]
    b_female_black = params["b_female_black"]
    b_v_prev_raw = params["b_v_prev_raw"]
    beta = params["beta"]
    b_age_edu = params["b_age_edu"]
    b_age_raw = params["b_age_raw"]
    b_edu_raw = params["b_edu_raw"]
    b_region_raw = params["b_region_raw"]
    b_state_raw = params["b_state_raw"]
    mu = params["mu"]
    mu_age_edu = params["mu_age_edu"]
    sigma_age_raw = params["sigma_age_raw"]
    sigma_edu_raw = params["sigma_edu_raw"]
    sigma_region_raw = params["sigma_region_raw"]
    sigma_state_raw = params["sigma_state_raw"]
    sigma_age_edu_raw = params["sigma_age_edu_raw"]
    xi_age = params["xi_age"]
    xi_edu = params["xi_edu"]
    xi_age_edu = params["xi_age_edu"]
    xi_state = params["xi_state"]
    # initialize transformed parameters
    Xbeta = init_vector("Xbeta", dims=(N)) # vector
    b_age = init_vector("b_age", dims=(n_age)) # vector
    b_age_edu_adj = init_vector("b_age_edu_adj", dims=(n_age_edu)) # vector
    b_edu = init_vector("b_edu", dims=(n_edu)) # vector
    b_region = init_vector("b_region", dims=(n_region)) # vector
    b_state = init_vector("b_state", dims=(n_state)) # vector
    b_state_hat = init_vector("b_state_hat", dims=(n_state)) # vector
    mu_adj = init_real("mu_adj") # real/double
    sigma_age = init_real("sigma_age", low=0) # real/double
    sigma_edu = init_real("sigma_edu", low=0) # real/double
    sigma_age_edu = init_real("sigma_age_edu", low=0) # real/double
    sigma_state = init_real("sigma_state", low=0) # real/double
    sigma_region = init_real("sigma_region", low=0) # real/double
    b_age = _pyro_assign(b_age, _call_func("multiply", [xi_age,_call_func("subtract", [b_age_raw,_call_func("mean", [b_age_raw])])]))
    b_edu = _pyro_assign(b_edu, _call_func("multiply", [xi_edu,_call_func("subtract", [b_edu_raw,_call_func("mean", [b_edu_raw])])]))
    b_age_edu_adj = _pyro_assign(b_age_edu_adj, _call_func("subtract", [b_age_edu,_call_func("mean", [b_age_edu])]))
    b_region = _pyro_assign(b_region, _call_func("multiply", [xi_state,b_region_raw]))
    b_state = _pyro_assign(b_state, _call_func("multiply", [xi_state,_call_func("subtract", [b_state_raw,_call_func("mean", [b_state_raw])])]))
    mu_adj = _pyro_assign(mu_adj, ((((_index_select(beta, 1 - 1)  + _call_func("mean", [b_age])) + _call_func("mean", [b_edu])) + _call_func("mean", [b_age_edu])) + _call_func("mean", [b_state])))
    sigma_age = _pyro_assign(sigma_age, (xi_age * sigma_age_raw))
    sigma_edu = _pyro_assign(sigma_edu, (xi_edu * sigma_edu_raw))
    sigma_age_edu = _pyro_assign(sigma_age_edu, (xi_age_edu * sigma_age_edu_raw))
    sigma_state = _pyro_assign(sigma_state, (xi_state * sigma_state_raw))
    sigma_region = _pyro_assign(sigma_region, (xi_state * sigma_region_raw))
    for i in range(1, to_int(N) + 1):
        Xbeta[i - 1] = _pyro_assign(Xbeta[i - 1], (((((((_index_select(beta, 1 - 1)  + (_index_select(beta, 2 - 1)  * _index_select(female, i - 1) )) + (_index_select(beta, 3 - 1)  * _index_select(black, i - 1) )) + ((_index_select(beta, 4 - 1)  * _index_select(female, i - 1) ) * _index_select(black, i - 1) )) + _index_select(b_age, age[i - 1] - 1) ) + _index_select(b_edu, edu[i - 1] - 1) ) + _index_select(b_age_edu, age_edu[i - 1] - 1) ) + _index_select(b_state, state[i - 1] - 1) ))
    for j in range(1, to_int(n_state) + 1):
        b_state_hat[j - 1] = _pyro_assign(b_state_hat[j - 1], (_index_select(b_region_raw, region[j - 1] - 1)  + (b_v_prev_raw * _index_select(v_prev, j - 1) )))
    # model block

    mu =  _pyro_sample(mu, "mu", "normal", [0, 100])
    mu_age_edu =  _pyro_sample(mu_age_edu, "mu_age_edu", "normal", [0, 1])
    b_age_raw =  _pyro_sample(b_age_raw, "b_age_raw", "normal", [0, sigma_age_raw])
    b_edu_raw =  _pyro_sample(b_edu_raw, "b_edu_raw", "normal", [0, sigma_edu_raw])
    b_age_edu =  _pyro_sample(b_age_edu, "b_age_edu", "normal", [(100 * mu_age_edu), sigma_age_edu])
    b_state_raw =  _pyro_sample(b_state_raw, "b_state_raw", "normal", [b_state_hat, sigma_state_raw])
    beta =  _pyro_sample(beta, "beta", "normal", [0, 100])
    b_v_prev_raw =  _pyro_sample(b_v_prev_raw, "b_v_prev_raw", "normal", [0, 100])
    b_region_raw =  _pyro_sample(b_region_raw, "b_region_raw", "normal", [0, sigma_region_raw])
    y =  _pyro_sample(y, "y", "bernoulli_logit", [Xbeta], obs=y)
