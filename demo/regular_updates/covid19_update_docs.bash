#!/bin/bash -l

update_date=$(date +"%d-%m-%Y")
repodir=REPODIR
#
## now update the README.rst, Sphinx, and push up
covid19_update_readme -d $repodir -j docs/covid19_topN_LATEST.json
#
cwd=$(pwd)
cd $repodir/docsrc
make deploy
cd $cwd
#
git -C $repodir pull
git -C $repodir stage README.rst docs docsrc
git -C $repodir commit -a -m "update README.rst and Sphinx at $update_date."
git -C $repodir push
