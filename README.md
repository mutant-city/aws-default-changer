# aws-profile-manger
* Change the default aws profile account/region 
* It works by creating symlinks for config/credentials.

### To use
1. Add your cred-files to the cred-files folder and your config files to the config-files folder
2. Run change-default.py

Notes: 
  * Backup your original config and credentials files!
  * This must be put into the .aws folder
  * Has only been tested with python3.7(but theoretically should work with 3+ python)
  * Add this to path/make an alias for system-wide usage!
  * only works on Linux/MacOS
