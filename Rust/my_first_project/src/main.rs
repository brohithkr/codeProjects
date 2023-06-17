fn main() {
    let mut fname = String::new();
    let mut lname = String::new();
    std::io::stdin().read_line(&mut fname).expect("failed to read line");
    std::io::stdin().read_line(&mut lname).expect("failed to read line");
    println!("Hello {} {}",fname.trim_end(),lname.trim_end());
}
