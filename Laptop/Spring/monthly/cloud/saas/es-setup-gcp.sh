#!bin/sh

# change: as where you want to install
cd /home/anuryadav

sudo apt-get install wget

mkdir elastic
cd elastic
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.8.0-linux-x86_64.tar.gz
tar -xvf elasticsearch-7.8.0-linux-x86_64.tar.gz

sleep 10

cd elasticsearch-7.8.0
sed -i 's/#node.name: node-1/node.name: es-aiops-node/g' ./config/elasticsearch.yml
sed -i 's/#cluster.name: my-application/cluster.name: es-aiops-cluster/g' ./config/elasticsearch.yml

nohup ./bin/elasticsearch > es_logs.log &

sleep 5

echo 'checking if cluster is up!'
curl http://localhost:9200

# Agent

cd /home/anuryadav
mkdir -p /home/anuryadav/aiops
cd aiops

# es-host-jmx
#wget --content-disposition 'https://apmgw.dxi-na1.saas.broadcom.com/acc/apm/acc/downloadpackage/57265?format=archive&layout=bootstrap_preferred&packageDownloadSecurityToken=19e6539965d8a4b0aee479c93f90d8900f09063b08ac3b0fcaf68c22f52afd5ax1017'

#  node name is simple -node
#wget --content-disposition 'https://apmgw.dxi-na1.saas.broadcom.com/acc/apm/acc/downloadpackage/57272?format=archive&layout=bootstrap_preferred&packageDownloadSecurityToken=11e644503fc493316ad86a026c0a7086c6d94a0813a47a98aed24f1cc2e1cc47x1017'

# es and Host and simple node name
wget --content-disposition 'https://apmgw.dxi-na1.saas.broadcom.com/acc/apm/acc/downloadpackage/57285?format=archive&layout=bootstrap_preferred&packageDownloadSecurityToken=d1ce3a1149ad671dbefa4be518e556ac62a131b5141838f4f4655734397cf2bbx1017'

tar -xvf *.tar

# start APMIA
sudo /home/anuryadav/aiops/apmia/APMIACtrl.sh install


# it worked fully in v6 instance