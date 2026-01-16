use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'happyLadybugs' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING b as parameter.
 */

fn happyLadybugs(b: &str) -> String {
    let mut count: HashMap<char, usize> = HashMap::new();
    for c in b.chars() {
        *count.entry(c).or_insert(0) += 1;
    }

    for (color, &freq) in count.iter() {
        if *color != '_' && freq == 1 {
            return "NO".to_string();
        }
    }

    if count.contains_key(&'_') {
        return "YES".to_string();
    }

    let chars: Vec<char> = b.chars().collect();
    let n = chars.len();

    for i in 0..n {
        let left_ok = i == 0 || chars[i] == chars[i - 1];
        let right_ok = i == n - 1 || chars[i] == chars[i + 1];

        if !left_ok && !right_ok {
            return "NO".to_string();
        }
    }

    "YES".to_string()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let g = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    for _ in 0..g {
        let n = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i32>()
            .unwrap();

        let b = stdin_iterator.next().unwrap().unwrap();

        let result = happyLadybugs(&b);

        writeln!(&mut fptr, "{}", result).ok();
    }
}
