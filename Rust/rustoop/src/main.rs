use std::env;


#[derive(Debug)]
struct Student {
    fname: String,
    lname: String
}

impl Student {
    fn from(s: &str) -> Self {
        let mut fname = String::new();
        let mut lname = String::new();
        let mut got_space = false;
        for i in s.trim().chars(){
            if i == ' '{
                got_space = true;
            }
            if !got_space {
                fname = fname + &String::from(i);
            }
            else {
                lname = lname + &String::from(i);
            }
        }
        Self {
            fname,
            lname: String::from(lname.trim())
        }
    }

    fn display(&self) {
        println!("First Name: Rohith\nLast Name: Kumar");
    }

    fn greet(&self){
        println!("Hello {} {}! How are you?",self.fname,self.lname);
    }

}

fn getcmdargs(s: &mut String) {
    let cmdargs = env::args();
    for i in cmdargs{
        *s = *s + &i;
    }
}

fn main() {
    let rohith = Student::from("Rohith Kumar");
    let mut cmdarg: String = String::new();
    getcmdargs(&mut cmdarg);
    rohith.greet();
    rohith.display();
}
