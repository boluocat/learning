
# Indentity
Often, the id is an integer(a whole number) which is incremented with each new row. SQL allows you to create a column that gets automatically incremented with each new row. That is done using the `AUTO_INCREMENT` keyword.

```SQL
CREATE TABLE Customers (
  id int NOT NULL AUTO_INCREMENT,
  firstname varchar(255),
  lastname varchar(255)
)
```

Now when inserting a new row, we do not need to specify the value of the id column, as it will automatically be set.
```SQL
INSERT INTO Customers (firstname, lastname)
VALUES
('demo', 'huel'),
('jdil', 'uefg');
```

By default, the `AUTO_INCREMENT` column starts with the value 1. This can be changed if needed, using the following:
```SQL
ALTER TALE Customers
  AUTO_INCREMENT=555
```

# Key
Another important concept in database are keys. They are used to define relationship between tables.
## Primary Key
The primary key constaint is used to uniquely identify rows of a table.
```SQL
CREATE TABLE Customers (
  id int NOT NULL AUTO_INCREMENT,
  firstname varchar(255),
  lastname varvhar(255),
  PRIMARY KEY (id)
);
```
Here are some rules for primary keys:
1. A primary key must contain **unique** values.
2. A primary key column cannot have **NULL** values.
3. A table can have **only one** primary key.

## Foreign Key
A Foreign key is a column in one table that refers to the Primary Key in another table.
```SQL
CREATE TABLE PhoneNumbers (
  id int NOT NULL AUTO_INCREMENT,
  customer_id int NOT NULL,
  number varchar(55).
  type varchar(55),
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES Customers(id)
);
```
A table can have multiple foreign keys.

