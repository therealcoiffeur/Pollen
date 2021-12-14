# Start the custom SSH server.
python3 pollen_ssh_server.py 2>log/debug &

# Start the custom HTTP server.
python3 pollen_http_server.py 2>log/debug &

# Start the custom HTTP server.
python3 pollen_https_server.py 2>log/debug &

# Start multiplexer on all port from 20 to 65000.
for i in $(cat common-ports.txt)
do
	sslh --listen=0.0.0.0:$i --ssh=127.0.0.1:65422 --http=127.0.0.1:65480 --tls=127.0.0.1:65443
done

# Loop to keep the container running.
while [ 1 ]
do
	sleep 100
done
