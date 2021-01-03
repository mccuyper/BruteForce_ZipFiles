# BruteForce_ZipFiles

BruteForce for Locked ZipFiles. 
You can use any dictionary, you can find in web or just create your own. (in case if you now part of password or smth).

Checking script: 
  1. Zip any file in archive using command: 
        # zip -P [put_your_password_here] archiveName.zip yourFile.ext
  2. Put this locked archive in the same directory with script, and run it:
        # python main.py
  3. Script will ask you for Dictionary you want to use(should be in the same directory)
  4. The second input is Name of Archive;
  5. Wait for a while.
  6. If your dictionary consists matching password, your archive will be exctracted in directory "Extracted".
