%define import_path     github.com/coreos/go-systemd
%define gopath          %_datadir/gocode
%define commit          f743bc15d6bddd23662280b4ad20f7c874cdd5ad
%define shortcommit     f743bc1

#%%define shortcommit     %%(c=%%commit; echo ${c:0:7})

Name: golang-github-coreos-go-systemd
Version: 2
Release: alt1.git%shortcommit
Summary: Go bindings to systemd socket activation, journal and D-BUS APIs
License: Apache-2.0
Group: Development/Other
Url: http://%import_path

BuildArch: noarch

# git clone https://%import_path.git
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64 %arm

%description
%summary

%package devel
Requires: golang
Summary: Go bindings to systemd socket activation, journal and D-BUS APIs
Group: Development/Other
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/activation) = %version-%release
Provides: golang(%import_path/dbus) = %version-%release
Provides: golang(%import_path/journal) = %version-%release

%description devel
%summary

This package contains library source intended for building other
packages which use coreos/go-systemd.

%prep
%setup

%install
install -d -p %buildroot/%gopath/src/%import_path/{activation,dbus,journal}
cp -av {activation,dbus,journal} %buildroot/%gopath/src/%import_path

%files devel
%doc LICENSE README.md
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/github.com
%dir %attr(755,root,root) %gopath/src/github.com/coreos
%dir %attr(755,root,root) %gopath/src/%import_path
%dir %attr(755,root,root) %gopath/src/%import_path/activation
%dir %attr(755,root,root) %gopath/src/%import_path/dbus
%dir %attr(755,root,root) %gopath/src/%import_path/journal
%gopath/src/%import_path/activation/*.go
%gopath/src/%import_path/dbus/*.go
%gopath/src/%import_path/journal/*.go

%changelog
* Wed Jun 11 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2-alt1.gitf743bc1
- New version.

* Tue Apr 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1-alt1.git1d8116f
- Initial build.
