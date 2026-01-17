use std::collections::BTreeSet;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'minimumAbsoluteDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

fn minimumAbsoluteDifference(arr: &[i32]) -> i32 {
    let mut seen = BTreeSet::new();
    let mut min_diff = i32::MAX;

    for &num in arr {
        if seen.contains(&num) {
            return 0;
        }

        if let Some(&lower) = seen.range(..=num).max() {
            min_diff = min_diff.min(num - lower);
        }

        if let Some(&higher) = seen.range(num..).min() {
            min_diff = min_diff.min(higher - num);
        }

        seen.insert(num);
    }

    min_diff
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

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

    let result = minimumAbsoluteDifference(&arr);

    writeln!(&mut fptr, "{}", result).ok();
}
