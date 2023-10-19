use diesel::prelude::*;

#[derive(Debug)]
#[derive(Queryable, Selectable, Insertable)]
#[diesel(table_name = crate::schema::users)]
#[diesel(check_for_backend(diesel::sqlite::Sqlite))]
pub struct User {
    pub uid: String,
    pub name: String
}