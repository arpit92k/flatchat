API endpoints :
login/		: login a user
logout/ 	: logout a user
signup/		: register a user
user/<id>	: list details of any user or list and update details of current user
user/		: list all users

REST access :
http -p username:password POST http://host:port/user/
http -p username:password POST http://host:port/user/<id>/
http -p username:password POST http://host:port/login/

Browser access :
http://host:port/signup -- will display signup form
http://host:port/login  -- will display login form
http://host:port/user  -- will display alist of all users
http://host:port/user/<id>/ -- will display details of user with given id and allow to edit details of authenticated user
http://host:port/logout/    -- logout user

to access in json responce from browser
http://host:port/user/?format=json
http://host:port/user/<id>/?format=json