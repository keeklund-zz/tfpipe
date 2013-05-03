[loggers]
keys=root,testing

[handlers]
keys=fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler
name=rootesting
propogate=0

[logger_testing]
level=DEBUG
handlers=fileHandler
qualname=testing
propogate=0

[handler_fileHandler]
class=FileHandler
formatter=simpleFormatter
args=("/tmp/tfpipe.log",)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s
datefmt=