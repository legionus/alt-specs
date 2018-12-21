Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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
%global project         sasha-s
%global repo            go-deadlock
# https://github.com/sasha-s/go-deadlock
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          03d40e5dbd5488667a13b3c2600b2f7c2886f02f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20171130

# commit 03d40e5dbd5488667a13b3c2600b2f7c2886f02f == version 0.2.0


Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.2.0
Release:        alt1_2
Summary:        Online deadlock detection in go
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{project}-%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package        devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/petermattis/goid)
%endif

Requires:       golang(github.com/petermattis/goid)

Provides:       golang(%{import_path}) = %{version}-%{release}

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%package        unit-test-devel
Group: Development/Other
Summary:        Unit tests for %{name} package

# test subpackage tests code from devel subpackage

%description    unit-test-devel
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
export GOPATH=%{buildroot}/%{go_path}:%{go_path}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE
%doc Readme.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc --no-dereference LICENSE
%doc Readme.md
%endif


%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_1.20171130.git03d40e5
- new version

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_0.5.git565eb44
- new version

