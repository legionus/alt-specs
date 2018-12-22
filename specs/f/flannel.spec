
%global import_path github.com/coreos/flannel 
%global commit 2fd6898a7c9a11a12e63b56ca01143a260ee0aad
#%%global shortcommit %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define _libexecdir /usr/libexec

Name: flannel
Version: 0.10.0
Release: alt1%ubt
Summary: flannel is a network fabric for containers
Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar
Source1: flanneld.sysconfig
Source2: flanneld.service
Source3: flannel-docker.conf
Source4: flannel-tmpfiles.conf

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: /proc

%description
Flannel is a simple and easy way to configure
a layer 3 network fabric designed for Kubernetes.

%prep
%setup -q

%build
gofmt -w -r "x -> \"%{version}\"" version/version.go
export BUILDDIR="$PWD"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

#%golang_prepare
mkdir -p src/github.com/coreos
ln -s ../../../ src/github.com/coreos/flannel

%golang_build "src/%import_path"

%install
install -D -p -m 755 bin/flannel %buildroot%_sbindir/flanneld
install -D -p -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/flanneld
install -D -p -m 644 %SOURCE2 %buildroot%_unitdir/flanneld.service
install -D -p -m 644 %SOURCE3 %buildroot%_unitdir/docker.service.d/flannel.conf
install -D -p -m 755 dist/mk-docker-opts.sh %buildroot%_libexecdir/flannel/mk-docker-opts.sh
install -D -p -m 0755 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

%files
%doc LICENSE README.md Documentation
%_sbindir/flanneld
%_unitdir/flanneld.service
%_unitdir/docker.service.d/flannel.conf
%dir %_libexecdir/flannel
%_libexecdir/flannel/mk-docker-opts.sh
%config(noreplace) %_sysconfdir/sysconfig/flanneld
%_tmpfilesdir/%name.conf

%changelog
* Sun May 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1%ubt
- Initial package
