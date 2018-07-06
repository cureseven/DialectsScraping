for textfile in $( ls ./hokkaido | grep .txt$ ); do
# filename =
  echo "${textfile}"
  cd hokkaido
  rm "${textfile}"
done
