Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        gopkg
%global provider_tld    in
%global project         go-macaroon
%global repo            macaroon
# https://github.com/go-macaroon/macaroon
%global import_path     gopkg.in/macaroon.v1
%global commit          d8fd13e6951f2ce46f0964a58149cf2f103cac9a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1
Release:        alt1_0.5.git%{shortcommit}
Summary:        A native Go implementation of macaroons
License:        BSD
URL:            https://gopkg.in/macaroon.v1
Source0:        https://github.com/go-macaroon/macaroon/archive/%{commit}.tar.gz#/macaroon-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info
BuildArch: noarch

%description
The macaroon package implements macaroons as described in the paper
"Macaroons: Cookies with Contextual Caveats for Decentralized
Authorization in the Cloud"

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires: golang(gopkg.in/check.v1)
%endif

Requires:      golang(golang.org/x/crypto/nacl/secretbox)
Requires:      golang(gopkg.in/check.v1)

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> devel.file-list.dir
    done
done
[ -s devel.file-list.dir ] && sort -u devel.file-list.dir >> devel.file-list
rm -f devel.file-list.dir
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test-devel.file-list.dir
    done
done
[ -s unit-test-devel.file-list.dir ] && sort -u unit-test-devel.file-list.dir >> unit-test-devel.file-list
rm -f unit-test-devel.file-list.dir
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
export GOPATH=%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}
%endif

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc --no-dereference LICENSE
%doc README.md

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE
%doc README.md
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc --no-dereference LICENSE
%doc README.md
%endif

%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 1-alt1_0.5.gitd8fd13e
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_0.4.gitd8fd13e
- new version

