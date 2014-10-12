I really don't like to work on Windoze, but unfortunatly the latest and greatest C compiler for PIC18 is only available there.

tools which work for me on windoze:

*) Core FTP mini-server v1.23 
download from coreftp.com

*) SmartGit 2.0.5 
download from www.syntevo.com

Workflow:

I do have have a git repo on Linux, edit the files as much as I can there and check them into my local repo. SmartGit is able to git clone ssh://... from my Linux box and this is how I get the changes over to Windoze.

Some files are changed on Windoze (like e.g. config file for MPLAB project). Those I get via sftp to Linux and update the repo there (with permission problems and other incompatibilites...)

*) Get changed form local Linux git repo to Windoze:
pull (Merge fetched remote changes, Update registeres Submodles, And initialize new Submodules)

----------

Anyhow you can just place the project in Windoze under c:/projects/microchip and it should be an "out of the box experience for you".

Have fun and let me know if you are facing problems.

robert.berger@reliableembeddedsystems.com

