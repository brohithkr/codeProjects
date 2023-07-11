use std::io;
mod str_modules;

fn main() {
    let mut s = String::new();

    io::stdin()
    .read_line(&mut s)
    .expect("Error taking input");

    println!("{}",str_modules::is_palindrome(&s));

}

fn greet(s: &String) {
    println!("hello {}",s);
    
}