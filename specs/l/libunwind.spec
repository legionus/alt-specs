Name: libunwind
Version: 1.1
Release: alt2

Summary: An unwinding library
License: BSD
Group: Development/Debuggers
Url: http://savannah.nongnu.org/projects/libunwind

Source: %name-%version.tar
Patch1: libunwind-1.1-aarch64.patch
Patch2: libunwind-1.1-fix-CVE-2015-3239.patch

%description
Libunwind provides a C ABI to determine the call-chain of a program.

%package devel
Summary: Development package for libunwind
Group: Development/Debuggers
Requires: libunwind = %version-%release

%description devel
The libunwind-devel package includes the libraries and header files for
libunwind.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-static
make

%install
%makeinstall

%files
%doc COPYING README NEWS
%_libdir/libunwind*.so.*

%files devel
%_libdir/libunwind*.so
%_pkgconfigdir/*.pc
%_mandir/*/*
%_includedir/*

%changelog
* Mon Sep 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1-alt2
- Fixed CVE-2015-3239.
- Added aarch64 architecture support.

* Thu Jun 27 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt1
- 1.1 release

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99-alt5.2
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99-alt5.1
- Rebuilt for soname set-versions

* Wed May 12 2010 Alexey Voinov <voins@altlinux.ru> 0.99-alt5
- Disabled build of libunwind-setjmp.so

* Thu Aug 27 2009 Alexey Voinov <voins@altlinux.ru> 0.99-alt4
- Fixed install order for libraries
- Fixed interlib deps

* Tue Apr 28 2009 Yuriy Kashirin <uka@altlinux.ru> 0.99-alt3
- Fixed build with new libtool

* Sat Dec 13 2008 Yuriy Kashirin <uka@altlinux.ru> 0.99-alt2
- Moved package to git
- Fixed build in sisyphus (drpintf collision)
- Removed obsolete post{,un}_ldconfig

* Thu May 17 2007 Avramenko Andrew <liks@altlinux.ru> 0.99-alt1
- Initial build for Sisyphus

* Thu Apr  5 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 0.99-0.1.frysk20070405cvs
- Update to the upstream snapshot snap-070224.
- Use the Frysk's modified version, currently snapshot 20070405cvs.
- Extend the supported architectures from ia64 also to x86_64, i386 and ppc64.
- Spec file fixups.
- Split the package to its base and the `devel' part.
- Drop the statically built libraries.

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.98.5-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 22 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 0.98.5-2
- SELinux compatibility fix - stack is now non-exec (Jakub Jelinek suggestion).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.98.5-1.1
- rebuild

* Sat May 27 2006 Alexandre Oliva <aoliva@redhat.com> - 0.98.5-1
- Import version 0.98.5.

* Thu Feb 09 2006 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.98.2-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Mar 01 2005 Jeff Johnston <jjohnstn@redhat.com>	0.98.2.3
- Bump up release number

* Thu Nov 11 2004 Jeff Johnston <jjohnstn@redhat.com>	0.98.2.2
- Import version 0.98.2.

* Wed Nov 10 2004 Jeff Johnston <jjohnstn@redhat.com>	0.97.6
- Bump up release number

* Thu Aug 19 2004 Jeff Johnston <jjohnstn@redhat.com>	0.97.3
- Remove debug file from files list.

* Fri Aug 13 2004 Jeff Johnston <jjohnstn@redhat.com>	0.97.2
- Import version 0.97.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 09 2004  Elena Zannoni <ezannoni@redhat.com>	0.96.4
- Bump release number.

* Mon Feb 23 2004  Elena Zannoni <ezannoni@redhat.com>	0.96.3
- Bump release number.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004  Jeff Johnston <jjohnstn@redhat.com>	0.96.1
- Import version 0.96.

* Tue Jan 06 2004  Jeff Johnston <jjohnstn@redhat.com>	0.92.2
- Bump release number.

* Mon Oct 06 2003  Jeff Johnston <jjohnstn@redhat.com>	0.92.1
- Initial release

