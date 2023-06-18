use std::io;
use rand::Rng;

fn main() {
    let mut guess = String::new();

    io::stdin()
    .read_line(&mut guess)
    .expect("Unable to take input");

    let secret_number = rand::thread_rng().gen_range(1..=100);
    
}
