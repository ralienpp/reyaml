reyaml
======

A humane YAML parser that tolerates comments, inline comments, whitespace; and catches some basic syntax errors for you.

The primary objective is to load configuration files. It is handy to leave comments inside the config file itself, to make administration tasks easier.

Examples of use
---------------

There are two functions you need: `load` parses a string, while `load_from_file` takes a file path instead. They return a dictionary.

```
import reyaml

raw_config = """
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
"""

config = reyaml.load(raw_config)
print config
>>> {'log': {'level': 'debug', 'format': '%(asctime)-15s %(levelname)s %(filename)s %(funcName)s %(message)s'}}

# you can also load it from a file directly
# config = reyaml.load_from_file('system.conf')
```


Example configuration
---------------------

Here is a YAML file that `reyaml` can absorb without a hitch:

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
	host: localhost # doesn't work with 127.0.0.1!!
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



Rationale
---------

Human errors can be roughly categorized as such:

* _Slip_ - your intention is right, but your action is wrong; e.g. accidentally press another button.
* _Mistake_ - your thought process was incorrect in the first place; e.g. you think that you can rename a file by selecting it and then pressing `Shift+Del` - the outcome is not what you wanted, even though the execution was flawless and you pressed exactly what you wanted.


YAML simplifies life by reducing the possibility of making slips in a configuration file. Below is an excerpt of a RabbitMQ configuration, it uses a different notation. You can see that it is easy to forget a bracket or miss a closing quote. As a result, you have to invest a lot of mental effort into counting symbols, when those problems could have easily been resolved by switching to YAML and leveraging indentation to express structure.


```
...
[
 {rabbit,
  [
   %% To listen on a specific interface, provide a tuple of {IpAddress, Port}.
   %% For example, to listen only on localhost for both IPv4 and IPv6:
   %% 
   {tcp_listeners, [{"127.0.0.1", 5672},
                    {"::1",       5672}]},
...
```

`Reyaml` takes that one step further and augments YAML by adding some additional features, here are a few:

- `host: localhost # doesn't work with 127.0.0.1!!` - inline comment
- tab indentation
- catch mixed tabs and spaces
- tell you about `#` when it is not clear whether this is a comment or an anchor, e.g. `https://docs.python.org/2/library/logging.html#logrecord-attributes`
- fail by making explicit remarks about what happened, instead of silently dropping `#logrecord-attributes` in the string above and moving on.