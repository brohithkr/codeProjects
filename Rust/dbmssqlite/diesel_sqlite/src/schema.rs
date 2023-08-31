// @generated automatically by Diesel CLI.

diesel::table! {
    posts (id) {
        id -> Nullable<Double>,
        title -> Nullable<Text>,
        body -> Nullable<Text>,
    }
}

diesel::table! {
    users (uid) {
        uid -> Text,
        name -> Text,
    }
}

diesel::allow_tables_to_appear_in_same_query!(
    posts,
    users,
);
