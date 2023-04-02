mod repl;
mod compiler;
mod executor;

use std::env::args;
use std::process::exit;

fn main() {
    pyo3::prepare_freethreaded_python();
    let mut args: Vec<_> = args().rev().collect();
    args.pop();
    let cmd = match args.pop() {
        Some(cmd) => cmd,
        _ => print_help_and_exit(),
    };
    let file = match args.pop() {
        Some(file) => file,
        _ => print_help_and_exit(),
    };
    match cmd.as_str() {
        "repl" => repl::run_repl(&file),
        "compile" => compiler::run_compiler(&file, &match args.pop() {
            Some(outfile) => outfile,
            _ => print_help_and_exit(),
        }),
        _ => print_help_and_exit()
    }
}

fn print_help_and_exit() -> ! {
    println!(r#" Gcode Plotter
    repl <file>              - run interactive mode
    compile <file> <outfile> - run compiler
    "#);
    exit(0);
}


