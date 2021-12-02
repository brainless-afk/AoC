use aoc2021::read_file::{read_input, parse_as_num};

fn main() {
    let content = read_input("01");
    let lines = parse_as_num(content);

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
