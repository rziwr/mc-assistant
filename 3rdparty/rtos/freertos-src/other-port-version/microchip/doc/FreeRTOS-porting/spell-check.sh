for FILE in *.tex; do
  if [ -e $FILE ]; then
  # do something with $FILE
  #echo "png File: $FILE"
  name=${FILE%\.*}
  echo ${name}
  ispell -t ${name}.tex
  fi
done

rm -f *.bak
