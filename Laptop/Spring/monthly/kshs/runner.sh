#/bin/sh


echo 'starting runner'

origin=/u002/ORACLE/service_cloud/2015/original

for i in {1..2}
do

	nohup sh -x tasks_v2.ksh 'CaseComments-Till2015Dec31-File$i-Of-3936804.xml' $origin '/u002/ORACLE/service_cloud/2015/$i' > $i.log &

	echo $! 'is the PID for: CaseComments-Till2015Dec31-File$i-Of-3936804.xml'  

done 

echo 'completed'
