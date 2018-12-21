%global import_path golang.org/x/crypto

%global commit 21052ae46654ecf18dfdba0f7c12701a1e2b3164
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-golang-x-crypto
Version: 0
Release: alt11.git%abbrev
Summary: Supplementary Go cryptography libraries
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Supplementary Go cryptography libraries

%package devel
Summary: Supplementary Go cryptography libraries
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

Requires: golang(golang.org/x/sys/unix)

%description devel
Supplementary Go cryptography libraries

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

%files devel
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 0-alt11.git21052ae4
-Update

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 0-alt10.git1875d0a7
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 0-alt9.git558b6879
- Update

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 0-alt8.git5ef0053f
- Update

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0-alt7.git728b753d
- Update
- Removed "Provides" for separate packages due updated automatic calculation

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 0-alt6.gitede567c8
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt5.git3c0d69f1
- Update

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 0-alt4.git8e06e8dd
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gitb35ccbc9
- Update

* Thu Apr 14 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.git1777f3ba
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.git1f22c010
- Initial package
