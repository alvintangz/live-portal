from subprocess import call
call(["apt-get", "update"])
call(["apt-get", "install", "unixodbc-dev"])