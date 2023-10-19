pub mod models;
pub mod schema;

use diesel::prelude::*;
use dotenvy::dotenv;
use std::env;

use models::User;

pub fn connect() -> SqliteConnection {
    dotenv().ok();
    let db_url = env::var("DATABASE_URL").expect("Please set a database url.");
    SqliteConnection::establish(&db_url).unwrap()
}

pub fn add_user(conn: &mut SqliteConnection, uid: &String, name: &String ) {
    let user = User {uid: uid.to_string(), name: name.to_string()};
    diesel::insert_into(schema::users::table)
    .values(user)
    .execute(conn).unwrap();
}