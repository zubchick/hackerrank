// Enter your code here
use std::io::{self};
use std::str::FromStr;


fn main() {
    let mut input = String::new();

    //cost
    io::stdin().read_line(&mut input).unwrap();
    let cost = f64::from_str(&input.trim()).unwrap();

    // tips
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let tips = f64::from_str(&input.trim()).unwrap();

    // tax
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let tax = f64::from_str(&input.trim()).unwrap();

    println!("The total meal cost is {} dollars.", (
        cost + cost * (tips / 100.) + cost * (tax / 100.)
    ).floor())
}
