url=$1
commit=$2
echo ${url}
if [ ! -d ".git" ]; then
# echo 11
  git init
  git remote add origin ${url}
fi
git pull origin master
git add -A
git commit -m "$commit"
git push origin master 
