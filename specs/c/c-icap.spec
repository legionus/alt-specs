Name: 	 c-icap
Version: 0.5.2
Release: alt3.qa1
Epoch:	 1
Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: ICAP server
License: %lgpl2only
Group: 	 System/Servers
Url: 	 http://c-icap.sourceforge.net/

Source0: %name-%version.tar.gz
Source1: %name.init
Source2: %name.watch
Source3: %name.conf

Requires(pre): shadow-utils

BuildRequires: rpm-build-licenses

BuildRequires: doxygen libdb4-devel libldap-devel libmemcached-devel zlib-devel bzlib-devel

%description
Implementation of an Internet Content Adaptation Protocol (ICAP) server.

%package devel
Summary: ICAP development files
Group: Development/C
Requires: %name = %EVR

%description devel
Headers and libraries for an Internet Content Adaptation Protocol (ICAP)
server implementation.

%if_with clamav
%package clamav
Summary: ICAP ClamAV module
Group: System/Servers
Requires: %name = %EVR

%description clamav
ICAP module for scanning content with ClamAV.
%endif

%prep
%setup -q

%build
%autoreconf
%undefine _configure_gettext
%configure --localstatedir=%_var
%make_build

%install
%makeinstall_std

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/%name %buildroot%_sbindir/%name

mkdir -p %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/{server,access}.log

mkdir -p %buildroot{%_var/run/%name,%_cachedir/%name}

rm -f %buildroot%_libdir/c_icap/*.la

# Fix configuration
. shell-config
%define cfg_set shell_config_set %buildroot%_sysconfdir/%name.conf
%cfg_set PidFile     %_runtimedir/%name/%name.pid ' ' ' '
%cfg_set ModulesDir  %_libdir/c_icap ' ' ' '
%cfg_set ServicesDir %_libdir/c_icap ' ' ' '
%cfg_set ServerLog   %_logdir/%name/server.log ' ' ' '
%cfg_set AccessLog   %_logdir/%name/access.log ' ' ' '
%cfg_set LoadMagicFile %_sysconfdir/%name.magic ' ' ' '

# Install /var/run rules
install -Dm 0644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

%pre
/usr/sbin/groupadd -r -f _c_icap ||:
/usr/sbin/useradd -M -n _c_icap -r -d %_runtimedir/%name -s /dev/null -c "System user for %name" -g _c_icap > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS README TODO contrib/get_file.pl
%config(noreplace) %_sysconfdir/%name.conf*
%config(noreplace) %_sysconfdir/%name.magic*
%attr (755,root,root) %_initdir/%name
%_bindir/*
%attr (755,root,root) %_sbindir/%name
%dir %_libdir/c_icap/
%_libdir/c_icap/*.so
%_libdir/libicapapi.so.*
%if_with clamav
%exclude %_libdir/c_icap/srv_clamav.so
%endif
%attr (750,_c_icap,root) %_logdir/%name/
%ghost %_logdir/%name/*.log
%attr (750,_c_icap,root) %_var/run/%name/
%attr (750,_c_icap,root) %_cachedir/%name/
%_tmpfilesdir/%name.conf
%_man8dir/c-icap*.8*

%files devel
%_includedir/c_icap
%_libdir/libicapapi.so

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.5.2-alt3.qa1
- NMU: applied repocop patch

* Thu Feb 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.5.2-alt3
- Fixed localstatedir location.

* Mon Oct 16 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.2-alt2
- Fix missing /var/run/c-icap after reboot

* Sun Oct 08 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.2-alt1
- New version
- Package run and cache dirs to fix daemon run

* Sat Mar 19 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt3
- Updated BuildRequires (gear-buildreq output used)

* Thu Mar 10 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt2
- Spec's cleanup
- Added LSB init header (fixed repocop's error)
- Removed gcc-c++ from BuildRequires

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.4.2-alt1
- New version
- Spec's cleanup
- Built without libclamav-devel
  (modules was moved to separate c-icap-modules package)
- Renamed libdir and includedir to c_icap as in upstream

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080706.01-alt2.3
- Fixed build

* Mon Apr 05 2010 Anton Pischulin <letanton@altlinux.ru> 20080706.01-alt2.2
- Fixed base64.c

* Fri Feb 26 2010 Andrey Cherepanov <cas@altlinux.org> 20080706-alt0.1.M50P.1
- Backport to p5

* Wed Nov 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20080706-alt1.1
- Built for sisyphus

* Mon Sep 28 2009 Grigory Batalov <bga@altlinux.ru> 20080706-alt2.M40.1
- New upstream release (c_icap-20080706).
- Updated url_filter.

* Wed Apr 15 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.2
- Pre-requirement of shadow-utils were added.
- Url-filter provides c-icap-skf.

* Thu Apr 09 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.1
- Rebuilt with custom url_filter.
- Built for ALT Linux branch 4.0.

* Thu Mar 22 2007 ALT QA Team Robot <qa-robot@altlinux.org> 20060603-alt1.0
- Rebuilt with libclamav.so.2.

* Wed Jan 17 2007 Grigory Batalov <bga@altlinux.ru> 20060603-alt1
- Initial ALTLinux release.
