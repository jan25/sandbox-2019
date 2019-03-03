Vagrant.configure("2") do |config|

  config.vm.define "sandbox" do |sandbox|
    sandbox.vm.box = "bento/ubuntu-18.04"
    sandbox.vm.hostname = "sandbox-host"
    sandbox.vm.network "private_network", ip: "10.0.0.11"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = "2"
  end

end
