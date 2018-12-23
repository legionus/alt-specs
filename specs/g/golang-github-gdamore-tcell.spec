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
%global project         gdamore
%global repo            tcell
# https://github.com/gdamore/tcell
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          061d51a604c546b48e92253cb65190d76cecf4c6
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20171124

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.0
Release:        alt1_1
Summary:        An alternate terminal package
License:        Apache-2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}


%global _description \
Package tcell provides a cell based view for text terminals, like xterm. It was \
inspired by termbox, but differs from termbox in some important ways. It also \
adds substantial functionality beyond termbox.
Source44: import.info
%description 

%if 0%{?with_devel}
%{_description}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/gdamore/encoding)
BuildRequires: golang(github.com/lucasb-eyer/go-colorful)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/encoding/japanese)
BuildRequires: golang(golang.org/x/text/encoding/korean)
BuildRequires: golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires: golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires: golang(golang.org/x/text/transform)
%endif

Requires:      golang(github.com/gdamore/encoding)
Requires:      golang(github.com/lucasb-eyer/go-colorful)
Requires:      golang(github.com/mattn/go-runewidth)
Requires:      golang(golang.org/x/text/encoding)
Requires:      golang(golang.org/x/text/encoding/charmap)
Requires:      golang(golang.org/x/text/encoding/japanese)
Requires:      golang(golang.org/x/text/encoding/korean)
Requires:      golang(golang.org/x/text/encoding/simplifiedchinese)
Requires:      golang(golang.org/x/text/encoding/traditionalchinese)
Requires:      golang(golang.org/x/text/transform)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/encoding) = %{version}-%{release}
Provides:      golang(%{import_path}/termbox) = %{version}-%{release}
Provides:      golang(%{import_path}/views) = %{version}-%{release}

%description devel
%{_description}

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
%{_description}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{version}

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}/
ln -s $(pwd) src/%{provider}.%{provider_tld}/%{project}/%{repo}
export GOPATH=$(pwd):%{go_path}

for f in boxes mouse unicode; do
    %gobuild -o bin/${f} _demos/${f}.go
done

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

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE
%doc AUTHORS README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc --no-dereference LICENSE
%doc AUTHORS README.md
%endif

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.20170807gitd55f61c
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.20170807gitd55f61c
- new version

