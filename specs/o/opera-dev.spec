%define		softver 46.0
%define		buildver 2573.0

Name:		opera-dev
Version:	%softver.%buildver
Release:	alt4
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	A fast and secure web browser and Internet suite
Group:		Networking/WWW
License:	Distributable
Vendor:		Opera Software ASA
Url:		http://www.opera.com/
Source0:	opera-%softver.%buildver.i386.linux.tar.bz2

ExclusiveArch:	%ix86

%add_verify_elf_skiplist %_libdir/*-linux-gnu/opera-developer/*.so
%set_verify_elf_method textrel=relaxed

BuildRequires: libGConf libXScrnSaver libXtst libalsa libcurl libnotify libnss libgtk+3 libgtk+2

%description
Opera is a small, fast, customizable, powerful and user-friendly web
browser, as well as an Internet suite, including an email client, an IRC
client, web developer tools (Opera Dragonfly), and a personal web server
(Opera Unite).

%prep
%setup -q -n opera-%softver.%buildver.i386.linux

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_datadir}
cp -a ./lib/* %buildroot%_libdir/
cp -a ./share/* %buildroot%_datadir
ln -s %_libdir/i386-linux-gnu/opera-developer/opera-developer %buildroot%_bindir/opera-developer
subst 's|PepperFlash/libpepflashplayer.so|pepper-plugins/libpepflashplayer.so|g' %buildroot%_libdir/*-linux-gnu/opera-developer/resources/pepper_flash_config.json

%post
chmod 4755 %_libdir/i386-linux-gnu/opera-developer/opera_sandbox

%files
%_docdir/opera-developer
%_bindir/*
%_libdir/*-linux-gnu
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_datadir/lintian
%_datadir/mime/packages/*.xml

%changelog
* Fri Aug 18 2017 Motsyo Gennadi <drool@altlinux.ru> 46.0.2573.0-alt4
- fix build

* Thu Aug 17 2017 Motsyo Gennadi <drool@altlinux.ru> 46.0.2573.0-alt3
- fix requires

* Tue Aug 08 2017 Motsyo Gennadi <drool@altlinux.ru> 46.0.2573.0-alt2
- build only x86

* Sun May 21 2017 Motsyo Gennadi <drool@altlinux.ru> 46.0.2573.0-alt1
- packaged 46.0.2573.0 snapshot

* Mon Apr 17 2017 Motsyo Gennadi <drool@altlinux.ru> 46.0.2556.0-alt1
- packaged 46.0.2556.0 snapshot

* Wed Mar 22 2017 Motsyo Gennadi <drool@altlinux.ru> 45.0.2539.0-alt1
- packaged 45.0.2539.0 snapshot

* Mon Mar 06 2017 Motsyo Gennadi <drool@altlinux.ru> 45.0.2522.0-alt1
- packaged 45.0.2522.0 snapshot

* Sat Feb 18 2017 Motsyo Gennadi <drool@altlinux.ru> 44.0.2505.0-alt1
- packaged 44.0.2505.0 snapshot

* Tue Feb 07 2017 Motsyo Gennadi <drool@altlinux.ru> 44.0.2494.0-alt1
- packaged 44.0.2494.0 snapshot

* Fri Feb 03 2017 Motsyo Gennadi <drool@altlinux.ru> 44.0.2487.0-alt1
- packaged 44.0.2487.0 snapshot

* Tue Jan 17 2017 Motsyo Gennadi <drool@altlinux.ru> 44.0.2475.0-alt1
- packaged 44.0.2475.0 snapshot

* Thu Jan 05 2017 Motsyo Gennadi <drool@altlinux.ru> 44.0.2463.0-alt1
- packaged 44.0.2463.0 snapshot

* Thu Dec 08 2016 Motsyo Gennadi <drool@altlinux.ru> 43.0.2431.0-alt1
- packaged 43.0.2431.0 snapshot

* Tue Nov 29 2016 Motsyo Gennadi <drool@altlinux.ru> 43.0.2423.0-alt1
- packaged 43.0.2423.0 snapshot

* Wed Nov 23 2016 Motsyo Gennadi <drool@altlinux.ru> 43.0.2420.0-alt1
- packaged 43.0.2420.0 snapshot

* Wed Nov 16 2016 Motsyo Gennadi <drool@altlinux.ru> 43.0.2412.0-alt1
- packaged 43.0.2412.0 snapshot

* Tue Nov 08 2016 Motsyo Gennadi <drool@altlinux.ru> 43.0.2403.0-alt1
- packaged 43.0.2403.0 snapshot

* Sun Oct 30 2016 Motsyo Gennadi <drool@altlinux.ru> 42.0.2392.0-alt1
- packaged 42.0.2392.0 snapshot

* Mon Oct 10 2016 Motsyo Gennadi <drool@altlinux.ru> 42.0.2372.0-alt1
- packaged 42.0.2372.0 snapshot

* Thu Sep 15 2016 Motsyo Gennadi <drool@altlinux.ru> 41.0.2349.0-alt1
- packaged 41.0.2349.0 snapshot

* Wed Sep 07 2016 Motsyo Gennadi <drool@altlinux.ru> 41.0.2340.0-alt1
- packaged 41.0.2340.0 snapshot

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 41.0.2329.0-alt1
- packaged 41.0.2329.0 snapshot

* Fri Aug 19 2016 Motsyo Gennadi <drool@altlinux.ru> 41.0.2323.0-alt1
- packaged 41.0.2323.0 snapshot

* Thu Aug 11 2016 Motsyo Gennadi <drool@altlinux.ru> 41.0.2315.0-alt1
- packaged 41.0.2315.0 snapshot

* Thu Aug 04 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2306.0-alt1
- packaged 40.0.2306.0 snapshot

* Thu Jul 28 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2301.0-alt1
- packaged 40.0.2301.0 snapshot

* Thu Jul 21 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2296.0-alt1
- packaged 40.0.2296.0 snapshot

* Wed Jul 13 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2288.0-alt1
- packaged 40.0.2288.0 snapshot

* Mon Jul 04 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2280.0-alt1
- packaged 40.0.2280.0 snapshot

* Tue Jun 28 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2273.0-alt1
- packaged 40.0.2273.0 snapshot

* Wed Jun 22 2016 Motsyo Gennadi <drool@altlinux.ru> 40.0.2267.0-alt1
- packaged 40.0.2267.0 snapshot

* Thu Jun 02 2016 Motsyo Gennadi <drool@altlinux.ru> 39.0.2248.0-alt1.1
- fix 64 content

* Thu Jun 02 2016 Motsyo Gennadi <drool@altlinux.ru> 39.0.2248.0-alt1
- packaged 39.0.2248.0 snapshot

* Mon May 30 2016 Motsyo Gennadi <drool@altlinux.ru> 39.0.2245.0-alt1
- packaged 39.0.2245.0 snapshot

* Thu May 19 2016 Motsyo Gennadi <drool@altlinux.ru> 39.0.2234.0-alt1
- packaged 39.0.2234.0 snapshot

* Sun May 15 2016 Motsyo Gennadi <drool@altlinux.ru> 39.0.2226.0-alt1
- packaged 39.0.2226.0 snapshot

* Sun May 01 2016 Motsyo Gennadi <drool@altlinux.ru> 38.0.2213.0-alt1
- packaged 38.0.2213.0 snapshot

* Thu Apr 21 2016 Motsyo Gennadi <drool@altlinux.ru> 38.0.2205.0-alt1
- packaged 38.0.2205.0 snapshot

* Fri Apr 15 2016 Motsyo Gennadi <drool@altlinux.ru> 38.0.2198.0-alt1
- packaged 38.0.2198.0 snapshot

* Wed Apr 06 2016 Motsyo Gennadi <drool@altlinux.ru> 38.0.2190.0-alt1
- packaged 38.0.2190.0 snapshot

* Fri Mar 18 2016 Motsyo Gennadi <drool@altlinux.ru> 37.0.2171.0-alt1
- packaged 37.0.2171.0 snapshot

* Wed Mar 16 2016 Motsyo Gennadi <drool@altlinux.ru> 37.0.2163.0-alt1
- packaged 37.0.2163.0 snapshot

* Sat Mar 05 2016 Motsyo Gennadi <drool@altlinux.ru> 37.0.2157.0-alt1
- packaged 37.0.2157.0 snapshot

* Thu Feb 18 2016 Motsyo Gennadi <drool@altlinux.ru> 37.0.2142.0-alt1
- packaged 37.0.2142.0 snapshot

* Fri Feb 05 2016 Motsyo Gennadi <drool@altlinux.ru> 36.0.2129.0-alt1
- packaged 36.0.2129.0 snapshot

* Thu Jan 28 2016 Motsyo Gennadi <drool@altlinux.ru> 36.0.2120.0-alt1
- packaged 36.0.2120.0 snapshot

* Thu Jan 14 2016 Motsyo Gennadi <drool@altlinux.ru> 36.0.2106.0-alt1
- packaged 36.0.2106.0 snapshot

* Tue Dec 22 2015 Motsyo Gennadi <drool@altlinux.ru> 36.0.2079.0-alt1
- packaged 36.0.2079.0 snapshot

* Mon Dec 14 2015 Motsyo Gennadi <drool@altlinux.ru> 36.0.2072.0-alt1
- packaged 36.0.2072.0 snapshot

* Sun Dec 06 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2064.0-alt1
- packaged 35.0.2064.0 snapshot

* Fri Nov 27 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2060.0-alt1
- packaged 35.0.2060.0 snapshot

* Wed Nov 18 2015 Motsyo Gennadi <drool@altlinux.ru> 35.0.2052.0-alt1
- packaged 35.0.2052.0 snapshot

* Fri Nov 13 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2044.0-alt1
- packaged 34.0.2044.0 snapshot

* Sat Nov 07 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2036.2-alt1
- packaged 34.0.2036.2 snapshot

* Sun Oct 25 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2026.0-alt1
- packaged 34.0.2026.0 snapshot

* Tue Oct 20 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2023.0-alt1
- packaged 34.0.2023.0 snapshot

* Fri Oct 09 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.2011.0-alt1
- packaged 34.0.2011.0 snapshot

* Sat Sep 26 2015 Motsyo Gennadi <drool@altlinux.ru> 34.0.1996.0-alt1
- packaged 34.0.1996.0 snapshot

* Fri Sep 11 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1982.0-alt1
- packaged 33.0.1982.0 snapshot

* Wed Sep 02 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1967.0-alt1
- packaged 33.0.1967.0 snapshot

* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 33.0.1963.0-alt1
- packaged 33.0.1963.0 snapshot

* Thu Jul 23 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1933.0-alt1
- packaged 32.0.1933.0 snapshot

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1.1
- change git folders

* Thu Jul 16 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1926.0-alt1
- packaged 32.0.1926.0 snapshot

* Thu Jul 02 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1910.0-alt1
- packaged 32.0.1910.0 snapshot

* Thu Jun 18 2015 Motsyo Gennadi <drool@altlinux.ru> 32.0.1899.0-alt1
- packaged 32.0.1899.0 snapshot

* Thu Jun 11 2015 Motsyo Gennadi <drool@altlinux.ru> 31.0.1876.0-alt1
- packaged for ALT Linux
