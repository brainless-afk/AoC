use std::fs::File;
use std::io::{BufRead, BufReader};

fn read_file() -> Vec<String> {
    let file_in = File::open("inputs/day01").unwrap();
    let reader = BufReader::new(file_in);
    return reader.lines().map(|line| line.unwrap()).collect();
}

fn parse_input(content: Vec<String>) -> Vec<u16> {
    return content.iter().map(|x| x.parse::<u16>().unwrap()).collect();
}

fn main() {
    let content = read_file();
    let lines = parse_input(content);

    let result_part1 = part1(&lines);
    println!("Part 1: {}", result_part1);

    let mut window_lines: Vec<u16> = Vec::new();
    for i in 0..lines.len()-2 {
        let window: u16 = lines[i..i + 3].iter().sum();
        window_lines.push(window);
    }

    let result_part2 = part1(&window_lines);
    println!("Part 2: {}", result_part2);
}

fn part1(lines: &Vec<u16>) -> u16 {
    let mut counter = 0;
    for i in 0..lines.len() - 1 {
        if lines[i + 1] > lines[i] {
            counter += 1;
        }
    }
    return counter;
}
