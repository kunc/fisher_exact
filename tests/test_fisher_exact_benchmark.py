from fisher_exact import fisher_exact
import scipy.stats as ss
import numpy.testing as npt

DECIMAL = 10




def test_fisher_exact_01_our(benchmark):
    table = [[1, 9], [11, 3]]
    res = benchmark(fisher_exact, table, alternative=None)
    expected_res = [0.0013797280926100372, 0.9999663480952982, 0.0027594561852200745]
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_01_ss(benchmark):
    table = [[1, 9], [11, 3]]
    _, res = benchmark(ss.fisher_exact, table, alternative='two-sided')
    expected_res = 0.0027594561852200745
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_02_our(benchmark):
    table = [[63, 5096], [128, 7425]]
    res = benchmark(fisher_exact, table, alternative=None)
    expected_res = [0.01788879597426398, 0.9878331093345797, 0.03140600873064571]
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_02_ss(benchmark):
    table = [[63, 5096], [128, 7425]]
    _, res = benchmark(ss.fisher_exact, table, alternative='two-sided')
    expected_res = 0.03140600873064571
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_03_our(benchmark):
    table = [[630, 50960], [1280, 74205]]
    res = benchmark(fisher_exact, table, alternative=None)
    expected_res = [2.9052048070478867e-12, 1.0, 5.518639232629043e-12]
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_03_ss(benchmark):
    table = [[630, 50960], [1280, 74205]]
    _, res = benchmark(ss.fisher_exact, table, alternative='two-sided')
    expected_res = 5.518639232629043e-12
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)