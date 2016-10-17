fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}


fn max_hourglass(data: &[i8], size: usize) -> i64 {
    let ind = |i: usize, j: usize| { data[i * size + j] };

    // j, j - indexes of top left item of hourglass
    let mut max_sum: i64 = -100500;

    for i in 0..(size - 2) {
        for j in 0..(size - 2) {
            let mut count: i64 = 0;

            for &(k, n) in [(i, j), (i, j + 1), (i, j + 2),
                            (i + 1, j + 1),
                            (i + 2, j), (i + 2, j + 1), (i + 2, j + 2)
            ].iter() {
                count += ind(k, n) as i64
            }

            if count > max_sum {
                max_sum = count;
            }
        }
    }
    max_sum
}


fn main() {
    let firstline: String = read_line();
    let firstline = firstline.trim();
    let size = firstline.split_whitespace().collect::<Vec<_>>().len();

    let mut line = firstline.to_string();
    let mut matrix: Vec<i8> = Vec::with_capacity(size * size);
    for i in 0..size {
        for chr in line.split_whitespace() {
            matrix.push(chr.parse().unwrap())
        }
        if i < size - 1 {
            line = read_line();
        }
    }

    let max_hourglass_count = max_hourglass(&matrix, size);
    println!("{}", max_hourglass_count);
}
