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

E:
cd E:\SourceCode\shell
git add -A
git commit -m %1%
git push ws master
