#![allow(dead_code)]
// #![allow(unused_imports)]


// use crate::garden::backyard::asp;

mod garden;

// mod garden {
//     pub mod backyard {
//         pub fn asparagus() {
//             println!("This is asparagus.");
//         }
//     }
// }


fn main() {
    let mut v: Vec<i32> = vec![1,2,3,4,5];
    println!("{:?}",v);
    v.push(7);
    for mut i in v {
        println!("{}",i);
    }
    println!("{:?}",v);

    
}
