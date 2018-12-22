Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
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
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         go-ini
%global repo            ini
# https://github.com/go-ini/ini
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          3d73f4b845efdf9989fffd4b4e562727744a34ba
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global v1_import_path     gopkg.in/v1/ini
%global v1_import_path_sec gopkg.in/ini.v1

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.21.1
Release:        alt1_0.5.git%{shortcommit}
Summary:        Package ini provides INI file read and write functionality in Go
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
License:        Apache-2.0
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

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{v1_import_path}) = %{version}-%{release}
Provides:      golang(%{v1_import_path_sec}) = %{version}-%{release}

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

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
%endif

Requires:      golang(github.com/smartystreets/goconvey/convey)

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
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/
echo "%%dir %%{go_path}/src/%%{v1_import_path}/." >> devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/
echo "%%dir %%{go_path}/src/%%{v1_import_path_sec}/." >> devel.file-list

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    echo "%%dir %%{go_path}/src/%%{v1_import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path}/$file
    echo "%%{go_path}/src/%%{v1_import_path}/$file" >> devel.file-list

    echo "%%dir %%{go_path}/src/%%{v1_import_path_sec}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$file
    echo "%%{go_path}/src/%%{v1_import_path_sec}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
cp -r testdata %{buildroot}/%{go_path}/src/%{import_path}/.
echo "%%{go_path}/src/%%{import_path}/testdata" >> unit-test-devel.file-list
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

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README_ZH.md README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/%{v1_import_path}
%dir %{go_path}/src/%{v1_import_path_sec}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc README_ZH.md README.md
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.21.1-alt1_0.5.git3d73f4b
- new version

