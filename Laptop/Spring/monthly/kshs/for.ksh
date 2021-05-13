#!/usr/bin/ksh
loc=/u001/web/service_cloud/comments/zebra/files
cd $loc
for f in *; do
echo 'reading: ' $f
   if [ -d ${f} ]; then

        # Will not run if no directories are available

        echo $f
	cd $loc/$f
#f=00013503
#	cc=$($f'_CaseComments.xml')
#	echo 'ls' $(ls)
	#cat * > joined.xml
	file=$f'_CaseComments.join'
(echo -e '<?xml version="1.0" encoding="UTF-8" standalone="no"?> \n <RelatedContent_Fields name="CaseComments">' && cat *.xml &&  echo '</RelatedContent_Fields>') > $f'_CaseComments.join'
#	(echo -e '<?xml version="1.0" encoding="UTF-8" standalone="no"?> \n <RelatedContent_Fields name="CaseComments">' && cat *.xml ) > $f'_CaseComments.xml' 
#	 cat $f'_CaseComments.xml' && echo '</RelatedContent_Fields>' > $f'_CaseComments.xml'

#	echo "" cat * > $f'_CaseComments.xml'
#	cat * > $f'_CaseComments.xml'
	#sed -i '1s+^+<?xml version="1.0" encoding="UTF-8" standalone="no"?><RelatedContent_Fields name="CaseComments">+' $f'_CaseComments.xml'
	
	sed -i 's+<records xsi:type="sObject">+  <RelatedContent>+g' $file
 	sed -i 's+</records>+    </RelatedContent>+g' $file
	sed -i 's+<CommentBody>+<casecomments_COMMENTBODY Name="Comment Body">+g' $file
	sed -i 's+</CommentBody>+</casecomments_COMMENTBODY>+g' $file
	sed -i 's+<IsPublished>+<casecomments_ISPUBLISHED Name="IsPublished">+g' $file
	sed -i 's+</IsPublished>+</casecomments_ISPUBLISHED>+g' $file
	sed -i 's+xsi:type="sObject"++g' $file
	sed -i 's+xsi:nil="true"++g' $file
	



#		for file in *;
#		do
#			echo 'files are: ' $file
#		done
    else 
	
	echo 'not found'
   fi
done
