INSERT INTO user ('login', 'pid') VALUES ('emptyset', SELECT pid FROM person WHERE email = 'emptyset@gmail.com');
