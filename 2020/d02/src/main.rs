use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("input").unwrap();
    let buf = BufReader::new(file);

    let mut counter1 = 0u64;
    let mut counter2 = 0u64;
    for line in buf.lines() {
        let line2 = line.unwrap();
        let l: Vec<&str> = line2.split(" ").collect();
        let vrange: Vec<usize> = l[0].split("-").filter_map(|x| x.parse().ok()).collect();
        let ch: char = l[1].chars().next().unwrap();
        let pw: &str = l[2];
        let len1 = pw.len();
        let len2 = pw.replace(&ch.to_string(), "").len();
        if len1-len2 >= vrange[0] && len1-len2 <= vrange[1] {
            counter1 += 1;
        }
        if pw.chars().nth(vrange[0]-1).unwrap().eq(&ch) != pw.chars().nth(vrange[1]-1).unwrap().eq(&ch) {
            counter2 += 1;
        }
    }
    println!("Part 1: {}", counter1);
    println!("Part 2: {}", counter2);
}

// blub
// ToDO