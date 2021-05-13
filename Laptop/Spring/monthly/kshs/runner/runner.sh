#/bin/sh


echo 'starting runner'

origin=/u001/web/service_cloud/comments/2018/original

for i in {1..3}
do

	nohup sh -x tasks.sh "CaseComments-From2018Jan1st-To-End-File$i-Of-7498128.xml" $origin "/u001/web/service_cloud/comments/2018/$i" > $i.log &

	echo $! "is the PID for: CaseComments-From2018Jan1st-To-End-File$i-Of-7498128.xml"

done 
wait

echo 'completed'
