%global import_path     gopkg.in/macaroon-bakery.v2-unstable

#global commit 7f1609ff1f3fcf3519ed62ccaaa9e609ea287838
#global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-macaroon-bakery-v2-unstable
Version: 2.0.1
Release: alt1
Summary: This package holds higher level operations for building systems with macaroons.
License: LGPL v.3
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository is a companion to http://github.com/go-macaroon .
It holds higher level operations for building systems with macaroons.

%package devel
Summary: This package holds higher level operations for building systems with macaroons.
Group: Development/Other
Requires: golang
Requires: golang(github.com/juju/webbrowser)
Requires: golang(github.com/julienschmidt/httprouter)
Requires: golang(github.com/rogpeppe/fastuuid)
Requires: golang(gopkg.in/httprequest.v1)
Requires: golang(gopkg.in/macaroon.v2)
Requires: golang(github.com/juju/httprequest)
Requires: golang(github.com/juju/loggo)
BuildRequires: golang(github.com/juju/webbrowser)
BuildRequires: golang(github.com/julienschmidt/httprouter)
BuildRequires: golang(github.com/rogpeppe/fastuuid)
BuildRequires: golang(gopkg.in/httprequest.v1)
BuildRequires: golang(gopkg.in/macaroon.v2)
Provides: golang(%import_path) = %version-%release

%description devel
This repository is a companion to http://github.com/go-macaroon .
It holds higher level operations for building systems with macaroons.

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
%doc README.md LICENSE
%go_path/src/*

%changelog
* Wed Jul 25 2018 Lenar Shakirov <snejok@altlinux.ru> 2.0.1-alt1
- Initial build

