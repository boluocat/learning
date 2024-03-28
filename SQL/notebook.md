
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

