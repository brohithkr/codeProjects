use std::io;

fn fibonacci(n: i32) {
    let mut prev = 1;
    let mut prevprev = 1;
    let mut k = 1;
    while k<n {
        if k==1{
            println!("1");
        }
        else if k==2{
            println!("1");
        }
        else {
            let num: usize = prev + prevprev;
            println!("{}",num);
            prevprev = prev;
            prev = num;
        }
        k+=1;
    }
    
}

fn main() {
    let mut i = String::new();

    io::stdin()
    .read_line(&mut i)
    .expect("Error");

    let i: i32 = i
    .trim()
    .parse()
    .expect("Not an integer.");

    fibonacci(i);

    // let a: [i32; 5 ] = [12,24,36,54,23];

 


}