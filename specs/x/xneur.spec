Name: xneur
Version: 0.20.0
Release: alt2

Summary: X Neural Switcher

License: GPL
Group: Office
Url: http://xneur.ru/

Source: %{name}_%version.orig.tar.gz

# Automatically added by buildreq on Mon May 29 2017
# optimized out: glib2-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libxml2-devel perl perl-XML-Parser pkg-config python-base python-modules xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: glibc-devel-static gstreamer1.0-devel intltool libXinerama-devel libXtst-devel libaspell-devel libgtk+3-devel libnotify-devel libpcre-devel libxosd-devel

BuildPreReq: zlib-devel

Requires: lib%name = %version-%release

%description
Xneur is program like Punto Switcher, but has other
functionality and features for configuring.

%package -n lib%name
Summary: Libraries needed for %name
Group: System/Libraries

%description -n lib%name
Libraries needed for %name

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup
# Stupid unhack
sed -i 's/loKg_message/log_message/' lib/main/program.c

%build
%autoreconf
%configure --disable-static --with-spell=aspell
%make_build

# Hack for X-linking
##make -C lib/lib clean
##sed -i 's@^libxneur_la_LIBADD = ../misc/libxnmisc.la@libxneur_la_LIBADD = -L../config/.libs ../misc/libxnmisc.la ../config/libxnconfig.la@' lib/lib/Makefile
%make

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/%name/*.so %buildroot%_libdir/%name/*.la

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_sysconfdir/%name/
%dir %_libdir/%name/
%_libdir/%name/*.so.*
%_iconsdir/hicolor/*/*/*
%_datadir/%name/
%_man1dir/*
%_man5dir/*

%files -n lib%name
%_libdir/libxneur.so.*
%_libdir/libxnconfig.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/libxneur.so
#_libdir/libxneur.a
%_libdir/libxnconfig.so
%_pkgconfigdir/*.pc

%changelog
* Wed Oct 03 2018 Fr. Br. George <george@altlinux.ru> 0.20.0-alt2
- Rebuild with grstreamer1.0

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 0.20.0-alt1
- Autobuild version bump to 0.20.0

* Thu Nov 17 2016 Fr. Br. George <george@altlinux.ru> 0.19.0-alt1
- Autobuild version bump to 0.19.0

* Mon Oct 28 2013 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Autobuild version bump to 0.17.0
- Drop inactual patches

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.1
- Fixed build with new libX11

* Wed Jan 11 2012 Fr. Br. George <george@altlinux.ru> 0.15.0-alt1
- Autobuild version bump to 0.15.0
- Icon files added (still no .desktop)

* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 0.13.0-alt1
- Autobuild version bump to 0.13.0

* Sun May 22 2011 Fr. Br. George <george@altlinux.ru> 0.12.0-alt1
- Autobuild version bump to 0.12.0

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.qa2
- Fixed built

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Sat Mar 20 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version 0.9.8 (with rpmrb script)

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix build

* Sat Nov 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Sun Oct 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (fix bug #21039)

* Tue Aug 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5 (with rpmrb script)

* Sun Nov 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Fri Jul 25 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- release 0.9.1

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- 0.9.1 (svn revision 162)
- update requires, fix build on x86_64

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt2
- split library in libname package
- pack missed sound files

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- update buildreq

* Wed Sep 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt2
- move libxnconfig to libdir

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Tue Apr 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0, update buildreq, fix linking
- add post*_ldconfig

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version 0.4.0 (with rpmrb script)

* Thu Dec 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt0.1
- new version 0.3.0

* Wed Dec 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version (0.2.0)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.0_1-alt1
- release (build gxneur from separate package now)

* Thu Oct 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt0.1beta
- updated version

* Wed Aug 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt0.1alpha
- new version (from new author)
- fix URL, Source URL

* Tue Feb 22 2005 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt0.1
- new version

* Wed Jan 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt0.1
- first build for Sisyphus
