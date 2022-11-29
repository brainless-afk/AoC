use aoc2022::read_file::{parse_nums, read_file};

fn main() {
    let content = read_input("01");
    let lines = parse_as_num(content);

    let result_part1 = part1(&lines);
    println!("Part 1: {}", result_part1);
}

fn part1(lines: &Vec<u16>) -> u16 {

    let mut counter = 0;
    for i in 0..lines.len() - 1 {
        if lines[i + 1] > lines[i] {
            counter += 1;
        }
    }
    
    return 0;
}
