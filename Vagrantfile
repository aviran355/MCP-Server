Vagrant.configure("2") do |config|

    # MCP Server
    config.vm.define "mcp_server" do |mcp|
      mcp.vm.box = "ubuntu/bionic64"
      mcp.vm.network "private_network", ip: "192.168.56.5"
      mcp.vm.hostname = "mcp-server"
      mcp.vm.provision "shell", inline: <<-SHELL
        apt update && apt install -y python3 python3-pip
      SHELL
    end
  
    # Model 1
    config.vm.define "model1" do |model1|
      model1.vm.box = "ubuntu/bionic64"
      model1.vm.network "private_network", ip: "192.168.56.10"
      model1.vm.hostname = "model1"
      model1.vm.provision "shell", inline: <<-SHELL
        apt update && apt install -y python3 python3-pip
      SHELL
    end
  
    # Model 2
    config.vm.define "model2" do |model2|
      model2.vm.box = "ubuntu/bionic64"
      model2.vm.network "private_network", ip: "192.168.56.11"
      model2.vm.hostname = "model2"
      model2.vm.provision "shell", inline: <<-SHELL
        apt update && apt install -y python3 python3-pip
      SHELL
    end
  end
  