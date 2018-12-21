#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: dahdi-linux
Summary: DAHDI drivers for Digium hardware and Asterisk
Version: 3.0.0
Release: alt1
License: GPL
Group: System/Kernel and hardware
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Source2: %name.watch
Url: http://downloads.asterisk.org/pub/telephony/dahdi-linux/

%package headers
Summary: DAHDI headers
Group: System/Kernel and hardware

%description headers
DAHDI headers

%package -n firmware-dahdi
Summary: firmware for Digium cards
Group: System/Kernel and hardware
BuildArch: noarch

%description -n firmware-dahdi
firmware for Digium cards

%package -n kernel-source-dahdi
Summary: Linux DAHDI module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-dahdi
This package contains DAHDI sources for Linux kernel module


%description -n kernel-source-dahdi -l ru_RU.KOI8-R
���� ����� �������� ��������� DAHDI ��� ������ ���� ������


%description
Dahdi drivers only


%prep
%setup
%patch -p1
sed -i 's/^all:.*/all:/' drivers/dahdi/firmware/Makefile
t="$RPM_SOURCE_DIR/kernel-source-dahdi-%version"
rm -rf "$t"
mkdir -p $t/dahdi
cp -a ./ "$t/dahdi"
mv "$t" .

%install
make DESTDIR=%buildroot install-include
mkdir -p %buildroot/lib/firmware
install -m 6400  drivers/dahdi/firmware/*.bin %buildroot/lib/firmware/
mkdir -p %buildroot%_usrsrc/kernel/sources
du -hsc kernel-source-dahdi-%version
tar cjf \
	%buildroot%_usrsrc/kernel/sources/kernel-source-dahdi-%version.tar.bz2 \
	kernel-source-dahdi-%version

%files headers
%dir %_includedir/dahdi
%_includedir/dahdi/dahdi_config.h
%_includedir/dahdi/fasthdlc.h
%_includedir/dahdi/kernel.h
%_includedir/dahdi/user.h
%_includedir/dahdi/wctdm_user.h

%files -n firmware-dahdi
/lib/firmware/*

%files -n kernel-source-dahdi
%_usrsrc/kernel/sources/kernel-source-dahdi-%version.tar.bz2

%changelog
* Sun Nov 18 2018 Cronbuild Service <cronbuild@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Thu Mar 03 2016 Cronbuild Service <cronbuild@altlinux.org> 2.11.1-alt1
- new version 2.11.1

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Mon Jun 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.10.2-alt1
- new version 2.10.2

* Thu Feb 19 2015 Denis Smirnov <mithraen@altlinux.ru> 2.10.1-alt1
- new version 2.10.1

* Fri Dec 12 2014 Denis Smirnov <mithraen@altlinux.ru> 2.10.0.1-alt2
- fix build with kernel 3.18

* Wed Oct 22 2014 Denis Smirnov <mithraen@altlinux.ru> 2.10.0.1-alt1
- new version 2.10.0.1

* Wed Sep 03 2014 Denis Smirnov <mithraen@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Wed Dec 18 2013 Denis Smirnov <mithraen@altlinux.ru> 2.7.0.2-alt1
- 2.7.0.2

* Sun Jun 30 2013 Denis Smirnov <mithraen@altlinux.ru> 2.7.0-alt1
- new version 2.7.0

* Fri Apr 19 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.2-alt1
- new version 2.6.2

* Sun Sep 02 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Feb 13 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt2
- enable ppp support and pcap support

* Mon Feb 13 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Oct 26 2011 Denis Smirnov <mithraen@altlinux.ru> 2.5.0.2-alt1
- 2.5.0.2

* Sun Aug 28 2011 Denis Smirnov <mithraen@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 2.4.1.2-alt3
- really disable firmware downloading

* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 2.4.1.2-alt2
- update firmware
- disable firmware downloading

* Tue Jun 28 2011 Denis Smirnov <mithraen@altlinux.ru> 2.4.1.2-alt1
- 2.4.1.2

* Sat Jan 22 2011 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt2
- package firmware for digium cards

* Sun Apr 18 2010 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sun Mar 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Sun Mar 14 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt2
- update firmware

* Thu Jan 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Nov 11 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt4
- add short flash support by default

* Mon Sep 07 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt3
- rebuild

* Sun Sep 06 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt2
- add Url tag
- add Packager tag

* Sat Jul 11 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0.1-alt1
- first build for Sisyphus

