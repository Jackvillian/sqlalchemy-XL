# sqlachemy-XL

A small tool that can on-the-fly "patch" SQL dialect of the [sqlalchemy](http://www.sqlalchemy.org/) project to enable creation of the correct database scheme that works in [postgres-XL](http://www.postgres-xl.org/) cluster.

## Usage


```
from sqlalchemy_xl.decorators import distribute_by_hash
from sqlalchemy_xl import generate_sql

...

Base = declarative_base()


@distribute_by_hash('id')
class Address(Base):
    __tablename__ = 'address'
...

print(generate_sql(Base.metadata))

```


## Examples

```
python examples/case1.py
```

the modified output will contain `DISTRIBUTE BY HASH` statement

```
CREATE TABLE person (
	id SERIAL NOT NULL, 
	name VARCHAR(250) NOT NULL, 
	PRIMARY KEY (id)
) DISTRIBUTE BY HASH(id);

CREATE TABLE address (
	id SERIAL NOT NULL, 
	street_name VARCHAR(250), 
	street_number VARCHAR(250), 
	post_code VARCHAR(250) NOT NULL, 
	person_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(person_id) REFERENCES person (id)
) DISTRIBUTE BY HASH(id);

```
