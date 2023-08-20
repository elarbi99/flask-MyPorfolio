drop table if exists posts;
    create table posts (
        id integer primary key autoincrement,
        FirstName text not null,
        comment text not null

    );