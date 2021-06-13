from fabric2 import Connection
def funcionInstalar():
	connect_kwargs = {"key_filename":['servidor-deploy.pub']}
	print("Realizo la conexion a la maquina de despliegue para las instalaciones")
	c = Connection(host='34.72.129.249',user="jeann",connect_kwargs=connect_kwargs)
	print("Instalo jenkins")
	result=c.run("sudo apt-get update")
	result=c.run("sudo apt-get install openjdk-8-jdk --yes")
	result=c.run("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -")
	result=c.run("sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
	result=c.run("sudo apt-get update")
	result=c.run("sudo apt-get install jenkins --yes")
	print("Instalo nodejs")
	result=c.run("sudo apt update")
	result=c.run("curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -")
	result=c.run("sudo apt -y install nodejs")
	result=c.run("sudo npm install -g npm@latest")
	result=c.run("node -v")
	print("Instalo Angular")
	result=c.run("sudo npm install -g @angular/cli")
	result=c.run("ng --version")
	print("Instalo Docker")
	result=c.run("sudo apt update")
	result=c.run("sudo apt install apt-transport-https ca-certificates curl software-properties-common --yes")
	result=c.run("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
	result=c.run("sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable\"")
	result=c.run("sudo apt update")
	result=c.run("sudo apt-cache policy docker-ce")
	result=c.run("sudo apt install docker-ce --yes")	
	result=c.run("docker --version")
	print("Instalo Docker-compose")
	result=c.run("sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
	result=c.run("sudo chmod +x /usr/local/bin/docker-compose")
	result=c.run("docker-compose --version")
	
def funcionFront():
	connect_kwargs = {"key_filename":['servidor-deploy.pub']}
	print("Realizo la conexion a la maquina de despliegue para el back")
	c = Connection(host='34.72.129.249',user="jeann",connect_kwargs=connect_kwargs)
	print("Muevo la carpeta del back y la levanto")
	
def funcionBack():
	connect_kwargs = {"key_filename":['servidor-deploy.pub']}
	print("Realizo la conexion a la maquina de despliegue para el front")
	c = Connection(host='34.72.129.249',user="jeann",connect_kwargs=connect_kwargs)
	print("Muevo la carpeta del front y la levanto")