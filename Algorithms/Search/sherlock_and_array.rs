use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'balancedSums' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

fn balancedSums(arr: &[i32]) -> String {
    let total: i32 = arr.iter().sum();
    let mut left_sum = 0;

    for &num in arr {
        if left_sum == total - left_sum - num {
            return "YES".to_string();
        }

        left_sum += num;
    }

    "NO".to_string()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let T = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    for _ in 0..T {
        let n = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i32>()
            .unwrap();

        let arr: Vec<i32> = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();

        let result = balancedSums(&arr);

        writeln!(&mut fptr, "{}", result).ok();
    }
}
