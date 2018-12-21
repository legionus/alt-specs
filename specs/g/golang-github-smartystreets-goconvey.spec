Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
# cyclic dependency between golang-github-smartystreets-goconvey and
# golang-github-smartystreets-assertions
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         smartystreets
%global repo            goconvey
# https://github.com/smartystreets/goconvey
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          bf58a9a1291224109919756b4dcc469c670cc7e4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.6.1
Release:        alt1_0.7.git%{shortcommit}
Summary:        Behavioral testing in the browser, integrates with go test
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
# cyclic dependency between golang-github-smartystreets-goconvey and
# golang-github-smartystreets-assertions
BuildRequires: golang(github.com/jtolds/gls)
BuildRequires: golang(github.com/smartystreets/assertions)
%endif

Requires:      golang(github.com/jtolds/gls)
Requires:      golang(github.com/smartystreets/assertions)

Provides:      golang(%{import_path}/convey) = %{version}-%{release}
Provides:      golang(%{import_path}/convey/gotest) = %{version}-%{release}
Provides:      golang(%{import_path}/convey/reporting) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/api) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/contract) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/executor) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/messaging) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/parser) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/system) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/watch) = %{version}-%{release}
Provides:      golang(%{import_path}/web/server/watch/integration_testing/sub) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description unit-test
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
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test.file-list.dir
    done
done
[ -s unit-test.file-list.dir ] && sort -u unit-test.file-list.dir >> unit-test.file-list
rm -f unit-test.file-list.dir
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

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/convey
%gotest %{import_path}/convey/reporting
%gotest %{import_path}/web/server/api
%gotest %{import_path}/web/server/executor
%gotest %{import_path}/web/server/parser
%gotest %{import_path}/web/server/system
%gotest %{import_path}/web/server/watch
%gotest %{import_path}/web/server/watch/integration_testing/sub
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE.md
%doc README.md CONTRIBUTING.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc --no-dereference LICENSE.md
%doc README.md CONTRIBUTING.md
%endif

%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_0.7.gitbf58a9a
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_0.6.gitbf58a9a
- new version

