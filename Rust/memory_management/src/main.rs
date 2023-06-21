mod str_modules;

fn main() {
    let name = String::from("Rohith");
    greet(&name);
    str_modules::print_n_times(&name,5);


}

fn greet(s: &String) {
    println!("hello {}",s);
    
}