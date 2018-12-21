
%def_disable gcrypt

Name: libssh
Version: 0.8.4
Release: alt2

Group: System/Libraries
Summary: C library to authenticate in a simple manner to one or more SSH servers
Url: http://www.libssh.org/
License: LGPL

# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source: http://www.libssh.org/files/%name-%version.tar.gz
Source1: version-script.libssh
Source2: compat.lds
Patch1: version-script.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake doxygen ghostscript-utils graphviz latex2html
BuildRequires: gcc-c++ %{?_enable_gcrypt: libgcrypt-devel}
BuildRequires: libssl-devel zlib-devel kde-common-devel
BuildRequires: libkrb5-devel

%description
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl). libssh features :

    * Full C library functions for manipulating a client-side SSH
      connection
    * Lesser GPL licensing -SSH2 protocol compliant
    * Fully configurable sessions
    * Support for AES-128,AES-192,AES-256,blowfish, in cbc mode
    * Use multiple SSH connections in a same process, at same time
    * Use multiple channels in the same connection
    * Thread safety when using different sessions at same time
    * Basic but correct SFTP implementation (secure file transfer)
    * RSA and DSS server public key supported
    * Compression support (with zlib)
    * Public key (RSA and DSS), password and keyboard-interactive
      authentication
    * Complete documentation about its API
    * Runs and tested under amd64, x86, arm, sparc32, ppc under Linux,
      BSD, MacosX and Solaris
    * A developer listening to you
    * It's free (LGPL)!


%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release
Provides: ssh-devel = %version-%release
%description devel
This package contains the development files for %name.


%prep
%setup -q
%patch1 -p1
install -m 0644 %SOURCE1 ./
install -m 0644 %SOURCE2 ./

%build
%Kbuild \
    -DWITH_ZLIB=ON \
    -DWITH_GSSAPI=ON \
    -DWITH_GCRYPT=%{?_enable_gcrypt:ON}%{!?_enable_gcrypt:OFF} \
    #

%install
%Kinstall

%files
%_libdir/libssh.so.4
%_libdir/libssh.so.*

%files devel
%_pkgconfigdir/%name.pc
%_libdir/cmake/libssh*
%_includedir/%name
%_libdir/*.so

%changelog
* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.4-alt2
- fix changelog
- security fixes: CVE-2018-10933

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.4-alt1
- new version
- security fix: CVE-2018-10933

* Mon Oct 08 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt1
- new version

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1%ubt
- new version

* Tue Aug 08 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.5-alt1%ubt
- new version
- security fix: CVE-2016-0739

* Thu Feb 11 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1.M70P.1
- build for M70P

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt2
- build without libgcrypt

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Wed Jun 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt0.M70P.1
- build for M70P

* Wed Jun 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt1
- new version
- security fix: CVE-2015-3146

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt0.M70P.1
- built for M70P

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version
- security fixes: CVE-2014-0017, CVE-2014-0017

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 0.5.5-alt0.M70P.1
- built for M70P

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 0.5.5-alt1
- new version

* Wed Nov 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt0.M60P.1
- built for M60P

* Wed Nov 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version
- security fixes: CVE-2012-4559, CVE-2012-4560, CVE-2012-4561

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt0.M60P.1
- built for M60P

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt1
- new version

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt0.M60P.1
- built for M60P

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.8-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.6-alt1
- new version

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.5-alt1
- new version
- add versioning

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt0.M51.1
- built for M51

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt0.M51.1
- built for M51

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- built for ALT

