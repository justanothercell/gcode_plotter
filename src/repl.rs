use notify_debouncer_mini::notify::{recommended_watcher, RecursiveMode, Watcher};
use processing::Screen;
use processing::shapes::line::Line;
use std::path::Path;
use std::sync::atomic::{AtomicBool, Ordering};
use crate::executor::execute_script;

static UPDATE_REQUIRED: AtomicBool = AtomicBool::new(true);

pub(crate) fn run_repl(file: &str) {
    let mut screen = Screen::new(800, 800, false, true, true).unwrap();

    let mut watcher = recommended_watcher(|event| {
        match event {
            Ok(_) => {
                UPDATE_REQUIRED.store(true, Ordering::Release)
            }
            Err(e) => eprintln!("error watching file: {e}"),
        }
    }).unwrap();
    watcher.watch(Path::new(file), RecursiveMode::NonRecursive).unwrap();

    loop {
        if UPDATE_REQUIRED.load(Ordering::Acquire) {
            UPDATE_REQUIRED.store(false, Ordering::Release);
            if let Some(((w, h), (ox, oy), (h_down, h_up), instructions)) = execute_script(file) {
                screen.background(0.0, 0.0, 0.0, 1.0);
                screen.stroke_weight(0.5);
                let mut x = 0.0;
                let mut y = 0.0;
                for instr in instructions {
                    screen.stroke(&[instr.3.0 as f32 / 255.0], &[instr.3.1 as f32 / 255.0], &[instr.3.2 as f32 / 255.0],
                                  &[if instr.2 { 1.0 } else { 0.1 }]);

                    let l1 = Line::new(&screen, &[(x / (w / 2.0) - 1.0) as f64], &[(y / (h / 2.0) - 1.0) as f64], &[0.0],
                                       &[(instr.0 / (w / 2.0) - 1.0) as f64], &[(instr.1 / (h / 2.0) - 1.0) as f64], &[0.0]).unwrap();
                    screen.draw(&l1).unwrap();

                    x = instr.0;
                    y = instr.1;
                }
            }
        }
        if screen.reveal().is_err() {
            break
        }
    }
}