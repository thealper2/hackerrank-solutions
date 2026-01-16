use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'missingNumbers' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY arr
 *  2. INTEGER_ARRAY brr
 */

fn missingNumbers(arr: &[i32], brr: &[i32]) -> Vec<i32> {
    let mut count_arr: HashMap<i32, i32> = HashMap::new();
    for &num in arr {
        *count_arr.entry(num).or_insert(0) += 1;
    }

    let mut count_brr: HashMap<i32, i32> = HashMap::new();
    for &num in brr {
        *count_brr.entry(num).or_insert(0) += 1;
    }

    let mut missing = Vec::new();

    let mut keys: Vec<i32> = count_brr.keys().cloned().collect();
    keys.sort();

    for num in keys {
        let brr_count = count_brr[&num];
        let arr_count = *count_arr.get(&num).unwrap_or(&0);

        if brr_count > arr_count {
            missing.push(num);
        }
    }

    missing
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

    let m = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    let brr: Vec<i32> = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = missingNumbers(&arr, &brr);

    for i in 0..result.len() {
        write!(&mut fptr, "{}", result[i]).ok();

        if i != result.len() - 1 {
            write!(&mut fptr, " ").ok();
        }
    }

    writeln!(&mut fptr).ok();
}
