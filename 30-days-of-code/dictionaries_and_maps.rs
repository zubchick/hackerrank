use std::collections::HashMap;

fn read_line<T: std::str::FromStr>() -> T {
   let mut  input = String::new();
   std::io::stdin().read_line(&mut input).expect("Could not read stdin!");
   match input.trim().parse() {
       Ok(v) => v,
       Err(_) => panic!("Could not parse input")
   }
}


fn main() {
    let count: u32 = read_line();

    let mut phonebook = HashMap::new();

    for _ in 0..count {
        let newline: String = read_line();
        let mut splitter = newline.split_whitespace();
        let name = splitter.next().unwrap().to_string();
        let phone = splitter.next().unwrap().to_string();

        phonebook.insert(name, phone);
    }

    loop {
        let query: String = read_line();
        if query == "" {
            break
        };

        match phonebook.get::<str>(&query) {
            Some(value) => println!("{}={}", query, value),
            None        => println!("Not found"),
        }
    }
}
