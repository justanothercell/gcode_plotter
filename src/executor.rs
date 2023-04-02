use std::fs::read_to_string;
use pyo3::prelude::PyModule;
use pyo3::Python;
use pyo3::types::PyDict;

#[allow(clippy::type_complexity)]
pub(crate) fn execute_script(file: &str) -> Option<((f32, f32), (f32, f32), (f32, f32), Vec<(f32, f32, bool, (i32, i32, i32))>)> {
    Python::with_gil(|py| {
        let paths = std::fs::read_dir("pylib").unwrap();

        for path in paths.flatten() {
            let filename = path.file_name().to_string_lossy().to_string();
            if filename.ends_with(".py") {
                PyModule::from_code(py, &read_to_string(&format!("pylib/{}", filename)).unwrap(), &filename, filename.split_at(filename.len()-3).0).unwrap();
            }
        }

        PyModule::from_code(py, include_str!("../pylib/plot_text.py"), "plot_text.py", "plot_text").unwrap();
        let globals = PyDict::new(py);
        let locals = PyDict::new(py);
        if let Err(e) = py.run(&read_to_string(file).expect("could not open file"), Some(globals), Some(locals)) {
            eprintln!("error executing print instructions:");
            e.print(py);
        }
        match locals.get_item("plotter").map(Some).unwrap_or_else(|| globals.get_item("plotter")) {
            None => eprintln!("no global plotter in instructions file"),
            Some(plotter) => {
                let w: f32 = plotter.getattr("width").unwrap().extract().unwrap();
                let h: f32 = plotter.getattr("height").unwrap().extract().unwrap();
                let ox: f32 = plotter.getattr("offset_x").unwrap().extract().unwrap();
                let oy: f32 = plotter.getattr("offset_y").unwrap().extract().unwrap();
                let h_down: f32 = plotter.getattr("h_down").unwrap().extract().unwrap();
                let h_up: f32 = plotter.getattr("h_up").unwrap().extract().unwrap();
                #[allow(clippy::type_complexity)] let instructions: Vec<(f32, f32, bool, (i32, i32, i32))> = plotter.getattr("instructions").unwrap().extract().unwrap();
                return Some(((w, h), (ox, oy), (h_down, h_up), instructions))
            }
        }
        None
    })
}