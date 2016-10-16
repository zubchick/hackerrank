fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}


fn count_ones(n: u32) -> usize {
    let mut mask = 0x00_00_00_01u32;
    let mut count_max: usize = 0;
    let mut count = 0;

    for _ in 0..32 {
        let res = n & mask;
        if res == 0 {
            if count_max < count {
                count_max = count;
            };
            count = 0;
        } else {
            count += 1;
        }
        mask <<= 1;
    }

    if count_max < count {
        count_max = count;
    }

    count_max
}


fn main() {
    let n: u32 = read_line();
    let ones = count_ones(n);
    println!("{}", ones);
}
