Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global         debug_package   %{nil}

%global         provider        github
%global         provider_tld    com
%global         project         BurntSushi
%global         repo            xgb
# https://github.com/BurntSushi/xgb
%global         provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global         import_path     %{provider_prefix}
%global         commit          27f122750802c950b2c869a5b63dafcf590ced95
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.2.git%{shortcommit}
Summary:        XGB is the X protocol Go language Binding
License:        BSD
URL:            https://%{provider_prefix}
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}.

%package devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/bigreq) = %{version}-%{release}
Provides:       golang(%{import_path}/composite) = %{version}-%{release}
Provides:       golang(%{import_path}/damage) = %{version}-%{release}
Provides:       golang(%{import_path}/dpms) = %{version}-%{release}
Provides:       golang(%{import_path}/dri2) = %{version}-%{release}
Provides:       golang(%{import_path}/ge) = %{version}-%{release}
Provides:       golang(%{import_path}/glx) = %{version}-%{release}
Provides:       golang(%{import_path}/randr) = %{version}-%{release}
Provides:       golang(%{import_path}/record) = %{version}-%{release}
Provides:       golang(%{import_path}/render) = %{version}-%{release}
Provides:       golang(%{import_path}/res) = %{version}-%{release}
Provides:       golang(%{import_path}/screensaver) = %{version}-%{release}
Provides:       golang(%{import_path}/shape) = %{version}-%{release}
Provides:       golang(%{import_path}/shm) = %{version}-%{release}
Provides:       golang(%{import_path}/xcmisc) = %{version}-%{release}
Provides:       golang(%{import_path}/xevie) = %{version}-%{release}
Provides:       golang(%{import_path}/xf86dri) = %{version}-%{release}
Provides:       golang(%{import_path}/xf86vidmode) = %{version}-%{release}
Provides:       golang(%{import_path}/xfixes) = %{version}-%{release}
Provides:       golang(%{import_path}/xinerama) = %{version}-%{release}
Provides:       golang(%{import_path}/xprint) = %{version}-%{release}
Provides:       golang(%{import_path}/xproto) = %{version}-%{release}
Provides:       golang(%{import_path}/xselinux) = %{version}-%{release}
Provides:       golang(%{import_path}/xtest) = %{version}-%{release}
Provides:       golang(%{import_path}/xv) = %{version}-%{release}
Provides:       golang(%{import_path}/xvmc) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Group: Development/Other
Summary:        Unit tests for %{name} package
BuildArch:      noarch
# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.


%prep
%setup -q -n %{repo}-%{commit}
find -type f -exec chmod 644 {} ';'

%build

%install
# source codes for building projects
install -d -p %{buildroot}%{go_path}/src/%{import_path}/
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

# testing files for this project
install -d -p %{buildroot}%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done

sort -u -o devel.file-list devel.file-list

%check
export GOPATH=%{buildroot}%{go_path}:%{go_path}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

# we're in a chroot and do not have access to the display
#%%gotest %%{import_path}/xproto

%files devel -f devel.file-list
%doc README
%doc --no-dereference LICENSE
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}

%files unit-test-devel -f unit-test-devel.file-list

%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.git27f1227
- fc update

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.git27f1227
- new version

