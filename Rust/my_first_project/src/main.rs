


fn main() {
    let x: u32 = "24".parse().expect("Not a number!");
    {
        let x = x*2;
        println!("{x}");
    }
    println!("{x}");

    
}
