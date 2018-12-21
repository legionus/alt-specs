
%define oname node_exporter
%global import_path github.com/prometheus/node_exporter
%global commit 575d8950d367987ab8792e90fb2cf00c3fee1c10

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: prometheus-%oname
Version: 0.16.0
Release: alt0.rc3%ubt
Summary: Prometheus exporter for hardware and OS metrics exposed by *NIX kernels.

Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: glibc-devel-static
BuildRequires: promu
BuildRequires: /proc

Requires(pre): prometheus-common

%description
There is varying support for collectors on each operating system.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
promu build

%install
#export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
#%golang_install
#rm -rf -- %buildroot%_datadir
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/sysconfig}

install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md docs/* example.rules example-rules.yml text_collector_examples
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Tue May 08 2018 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt0.rc3%ubt
- Initial build for ALT.
