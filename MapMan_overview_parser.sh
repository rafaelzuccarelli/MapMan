cd input
for f in *xls; do ssconvert -O "separator='	' format=preserve quoting-mode=always" $f $f.txt;done
for f in *.txt; do mv "$f" "$(echo "$f" | sed s/\.xls\.txt//)"; done
#mkdir xls
#mv *xls xls
#ssconvert -O "quoting-mode=always" --import-type=Gnumeric_stf:stf_csvtab --merge-to=all.xls *_*
#mv *xls xls
#mkdir txt
#mv *_* txt
#cd ..
#python3 MapMan_overview_parser.py
#cd output
#for f in *.csv; do mv "$f" "$(echo "$f" | sed s/_features_added.csv//)"; done
#ssconvert --import-type=Gnumeric_stf:stf_csvtab --merge-to=all_features_added.xls *_*
#mv all_features_added.xls .all_features_added.xls
#rm *_*
#mv .all_features_added.xls all_features_added.xls
#cd ..
#cd input
#mv xls ..
#mv txt ..
#cd ..
#mv xls output
#mv txt output
