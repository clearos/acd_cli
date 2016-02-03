%global commit 75c5aa4b273d0227497e0daf4da29268bf118ba4
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:    acd_cli
Version: 0.3.1
Release: 2%{?dist}
Summary: A command line interface and FUSE filesystem for Amazon Cloud Drive 

License: GPLv2+
URL:     https://github.com/yadayada/acd_cli
Source0: https://github.com/yadayada/acd_cli/archive/%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel

# in order from https://acd-cli.readthedocs.org/en/latest/setup.html#python-packages
Requires:   python3-appdirs
Requires:   python3-colorama
Recommends: python3-dateutils
Requires:   python3-requests > 2.1.0
Recommends: python3-requests-toolbelt
Requires:   python3-sqlalchemy

%description
acd_cli provides a command line interface to Amazon Cloud Drive and allows
mounting your cloud drive using FUSE for read and write access. It is
currently in beta stage.

%prep
%setup -q

%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# default installs acd_cli, acdcli, and acd_cli.py -- docs only refer
# to the first two.
rm $RPM_BUILD_ROOT/%_bindir/{acd_cli,acdcli}
mv $RPM_BUILD_ROOT/%_bindir/acd_cli.py $RPM_BUILD_ROOT/%_bindir/acd_cli
ln -s acd_cli $RPM_BUILD_ROOT/%_bindir/acdcli

%files
%doc README.rst CONTRIBUTING.rst
%license LICENSE
%{python3_sitelib}/acdcli/
%{python3_sitelib}/acdcli-*egg-info/
%_bindir/acdcli
%_bindir/acd_cli

%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.1-1
- initial RPM

