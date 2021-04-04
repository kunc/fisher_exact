use pyo3::prelude::{pymodule, PyModule, PyResult, Python};
use std::f64;
use fishers_exact::fishers_exact;

#[pymodule]
fn fisher_exact(_py: Python<'_>, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "_fisher_exact")]
    fn fisher_exact_py<'py>(
        _py: Python<'py>,
        n11: u32, n12: u32, n21: u32, n22: u32
    ) -> Vec<f64> {
        let p = fishers_exact(&[n11, n12, n21, n22]).unwrap();
        let res: Vec<f64> = vec![p.less_pvalue, p.greater_pvalue, p.two_tail_pvalue];
        res
    }

    Ok(())
}


#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;
    #[macro_use]
    use approx::assert_abs_diff_eq;

    // taken from https://github.com/cpearce/fishers_exact
    #[test]
    fn test_fisher_exact_01() {
        let p = fishers_exact(&[1, 9, 11, 3]).unwrap();
        let epsilon = 0.000001;
        assert_abs_diff_eq!(p.less_pvalue, 0.001379728, epsilon = epsilon); // modified based on scipy.stats.fisher_exact result
        assert_abs_diff_eq!(p.greater_pvalue, 0.9999663, epsilon = epsilon);
        assert_abs_diff_eq!(p.two_tail_pvalue, 0.0027594, epsilon = epsilon);
    }


}