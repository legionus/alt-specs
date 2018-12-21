Name: 	  zsh-completions
Version:  0.30.0
Release:  alt1

Summary:  Additional completion definitions for Zsh
License:  BSD
Group:    Shells
Url: 	  https://github.com/zsh-users/zsh-completions

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Requires: zsh

BuildArch: noarch

%description
This projects aims at gathering/developing new completion scripts that are not
available in Zsh yet.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/zsh/site-functions
cp src/_* %buildroot%_datadir/zsh/site-functions/

%add_findreq_skiplist %_datadir/zsh/site-functions/_setup.py

%files
%doc README*
%_datadir/zsh/site-functions/*

%changelog
* Thu Dec 20 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.30.0-alt1
- new version 0.30.0

* Mon Oct 09 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.26.0-alt0.1.f13a8d.1
- Update to f13a8d commit (0.26.0 is last version)

* Sun Jul 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.25.0-alt1
- Initial build for Sisyphus
