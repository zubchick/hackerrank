fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}


fn main() {
    let _: u32 = read_line();
    let line: String = read_line();

    let res: Vec<_> = line.split_whitespace()
        .rev()
        .collect();
    println!("{}", res.join(" "));
}
