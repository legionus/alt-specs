%global import_path     github.com/syndtr/gocapability

%global commit db04d3cc01c8b54962a58ec7e491717d06cfcc16
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-syndtr-gocapability
Version: 0
Release: alt4.git%abbrev
Summary: Package capability provides utilities for manipulating POSIX capabilities.
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Package capability provides utilities for manipulating POSIX capabilities.

%package devel
Summary: Package capability provides utilities for manipulating POSIX capabilities.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/capability) = %version-%release

%description devel
Package capability provides utilities for manipulating POSIX capabilities.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%go_path/src/%import_path/capability/enumgen

%files devel
%doc LICENSE
%go_path/src/*

%changelog
* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 0-alt4.gitdb04d3cc
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gite7cb7fa3
- Ambient capabilities support

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt2.git2c00daeb
- Initial package for development only

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0-alt1.git20140517
- New snapshot

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT
