# Learn To Ignore

We have a zip of a git repository, it contains a Python virtual environment which should have been in the .gitignore and a Flask Application returning JSON data (the flag) at /beauty.

The Flask Application loads the flag from the environment variable FLAG. This Environment Variable is loaded when the virtual environment is activated using source ./env/bin/activate . The purpose is to ease development and also store config and keys and the environment is usually not commited to the git repository. 

In the env/bin/activate script you will find the environment variable being exported as an env var (all encoded in base64). Decode the base64 to get the flag.

flag: evlz{always_ignore_the_unneccessary}ctf
