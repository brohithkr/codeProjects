fn ask_and_push(v: &mut Vec<i32>) -> bool {
    let stdin = std::io::stdin();
    println!("Please give a number to push.");
    let mut num = String::new();
    stdin.read_line(&mut num).expect("Unable to take input.");
    let num: i32 = match num.trim().parse() {
        Ok(n) => n,
        Err(_e) => {
            println!("Please provide a valid number.");
            return false;
        }
    };
    v.push(num);
    return true
}

fn pop_vec(v: &mut Vec<i32>) {
    let num = v.pop();
    match num {
        Some(n) => println!("The number {} as been popped from back.", n),
        None => println!("The vector is empty!"),
    }
}

fn get_a_num(v: &Vec<i32>) -> bool {
    let stdin = std::io::stdin();
    println!("Enter a position: ");
    let mut pos = String::new();
    stdin.read_line(&mut pos).expect("Unable to take input.");
    let pos: usize = match pos.trim().parse() {
        Ok(n) => n,
        Err(_e) => {
            println!("Please provide a number.");
            return false;
        } 
    };
    let num = (v).get(pos);
    match num {
        Some(n) => {
            println!("The number is {}", n);
            return true;
        }
        None => {
            println!("The given position is out of range!");
            return false;
        }
    }
}

fn main() {
    let stdin = std::io::stdin();
    let mut v: Vec<i32> = Vec::new();
    loop {
        println!("Choose among the following options:\n1. Push a number\n2. Pop a number\n3. Get a number\n4. Print the vector\n5. Exit");
        let mut opt = String::new();
        stdin.read_line(&mut opt).expect("Unable to take input.");
        let opt: i32 = match opt.trim().parse() {
            Ok(n) => n,
            Err(_e) => {
                println!("Please provide a valid number.");
                continue;
            }
        };
        if opt == 1 {
            while !ask_and_push(&mut v) {
                println!("Please try again.")
            }
        } else if opt == 2 {
            pop_vec(&mut v);
        } else if opt == 3 {
            while !get_a_num(&v) {
                println!("Please Try again.")
            }
        } else if opt == 4 {
            if v.is_empty() {
                println!("The vector is empty.");
            } else {
                println!("The vector currently contains: ");
                for i in &v {
                    print!("{i} ")
                }
                println!("");
            }
        } else if opt == 5 {
            break;
        } else {
            println!("Please select an option among following options only!\nIf you want to exit type 5.")
        }
        println!("Press enter key to continue...");
        let mut opt = String::new();
        stdin.read_line(&mut opt).expect("Unable to take input.");
    }
}
