awk '{if(min==""){min=max=$1}; if($1>max){max=$1}; if($1<min){min=$1}; total+=$1; count+=1} END {print "avg="total/count ",max="max ",min="min}'
