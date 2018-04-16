drop table if exists pages;
create table pages (
  id integer primary key autoincrement,
  title text not null,
  type text not null,
  content text not null
);

create table flags (
  flag text not null
);