from fisher_exact import fisher_exact
import numpy.testing as npt

DECIMAL = 10

def test_fisher_exact_01():
    table = [[1, 9], [11, 3]]
    res = fisher_exact(table, alternative=None)
    expected_res = [0.0013797280926100372, 0.9999663480952982, 0.0027594561852200745]
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_01b():
    table = [[1, 9], [11, 3]]
    res = fisher_exact(table, alternative='less')
    expected_res = 0.0013797280926100372
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_01b():
    table = [[1, 9], [11, 3]]
    res = fisher_exact(table, alternative='greater')
    expected_res = 0.9999663480952982
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)

def test_fisher_exact_01b():
    table = [[1, 9], [11, 3]]
    res = fisher_exact(table, alternative='two-sided')
    expected_res = 0.0027594561852200745
    npt.assert_almost_equal(res, expected_res, decimal=DECIMAL)
