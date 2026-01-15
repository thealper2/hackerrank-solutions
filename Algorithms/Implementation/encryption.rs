use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

fn encryption(s: &str) -> String {
    let no_space: String = s.chars().filter(|c| !c.is_whitespace()).collect();
    let n = no_space.len();

    let sqrt_n = (n as f64).sqrt();
    let mut rows = sqrt_n.floor() as usize;
    let mut cols = sqrt_n.ceil() as usize;

    if rows * cols < n {
        rows += 1;
    }

    let mut result = Vec::new();

    for c in 0..cols {
        let mut column_text = String::new();

        for r in 0..rows {
            let idx = r * cols + c;
            if idx < n {
                column_text.push(no_space.chars().nth(idx).unwrap());
            }
        }

        result.push(column_text);
    }

    result.join(" ")
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let s = stdin_iterator.next().unwrap().unwrap();

    let result = encryption(&s);

    writeln!(&mut fptr, "{}", result).ok();
}
