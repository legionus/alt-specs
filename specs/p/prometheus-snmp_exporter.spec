
%define oname snmp_exporter
%global import_path github.com/prometheus/snmp_exporter
%global commit 5c997da9e9ee79dc6c72641f02d204f4eafc14b3

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: prometheus-%oname
Version: 0.10.0
Release: alt2%ubt
Summary: Prometheus snmp exporter

Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: promu
BuildRequires: /proc
# for build generator
BuildRequires: libnet-snmp-devel snmp-mibs-std

Requires(pre): prometheus-common

%description
This is an exporter that exposes information gathered
from SNMP for use by the Prometheus monitoring system.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
promu build

cd .gopath/src/%import_path/generator
%gobuild

%install
#export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
#%golang_install
#rm -rf -- %buildroot%_datadir
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}

install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 snmp.yml %buildroot%_sysconfdir/prometheus/snmp.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service

# generator
install -m0755 .gopath/src/%import_path/generator/generator %buildroot%_bindir/%oname-generator

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md snmp.yml
%doc .gopath/src/%import_path/generator/generator.yml
%doc .gopath/src/%import_path/generator/FORMAT.md
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/snmp.yml

%changelog
* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt2%ubt
- fix typo in option

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1%ubt
- Initial build for ALT.
