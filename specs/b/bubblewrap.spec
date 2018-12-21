%def_enable selinux

Name: bubblewrap
Version: 0.3.1
Release: alt1

Summary: Unprivileged sandboxing tool

Group: System/Base
License: LGPLv2+
Url: https://github.com/projectatomic/bubblewrap

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/projectatomic/bubblewrap/releases/download/v%version/bubblewrap-%version.tar.xz
# VCS: https://github.com/projectatomic/bubblewrap.git
Source: %name-%version.tar
#Source: https://github.com/projectatomic/%name/releases/download/v%version/%name-%version.tar.xz

BuildRequires: gcc-c++ binutils-devel libelf-devel
BuildRequires: db2latex-xsl docbook-style-xsl libcap-devel xsltproc
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
Many container runtime tools like systemd-nspawn, docker, etc. focus on providing
infrastructure for system administrators and orchestration tools (e.g. Kubernetes) to run containers.

These tools are not suitable to give to unprivileged users,
because it is trivial to turn such access into to a fully privileged root shell on the host.

%prep
%setup

%build
%autoreconf
%configure --with-priv-mode=none \
	--enable-require-userns=yes \
	%{subst_enable selinux}

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysctldir
cat > %buildroot%_sysctldir/90-bwrap.conf << _EOF_
kernel.userns_restrict = 0
_EOF_

%files
%attr(4511,root,root) %_bindir/bwrap
%_sysctldir/90-bwrap.conf
%_man1dir/bwrap*
%_datadir/bash-completion/completions/bwrap

%changelog
* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- updated to v0.3.1-4-g8fc5a96

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- updated to v0.3.0-1-gb3906bb
- enabled selinux support

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- fixed permissions for bwrap
- created %%_sysctldir/90-bwrap.conf

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.8-alt1
- new version 0.1.8 (with rpmrb script)

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- new version 0.1.7 (with rpmrb script)

* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)

* Sat Dec 31 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- new version 0.1.4 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus
