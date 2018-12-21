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
%global project         ncw
%global repo            dropbox-sdk-go-unofficial
# https://github.com/ncw/dropbox-sdk-go-unofficial
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          5d9f46f9862ae5f65e264e178de6ce2c41a32d40
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20170530

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.2.%{commitdate}git%{shortcommit}
Summary:        An unofficial Go SDK for integrating with the Dropbox API v2
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
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

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/oauth2)
%endif

Requires:      golang(golang.org/x/oauth2)

Provides:      golang(%{import_path}/dropbox) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/async) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/auth) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/common) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/files) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/paper) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/properties) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/sharing) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/team) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/team_common) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/team_log) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/team_policies) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/users) = %{version}-%{release}
Provides:      golang(%{import_path}/dropbox/users_common) = %{version}-%{release}
Provides:      golang(%{import_path}/generator/go_rsrc) = %{version}-%{release}
Provides:      golang(%{import_path}/generator/go_rsrc/files) = %{version}-%{release}
Provides:      golang(%{import_path}/generator/go_rsrc/sharing) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
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
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.20170530git5d9f46f
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.20170530git5d9f46f
- new version

