cd qgb
rm *.pyc
git add -A
git commit -m %1%
git push qpsu master

cd ..
rm *.pyc
git add -A
git commit -m %1%
git push pm master