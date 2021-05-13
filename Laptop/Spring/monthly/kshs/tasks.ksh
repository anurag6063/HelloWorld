cd /u001/web/service_cloud/comments/2016
file=CaseComments-From2016Jan1st-To-Dec201731-File9-Of-10796132.xml




dest=/u001/web/service_cloud/by_number/nine
cp $file $dest/$file

cd $dest

mkdir -p files
mkdir -p folders


xmllint --format $file >./folders/formatted.xml

echo 'completed formatting'

cd $dest/folders

csplit formatted.xml --prefix='comment' --suffix-format='%09d.xml' --elide-empty-files /'<records xsi:type="sObject">'/ '{*}'
echo 'completed splitting'

rm -rf formatted.xml
echo 'completed removal'

sleep 30

echo 'starting to pul files in respective folder'

start=$(date)
echo $start
count=0
for i in comment*.xml; do
        #< $i xml2json > $i.json && curl -X POST http://34.73.47.238:9200/test_docker/doc/ -d @"$i.json" -H "Content-Type:application/json" &
        echo $i': getting processed'
        caseNoLine=$(grep -E "<CaseNumber>[0-9]{8}</CaseNumber>" $i)
        caseNo=$(grep -oE "[0-9]*" <<<"$caseNoLine")
        echo 'case no is: ' $caseNo
        mkdir -p ./$caseNo
        mv $i ./$caseNo
        $count=$count+1
        echo 'processed: ' $count

done

echo 'completed movieng files to respective folder'
echo $(date) - $start
