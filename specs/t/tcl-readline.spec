# -*- rpm-spec -*-
# $Id: tcl-readline,v 1.13 2006/07/22 12:12:05 me Exp $

%define teaname readline
%define srcname tclreadline
%define srcver 2.1.0

Name: tcl-%teaname
Version: 2.1.1
Release: alt8

Summary: GNU readline for the Tcl scripting language
License: BSD
Group: Shells
Url: http://tclreadline.sourceforge.net

# repacked ftp://tclreadline.sourceforge.net/pub/%srcname/%srcname-%srcver.tar.bz2
Source0: %srcname-%srcver.tar
Source1: sample.tclshrc
Patch0: %srcname-211.patch
Patch1: %srcname-2.1.0-interp.patch
Patch2: %srcname-2.1.0-init.patch
Patch3: %srcname-2.1.0-sf-completer.patch
Patch4: %srcname-2.1.0-x86_64.patch
Patch5: %srcname-2.1.0-rl_ding.patch
Patch6: %srcname-2.1.0-rl_completion_func_t.patch
# Debian patches
Patch10: %srcname-2.1.0-memuse.patch
Patch11: %srcname-2.1.0-rl_completion.patch
Patch12: %srcname-2.1.0-man-page.patch

BuildRequires: libreadline-devel libtinfo-devel rpm-build >= 4.0.4-alt41 tcl-devel >= 8.4.0-alt1
Requires: tcl >= 8.4.0-alt1

%package devel
Summary: development files for %srcname
Group: Development/C

%description
%name makes the gnu readline available to the scripting language tcl.
The primary purpose of the package is to facilitate the interactive
script development by the means of word and file name completion
as well as history expansion (well known from shells like bash).

%description devel
%name makes the gnu readline available to the scripting language tcl.
The primary purpose of the package is to facilitate the interactive
script development by the means of word and file name completion
as well as history expansion (well known from shells like bash).

This pacakge contains development files.

%prep
%setup -q -n %srcname-%srcver
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p2
%patch6 -p2
%patch10 -p1
%patch11 -p1
%patch12 -p1
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in
sed -i 's/lib%srcname.so/lib%srcname-%version.so/' pkgIndex.tcl.in

%build
autoreconf -fisv -Iaux
%add_optflags -DUSE_NON_CONST
%configure --libdir=%_tcllibdir --with-tlib-library="-ltinfo"
%make_build

%install
%make_install DESTDIR=%buildroot install \
	libdir=%_tcllibdir tclrldir=%_tcldatadir/%teaname
%__cp %SOURCE1 .

%files
%doc AUTHORS COPYING ChangeLog README TODO sample.tclshrc
%_tcllibdir/lib%{srcname}-*.so
%_tcldatadir/%teaname
%_mandir/mann/%srcname.n.*

%files devel
%_includedir/%{srcname}.h
%_tcllibdir/lib%{srcname}.so

%changelog
* Tue Jul 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.1-alt8
- Fixed working with threaded Tcl (Debian #175192).
- Fixed implicit declaration (Debian #226565).
- Fixed typos in man page (Debian #242369).
- Built devel subpackage.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.1-alt7.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt7
- fixed build on x86_64

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt6.1
- Rebuilt with libreadline.so.5.

* Sat Apr 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt6
- rebuilt in new env

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt5
- rebuilt against new shiny tcl reqprov finder

* Tue Sep 30 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt4
- rebuilt without ncurses

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt3
- rebuilt in new env

* Tue Oct  1 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.1-alt2
- rebuilt with tcl 8.4
- name changed

* Tue Jun  4 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.1-alt1
- 2.1.1
- delibification
- rl shells removed, `package require' use instead recommended
- libpath changed to %_tcllibdir

* Fri Dec  7 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.0-alt2
- rebuild in new env

* Thu Apr 26 2001 Sergey Bolshakoff <s.bolshakov@belcaf.com>
- First spec for ALTLinux distribution





