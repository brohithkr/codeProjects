use diesel_sqlite::*;

fn main() {
    let db_conn = &mut connect();
    add_user(db_conn, &"hello123".to_string(), &"2345".to_string());
    println!("Hello, world!");
}
