
file=$1

source=$2
dest=$3



mkdir -p $dest
cd $source


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
       
		echo $i': getting processed'
        caseNoLine=$(grep -E "<CaseNumber>[0-9]{8}</CaseNumber>" $i)
        caseNo=$(grep -oE "[0-9]*" <<<"$caseNoLine")
        echo 'case no is: ' $caseNo
        mkdir -p ./$caseNo
        mv $i ./$caseNo
#        count=(($count+1))
 #       echo 'processed: ' $count

	count=$(($count+1))
	echo $count

done

echo 'completed movieng files to respective folder'
echo $(date) - $start

wait
echo 'all done'
