use pyo3::prelude::*;
use pyo3::types::{PyDict};
use serde_json::Value;

#[allow(unsafe_op_in_unsafe_fn)]
#[pyfunction]
fn parse_json(py: Python<'_>, input: &str) -> PyResult<Py<PyDict>> {
    let value: serde_json::Value = serde_json::from_str(input)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;
    
    let dict = value_to_pydict(py, &value)?;
    Ok(dict)
}

fn value_to_pydict<'py>(py: Python<'py>, value: &serde_json::Value) -> PyResult<Py<PyDict>> {
    // Safety: safe because we’re under the GIL via `py`
    let dict =  PyDict::new(py);

    if let serde_json::Value::Object(map) = value {
        for (k, v) in map {
                    match v {
                    serde_json::Value::String(s) => { dict.set_item(k, s)?; }
                    serde_json::Value::Number(num) => {
                        if let Some(i) = num.as_i64() {
                            dict.set_item(k, i)?;
                        } else if let Some(f) = num.as_f64() {
                            dict.set_item(k, f)?;
                        }
                    }
                    serde_json::Value::Bool(b) => { dict.set_item(k, b)?; }
                    serde_json::Value::Null => { dict.set_item(k, py.None())?; }
                    serde_json::Value::Object(_) | serde_json::Value::Array(_) => {
                        dict.set_item(k, value_to_pydict(py, v)?)?;
                    }
            }
        }
    }

    Ok(dict.into())
}

/// Module definition
#[pymodule]
fn rust_utilities(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_json, m)?)?;
    Ok(())
}