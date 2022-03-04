i=1;
while [[ $i -le 10  ]];do
echo $i
    ((i++));
done;
luo=(a b c  )
echo ${luo[1]}
echo ${luo[@]}
