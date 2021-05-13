#!/bin/bash


start=$(date)

loc=$1
formed=$2
cd $loc
for f in *;


	echo 'inside clubbing file function'

	
echo 'reading: ' $f
  #  if [ -d ${f} ]; then

        # Will not run if no directories are available

        echo $f
	cd $loc/$f

	file=$f'_CaseComments.join'
(echo -e '<?xml version="1.0" encoding="UTF-8" standalone="no"?> \n <RelatedContent_Fields name="CaseComments">' && cat *.xml &&  echo '</RelatedContent_Fields>') > $f'_CaseComments.join'
	sed -i 's+<records xsi:type="sObject">+  <RelatedContent>+g' $file
 	sed -i 's+</records>+    </RelatedContent>+g' $file
	sed -i 's+<CommentBody>+<casecomments_COMMENTBODY Name="Comment Body">+g' $file
	sed -i 's+</CommentBody>+</casecomments_COMMENTBODY>+g' $file
	sed -i 's+<IsPublished>+<casecomments_ISPUBLISHED Name="IsPublished">+g' $file
	sed -i 's+</IsPublished>+</casecomments_ISPUBLISHED>+g' $file
	sed -i 's+xsi:type="sObject"++g' $file
	sed -i 's+xsi:nil="true"++g' $file
	
	cp $file $formed

wait
echo 'all done'

echo $(date) - $start