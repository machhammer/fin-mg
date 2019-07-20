#Slave
sudo su
adduser jenkins-slave-03
sudo su - jenkins-slave-03
ssh-keygen -t rsa -N "" -f /home/jenkins-slave-03/.ssh/id_rsa
cd .ssh
cat id_rsa.pub > authorized_keys
chmod 700 authorized_keys

cd..
mkdir workspace

exit
exit

sudo su ubuntu
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install default-jdk

#DOCKER
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
sudo apt-get update
sudo apt-get install docker-ce
apt-cache madison docker-ce

sudo usermod -aG docker jenkins-slave-03



#Master

sudo mkdir -p /var/lib/jenkins/.ssh
cd /var/lib/jenkins/.ssh
sudo su 
ssh-keyscan -H 172.31.42.121 >> /var/lib/jenkins/.ssh/known_hosts
chown ubuntu:ubuntu known_hosts
chmod 777 known_hosts



#Stock Docker

docker stop $(docker ps -aq)
docker rmi $(docker images -q)