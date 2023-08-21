drop table if exists testimonial;
    create table testimonial (
        id integer primary key autoincrement,
        names text not null,
        comment text not null
    );