use std::fs::File;
use std::io::Write;
use crate::executor::execute_script;

pub(crate) fn run_compiler(file: &str, outfile: &str) {
    if let Some(((_w, _h), (ox, oy), (h_down, h_up), instructions)) = execute_script(file) {
        let mut is_down = false;
        let mut code = vec![
            "; plotter code created by DragonFighter603's gcode plotter".to_string(),
            "M107 ; turn off extruder fan".to_string(),
            "M106 S0 ; turn off extruder fan again".to_string(),
            "G28 ; homing all axis".to_string(),
            format!("G0 Z{h_up} ; go to pen_up state"),
            "M25 P\"prepare pen [ok]\" S2".to_string(),
            // use the accurate movement in hopes that it'll help
            format!("G1 X{ox} Y{oy}; go to min positions"),
            format!("G1 Z{h_up} ; go to pen_up state again"),
            "".to_string()
        ];

        for (x, y, down, _) in instructions {
            if down != is_down {
                if down {
                    code.push(format!("G0 Z{h_down}"));
                } else {
                    code.push(format!("G0 Z{h_up}"));
                }
                is_down = down;
            }
            if down {
                code.push(format!("G1 X{} Y{}", x + ox, y + oy));
            } else {
                code.push(format!("G0 X{} Y{}", x + ox, y + oy));
            }
        }

        code.push("".to_string());
        // use the accurate movement in hopes that it'll help
        code.push(format!("G1 Z{h_up} ; go to pen_up state again"));
        code.push(format!("G1 X{ox} Y{oy} ; go to min positions"));

        File::create(outfile).expect("could not open outfile").write_all(code.join("\n").as_bytes()).unwrap();
    } else {
        println!("error executing instructions")
    }
}