use std::io;
use std::str::FromStr;

fn main() {
    let mut data = String::new();
    io::stdin().read_line(&mut data).unwrap();

    match u32::from_str(&data.trim()).unwrap() {
        n if n % 2 == 1 => println!("Weird"),
        n if n >= 2 && n <= 5 => println!("Not Weird"),
        n if n >= 6 && n <= 20 => println!("Weird"),
        n if n > 20 => println!("Not Weird"),
        n => panic!("Imposible! {}", n),
    }
}
