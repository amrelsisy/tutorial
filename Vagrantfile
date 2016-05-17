Vagrant.configure("2") do |config|
	
	config.vm.define("test1") do |test1_config|
  		test1_config.vm.box = "puppetlabs/centos-6.6-64-nocm"
		test1_config.vm.network "private_network", ip:"172.25.0.2", netmask: "255.255.0.0"
		test1_config.vm.provision "shell", path: "script1.sh"
	end

	config.vm.define("test2") do |test2_config|
  		test2_config.vm.box = "puppetlabs/centos-6.6-64-nocm"
		test2_config.vm.network "private_network", ip:"172.25.0.3", netmask: "255.255.0.0"
		
		test2_config.vm.provision "shell", path: "script2.sh"
	end


end
