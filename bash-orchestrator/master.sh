#!/bin/bash

# TODO take these as args to script
image=app
replicas=3
base_hostport=8081
hostname=localhost

# For DEV reasons
# stops all running containers
stopAllContainers() {
    container_ids=($(docker ps -a -q))
    for c_id in ${container_ids[*]}; do
        echo "stopping.. $c_id"
        docker stop $c_id
    done
}

# IN: (container_port, image)
startNewContainer() {
    docker run --rm -it -p $1:5000 -d $2
}

# boot all replicas
boot() {
    # spin up containers for given image
    for i in $(seq 1 $replicas); do
        local container_port=$(( base_hostport + i ))
        echo "docker run --rm -it -p $container_port:5000 -d $image"
        (startNewContainer $container_port $image)
    done
}

#IN: (container_port)
isContainerDown() {
    health_status_code=$(curl -s -o /dev/null -w '%{http_code}' $hostname:$1/health)
    echo "$(( health_status_code - 200 ))"
}

monitor() {
    while true
    do
        sleep 5
        for i in $(seq 1 $replicas); do
            local container_port=$(( base_hostport + i ))
            health=$(isContainerDown $container_port)
            if [[ "$health" -eq "0" ]]; then
                echo "$hostname:$container_port OK!"
            else
                echo "$hostname:$container_port down. starting new container.."
                (startNewContainer $container_port $image)
            fi
        done
    done        
}

stopAllContainers
# (boot)
(monitor)
