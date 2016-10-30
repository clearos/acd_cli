git clone git+ssh://git@github.com/clearos/acd_cli.git
cd acd_cli/
git checkout f23
git remote add upstream git://pkgs.fedoraproject.org/acd_cli.git
git pull upstream f23
git checkout clear7
git merge --no-commit f23
