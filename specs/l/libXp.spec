Name: libXp
Version: 1.0.2
Release: alt1
Summary: X Print Library
License: (MIT or X11)
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

Source: %name-%version.tar.gz

##BuildRequires: libX11-devel libXau-devel libXext-devel libXdmcp-devel
##BuildRequires: xorg-proto-devel xorg-printproto-devel xorg-util-macros
BuildRequires: xorg-util-macros

# Automatically added by buildreq on Wed Jun 05 2013
# optimized out: libX11-devel libXau-devel pkg-config xorg-xproto-devel
BuildRequires: libXext-devel xorg-printproto-devel

%description
X Print Library

%package devel
Summary: X Print Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Wed Jun 05 2013 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2
- Recalculate buildreq

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.0-alt5.qa1
- NMU: rebuilt for updated dependencies.

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt5
- rebuilt for debuginfo

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt4.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.0-alt3.0
- Automated rebuild.

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

