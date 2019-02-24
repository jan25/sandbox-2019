# Copied from [https://gist.github.com/ryu22e/462976ca1c74c61c9f18]
# Installs and sets up docker and docker-compose

sudo apt-get update
sudo apt-get install -y software-properties-common curl
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get purge lxc-docker
sudo apt-cache policy docker-engine
sudo apt-get install -y linux-image-extra-$(uname -r) 
sudo apt-get install -y docker-engine
sudo echo 'DOCKER_OPTS="-H tcp://127.0.0.1:4243 -H unix:///var/run/docker.sock"' >> /etc/default/docker
sudo service docker restart
sudo usermod -aG docker vagrant
echo 'export DOCKER_HOST=tcp://localhost:4243' >> /home/vagrant/.bashrc
curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` -o docker-compose
sudo chmod +x docker-compose
sudo mv docker-compose /usr/local/bin

# docker run --rm -it -p 8080:5000 -d app