Summary: OpenNode Textual User Interface RPM
Name: opennode-tui
Version: 2.0.1
Release: alt6.git.6af352f
License: Apache-2.0
Group: System/Configuration/Other
Url: http://github.com/opennode/opennode-tui
Source0: %name-%version.tar
BuildArch: noarch

Packager: Valentin Rosavitskiy <valintinr@altlinux.org>

BuildRequires: python-module-distribute

Requires: libvirt-client libvirt-daemon screen
# qemu qemu-kvm vzctl

%description
This package contains the OpenNode Textual User Interface for the OpenNode cloud toolkit.

%package -n python-module-opennode
Summary: Common modules for opennode
Group: Development/Python

%description -n python-module-opennode
Common modules for opennode

%prep
%setup

#fix for /bin/env in on-dump-csv.py
sed -i 's/\/bin\/env/\/usr\/bin\/env/' scripts/on-dump-csv.py

%build
%python_build

%install
%python_install

#Create directories for files
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/opennode/
mkdir -p %buildroot%_sysconfdir/profile.d/

# create default storage endpoint
mkdir -p %buildroot%_localstatedir/storage/local/{iso,images,openvz/unpacked,kvm/unpacked}
mkdir -p %buildroot%_spooldir/opennode
#mkdir -p %buildroot%python_sitelibdir/salt/modules

#Copy files to system
cp scripts/* %buildroot/%_bindir/
cp conf/* %buildroot%_sysconfdir/opennode/
cp opennode-tui.sh %buildroot%_sysconfdir/profile.d/

#fix repocop warning for bin  permissions
chmod 755 %buildroot/%_bindir/detect-ip.py

%post
%__python -c "from opennode.cli.actions import storage; storage.add_pool('local')" ||:
##ln -sf %python_sitelibdir_noarch/opennode/cli/actions %buildroot%python_sitelibdir/salt/modules/onode ||:

%files
%config(noreplace) %_sysconfdir/opennode/opennode-tui.conf
%config(noreplace) %_sysconfdir/opennode/kvm.conf
%config(noreplace) %_sysconfdir/opennode/openvz.conf
%config(noreplace) %_sysconfdir/opennode/VM.conf
%_sysconfdir/profile.d/opennode-tui.sh

%_bindir/*

%python_sitelibdir_noarch/opennode/*
%python_sitelibdir_noarch/opennode_tui*
#python_sitelibdir/salt/modules/onode
%_localstatedir/storage
%dir %_sysconfdir/opennode
%dir %_spooldir/opennode

%exclude %python_sitelibdir_noarch/opennode/*.*
%exclude %dir %python_sitelibdir_noarch/opennode

%files -n python-module-opennode
%dir %python_sitelibdir_noarch/opennode
%python_sitelibdir_noarch/opennode/*.*

%changelog
* Tue Oct 28 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2.0.1-alt6.git.6af352f
- New version

* Sat Jul 05 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2.0.1-alt5.git.43b881d
- Fix repocop warning for bin permissions 

* Fri Jul 04 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2.0.1-alt4.git.43b881d
- Updated from git

* Wed Jan 02 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt3.git.cec422f06
- Add subpackage python-module-opennode
- Update from git

* Fri Dec 28 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt2.git.c37bc03e
- Bugfix version from git

* Mon Dec 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt1
- Build for ALT
