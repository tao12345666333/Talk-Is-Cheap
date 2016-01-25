# Set the base image to Ubuntu
FROM        ubuntu

# Install
RUN         apt-get update && apt-get install -y redis-server

# Expose Redis port 6379
EXPOSE      6379

# Run Server
ENTRYPOINT  ["/usr/bin/redis-server"]
