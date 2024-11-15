#!/bin/bash

Directory ="D://ImportantFiles" 
Username = "user"
Server = "remote_server"
Remote_directory = "D://Backup" 

rsync -avz  "$Directory" "$Username"@"$Server":"$Remote_directory"
