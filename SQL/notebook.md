
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
Foreign keys are used to create relationships between tables. They refer to the primary key in other tables.


## Unique
The `UNIQUE` constraint ensures that all vallues in a column are different.

```SQL
ALTER TABLE Customers ADD UNIQUE (lastname);
```
But, you can have multiple NULL values in a unique column.


## Join
A better way of combining data is the JOIN clause. It allows you to combine multiple tables based on a condition.

```SQL
SELECT Customers.firstname, Customers.lastname, Customers.city, PhoneNumbers.number, PhoneNumbers.type
FROM Customers JOIN PhoneNumbers
ON Customers.id = PhoneNumbers.customer_id
```
Because you use the full column names when joining tables, the query can get really long. To make it easier and shorter, we can provide nicknames for our tables:
```SQL
SELECT C.firstname, C.lastname, C.city, PN.number, PN.type
FROM Customers AS C JOIN PhoneNumber AS PN
ON C.id = PN.customer_id
```

Another type of JOIN is the **LEFT JOIN**.
The LEFT JOIN returns all rows from the left table(first table), even if there are no matches in the right table(seconde table).
This means that if there are no matches for the ON clause in the table on the right, the jion will still return thr rows from the first table in the result.

![image](https://github.com/boluocat/learning/assets/44392038/2cc62413-f306-4046-a0ce-cffcba7a22e3)

```SQL
SELECT C.fristname, C.lastname, C.city, PN.number, PN.type
FROM Customers AS C LEFT JOIN PhoneNumbers AS PN
ON C.id = PN.customer_id
```

Similarly, the **RIGHT JOIN** returns all the rows from the right tables, even if there are no matches in the left table.
```SQL
SELECT C.fristname, C.lastname, C.city, PN.numberm PN.type
FROM PhoneNumbers AS PN RIGHT JOIN Customers AS C
ON C.id = PN.customer_d
ORDER BY C.id
```

# UNION
The **UNION** operator is used to combine the result-sets of two or more SELECT statements.
```SQL
SELECT firstname, lastname, age FROM Customers
UNION
SELECT firstname, lastname, age FROM Contacts
```
All `SELECT` statements within the **UNION** must have the same number of columns. The columns must also have the same data types. Also, the columns in each `SELECT` statement must be i the same order.


**UNION ALL** is similar to **UNION**, but does not remove the duplicates.

Remember, the `SELECT` statements need to have the same columns for the **UNION** to work. In case one of the tables has extra columns that we need to select, we can simply add them to the second select as **NULL**:
```SQL
SELECT firstname, lastname, age, city FROM Customers
UNION
SELECT firstname, lastname, age, NULL FROM Contacts
```
