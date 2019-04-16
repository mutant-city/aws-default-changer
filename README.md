# aws-default-changer
Change the default aws account/region
By running change-default.py you can input the region and account you want as your system wide AWS default. 
It works by creating symlinks for config/credentials.

Notes: 
  * Backup your config and credentials files
  * This must be put into the .aws folder
  * Has only been tested with python3.7
  * Add this to your path for 
