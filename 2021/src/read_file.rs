use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn read_input(day: &str) -> Vec<String> {
    let input_path = format!("inputs/day{}", day);
    let file_in = File::open(input_path).unwrap();
    let reader = BufReader::new(file_in);
    return reader.lines().map(|line| line.unwrap()).collect();
}

pub fn parse_as_num(content: Vec<String>) -> Vec<u16> {
    return content.iter().map(|x| x.parse::<u16>().unwrap()).collect();
}