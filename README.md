# DockerCleaner
 - removes docker ownerless <none> images

### Additional data
 - Docker compose file is ready to work, it starts 2 containers with pyserver and pyclient made on socket lib. The localhost network is used. Client sends message each 5 sec during one minute, then shutdowns, server countinues to be upped.
 - Logs after each script lunch are saved in docker_cleaner.log
