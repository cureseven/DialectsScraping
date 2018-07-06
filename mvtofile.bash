for textfile in $( ls . | grep .txt$ | grep gunma); do
  mv "${textfile}" "./gunma/${textfile}"
done
