fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}


fn factorial(n: u8) -> u32 {
    match n {
        0 => 1,
        1 => 1,
        n => factorial(n - 1) * n as u32,
    }
}

fn main() {
    let input: u8 = read_line();
    let res = factorial(input);
    println!("{}", res);
}
