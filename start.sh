# Create an option for docker cli that contains all ports to listen on.
ports=""
for i in $(cat src/common-ports.txt)
do
    port="-p $i:$i"
    ports="${ports} ${port}"
done

# Run the docker sharing ports most common HTTP ports and sharing guest's /app/log directory with host's ./log directory.
docker run $ports -v $(pwd)/log:/app/log -d -it -t pollen
