pub fn print_n_times(s: &String, n: i32) {
    for _ in 0..n {
        println!("{s}");
    }
}

pub fn is_palindrome(s: &String) -> bool {
    let mut revstring = String::new();
    for i in s.trim().chars() {
        revstring = String::from(i) + &revstring;
    }
    println!("{} {}",s.trim(),&revstring);
    (*s.trim() == revstring)
}