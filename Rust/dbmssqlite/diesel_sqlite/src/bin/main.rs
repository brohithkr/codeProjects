use diesel::prelude::*;
use diesel_sqlite::models::*;
use diesel_sqlite::{schema, connect};

fn main() {
    use schema::users::dsl::*;
    let conn: &mut SqliteConnection = &mut connect();
    let res = users
    .filter(name.eq("2345".to_string())).select(User::as_select()).load(conn).unwrap();
    let v = [0; 12];
    println!("{:?}, {:?}",res, v);

}