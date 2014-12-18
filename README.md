reyaml
======

A parser of humane YAML files, that tolerates comments, inline comments, whitespace; as well as catches some basic syntax errors for you.

The primary objective of this library is to use it for loading configuration files of a software system. It is handy to leave comments inside the config file itself, to make administration tasks easier.


Here is an example of a YAML file that `reyaml` can absorb without a hitch:

```
# This is the main configuration file of the system, it is written in a
# relaxed flavour of YAML that gives you more freedom and makes the file
# more readable.

# As you have already noticed, a line that begins with '#' is a comment,
# it is ignored.

	#A comment can begin anywhere on the line, it is still ignored

# Empty lines are ignored as well.

# Strings don't have to be quoted, example:
#	test: the wise fox
#	url: http://myaddress.com

# However, sometimes you need quotes, for example if the string is a URL with 
# an anchor, the '#' sign will be treated as a comment, unless quoted.
#			trickyUrl: http://address.com/path#anchor  #WRONG
#			trickyUrl: "http://address.com/path#anchor"  #CORRECT, double-quote
#			trickyUrl: 'http://address.com/path#anchor'  #CORRECT, single-quote

# As you can see above, you can quote strings with double- and single-quotes,
# they are both valid.

# Lines can be indented with spaces or tabs, but you cannot mix them. An error
# will be shown if you do that.

# The configuration loader is designed to fail and make a lot of noise if something
# is wrong with the syntax. You will see an error and a chunk of the problematic
# line.
##############################################################################



# database settings go here; these will be used to connect to PostgreSQL
db:
	host: localhost
	port: 60000
	db: ts_db
	user: jedi
	password: noAuthNeeded

# stuff related to the LDAP server
ldap:
	host: 192.135.1.7
	port: 389
	password: Cxronomat0peaea
	timeout: 3 # in seconds

	# the values below don't have to be quoted, but it gives one
	# psychological comfort when they have no doubts about how a
	# setting is interpreted, so there you go
	user: "cn=admin,o=Dekart"


# RabbitMQ connection settings
amqp:
	url: amqp://guest:guest@127.0.0.1



log:
	# valid options: {debug, info, warning, error, critical}
	# if not specified, no logging takes place
	level: debug

	# full path to log file. If not specified, logging to STDOUT
	#path: taxisomatic.log 

	# this must be a valid Python log format string, reference:
	# https://docs.python.org/2/library/logging.html#logrecord-attributes 
	# If not specified, the default is `'%(asctime)-15s %(levelname)s %(message)s'`
	#format: "%(asctime)-15s %(levelname)s %(message)s"
	format: "%(asctime)-15s %(levelname)s %(filename)s %(funcName)s %(message)s"
```
