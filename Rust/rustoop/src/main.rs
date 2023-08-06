// use std::env;
#![allow(dead_code)]


mod stu_module{
    #[derive(Debug)]
    pub struct Student {
        pub fname: String,
        lname: String
    }

    impl Student {
        pub fn from(s: &str) -> Self {
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

        pub fn display(&self) {
            println!("First Name: Rohith\nLast Name: Kumar");
        }

        pub fn greet(&self){
            println!("Hello {} {}! How are you?",self.fname,self.lname);
        }

    }
}

// fn getcmdargs(s: &mut String) {
//     let cmdargs = env::args();
//     for i in cmdargs{
//         *s = s + &i;
//     }
// }

use stu_module::Student;

fn main() {
    let mut rohith = Student::from("Rohith Kumar");
    // let mut cmdarg: String = String::new();
    // getcmdargs(&mut cmdarg);
    // rohith.greet();
    // rohith.display();
    rohith.fname = String::from("Roro");
    let mut stu_vec = vec![Student::from("rohith bandari"), rohith];
    println!("{:?}",stu_vec);
    stu_vec.push(Student::from("Jai Parmar"));
    println!("{:?}",stu_vec);

}
