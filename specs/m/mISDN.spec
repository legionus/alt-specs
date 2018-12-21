%define svndate 20110114

Name: mISDN
Version: 1.1.5
Release: alt3.1

Summary: %name library utilites

License: LGPL
Group: System/Servers
Url: http://www.misdn.org/

Obsoletes: misdn
Conflicts: misdn

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: misdn-%version.tar
Patch1: misdn-%version-%release.patch
Source2: mISDN.rules

Requires: asterisk-base

Requires: libmISDN = %version-%release

# Automatically added by buildreq on Sat Mar 18 2006
BuildRequires: flex libgsm-devel libncurses-devel

%description
mISDN library utilites

%package -n lib%name
Summary: mISDN library
Group: %group

Obsoletes: libmisdn
Conflicts: libmisdn

%description -n lib%name
mISDN library

%package -n lib%name-devel
Requires: lib%name = %version-%release
Summary: mISDN library headers
Group: Development/C

Obsoletes: libmisdn-devel
Provides: libmisdn-devel

%description -n lib%name-devel
%name library headers

%package -n lib%name-devel-static
Requires: lib%name-devel = %version-%release
Summary: %name static library
Group: Development/C

Obsoletes: libmisdn-devel-static
Conflicts: libmisdn-devel-static

%description -n lib%name-devel-static
%name static library

%package -n kernel-source-%name
Summary: Linux %name module sources
Group: Development/Kernel

%description -n kernel-source-%name
This package contains %name sources for Linux kernel module

%prep
%setup -n misdn-%version
%patch1 -p1


cp -a mISDN/include/linux mISDNuser/include/

%build
export CFLAGS=-fPIC
cd mISDNuser
subst 's!/usr/lib/libgsm!/usr/%_lib/libgsm!' voip/Makefile
subst 's!usr/lib!usr/%_lib!' lib/Makefile i4lnet/Makefile

# SMP incompatible build
make

subst 's!linux/mISDNif.h!mISDNif.h!' include/*.h
subst 's!linux/isdn_compat.h!isdn_compat.h!' include/*.h

%install
# Make kernel-source tarball
cp -a mISDN kernel-source-%name-%version
mkdir -p %buildroot%_usrsrc/kernel/sources
du -hsc kernel-source-%name-%version
tar cjf \
        %buildroot%_usrsrc/kernel/sources/kernel-source-%name-%version.tar.bz2 \
	    kernel-source-%name-%version

cd mISDNuser
mkdir -p %buildroot%_libdir
cp -a include/linux/*.h include/
mkdir -p %buildroot%_libdir
%make_install INSTALL_PREFIX=%buildroot install

install -d %buildroot%_udevrulesdir
install %SOURCE2 %buildroot%_udevrulesdir/00-misdn.rules

%if %_lib != "lib"
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name
%_libdir/libisdnnet.so
%_libdir/libsuppserv.so
%_libdir/libmISDN.so

%files -n lib%name-devel
%dir %_includedir/mISDNuser
%_includedir/mISDNuser/*.h

%files
%_bindir/loadfirm
%_bindir/sendhwctrl
%_bindir/testcon
%_bindir/testcon_l2
%_bindir/testlayer1
%_bindir/testlayer3
%_bindir/testlib
%_bindir/tstlib
%_bindir/voipisdn
%_bindir/misdnportinfo
%_bindir/mISDNdebugtool
%_udevrulesdir/00-misdn.rules

%files -n kernel-source-%name
%_usrsrc/kernel/sources/kernel-source-%name-%version.tar.bz2

%changelog
* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt3.1
- fix build on aarch64

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.5-alt3
- Fixed build with gcc-6

* Wed Apr 24 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1.5-alt2
- repocop fixes

* Fri Nov 16 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sat Jan 14 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1.3-alt0.20110114
- svn update
- fix rpath

* Sat Apr 02 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt5.20070317
- rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt4.20070317
- auto rebuild

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3.20070317
- cleanup spec

* Thu Apr 12 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2.20070317
- try to really fix x86_64 build

* Thu Apr 12 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1.20070317
- try to fix x86_64 build

* Sun Mar 18 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt0.20070317
- this packages replace misdn
- fix #9734 (ldconfig)
- build kernel modules source package
- add udev rules
