#!/usr/bin/ksh

start=$(date)
echo $start
for i in *.xml
do
        #< $i xml2json > $i.json && curl -X POST http://34.73.47.238:9200/test_docker/doc/ -d @"$i.json" -H "Content-Type:application/json" &
	echo $i': getting processed'
	caseNoLine=$(grep -E "<CaseNumber>[0-9]{8}</CaseNumber>"  $i)
	caseNo=$(grep -oE "[0-9]*" <<< "$caseNoLine")
#	caseNo=$(grep -E "[0-9]{8}>"  $caseNo)
	echo 'case no is: ' $caseNo 
	mkdir -p ./$caseNo
	mv $i ./$caseNo
done

echo $(date) - $start