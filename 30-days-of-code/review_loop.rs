fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}

fn main() {
    let n: u32 = read_line();

    for _ in 0..n {
        let line: String = read_line();
        let mut even = String::new();
        let mut odd = String::new();

        for (i, chr) in line.chars().enumerate() {
            if i % 2 == 0 {
                even.push(chr);
            } else {
                odd.push(chr);
            }
        }
        println!("{} {}", even, odd);
    }
}
