# envcrypt - Symmetrical encryption of environment variables & data.
[link to github repo](https://github.com/snowfox-dev/envcrypt.git)

## Usage:

import statement:
> import envcrypt.envcrypt as env

Generate key:
> env.generate_key()
> Store this key in environment variable 'CS1'



Load password env:
> env.load_pass()
> Password must be stored in environment variable 'CS2' to work.


Load key env:
> env.load_key()
> Key must be stored in enviroment variable 'CS1' to work.

Encrypt string or data:
> env.encrypt_message(x)


Decrypt string or data from encrypt_message method:
> env.decrypt_message(x)
