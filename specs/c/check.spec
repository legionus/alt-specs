%def_enable static
%define EVR %{?epoch:%epoch:}%version-%release

Name: check
Version: 0.12.0
Release: alt1
Epoch: 20180202

Summary: A unit test framework for C
License: LGPL
Group: Development/C

Url: https://github.com/libcheck/check
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

Requires: info-install

%add_optflags %optflags_shared
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Check is a unit test framework for C. It features a simple
interface for defining unit tests, putting little in the way
of the developer. Tests are run in a separate address space,
so Check can catch both assertion failures and code errors that
cause segmentation faults or other signals. The output from unit
tests can be used within source code editors and IDEs.

%package -n lib%name
Summary: A unit test framework for C (core library)
Group: Development/C
Conflicts: %name < 20070219:0.9.5-alt4

%description -n lib%name
Check is a unit test framework for C.

This package contains check library.

%package -n lib%name-devel
Summary: A unit test framework for C (development headers)
Group: Development/C
Requires: lib%name = %EVR
Conflicts: %name < 20070219:0.9.5-alt4

%description -n lib%name-devel
Check is a unit test framework for C.

This package contains library header files needed to build
software with libcheck.

%if_enabled static
%package -n lib%name-devel-static
Summary: A unit test framework for C (static library)
Group: Development/C
Requires: lib%name = %EVR
Conflicts: %name < 20070219:0.9.5-alt4

%description -n lib%name-devel-static
Check is a unit test framework for C.

This package contains a static development library.
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_bindir/checkmk
%_man1dir/checkmk.1*

%files -n lib%name
%doc AUTHORS NEWS THANKS TODO
%_docdir/%name
%exclude %_docdir/%name/example
%_libdir/*.so.*
%_infodir/*info*

%files -n lib%name-devel
%doc %_docdir/%name/example
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Feb 02 2018 Grigory Ustinov <grenka@altlinux.org> 20180202:0.12.0-alt1
- NMU:
  + build new version (Closes: #33422).
  + change packaging method (transfer to github).

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 20121107:0.10.0-alt1.1
- NMU: added BR: texinfo

* Mon Aug 03 2015 Michael Shigorin <mike@altlinux.org> 20121107:0.10.0-alt1
- new version (watch file uupdate)

* Mon Aug 04 2014 Michael Shigorin <mike@altlinux.org> 20121107:0.9.14-alt1
- new version (watch file uupdate)

* Sat May 31 2014 Michael Shigorin <mike@altlinux.org> 20121107:0.9.13-alt1
- new version (watch file uupdate)

* Wed Jan 22 2014 Michael Shigorin <mike@altlinux.org> 20121107:0.9.12-alt1
- new version (watch file uupdate)

* Tue Nov 12 2013 Michael Shigorin <mike@altlinux.org> 20121107:0.9.11-alt1
- new version (watch file uupdate)

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 20121107:0.9.10-alt1
- new version (watch file uupdate)

* Tue Nov 06 2012 Michael Shigorin <mike@altlinux.org> 20121107:0.9.9-alt1
- new version (watch file uupdate)
- added checkmk(1) to the main package

* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 20120522:0.9.8-alt3
- clarified intersubpackage Requires: with Epoch:
  to be strict (thanks led@ for spotting the incompleteness
  of the preexisting dependencies, only half of them were epochal)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 20120509:0.9.8-alt2
- added watch file

* Tue Oct 19 2010 Michael Shigorin <mike@altlinux.org> 20101019:0.9.8-alt1
- 0.9.8
- introduced conditional static library build
  (enabled by default for kas@)

* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 20090729:0.9.6-alt2
- applied repocop patch
- minor spec cleanup

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 20090407:0.9.6-alt1
- 0.9.6
- removed patch
- buildreq

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 20081204:0.9.5-alt8
- applied repocop patch

* Sat Apr 12 2008 Michael Shigorin <mike@altlinux.org> 20070412:0.9.5-alt7
- rebuilt to fix requires (#15331)

* Thu Oct 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070219:0.9.5-alt6
- NMU:
  + fixed check.m4

* Sun Sep 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070219:0.9.5-alt5
- NMU:
  + libification
  + disable static

* Mon Feb 19 2007 Michael Shigorin <mike@altlinux.org> 20070219:0.9.5-alt4
- should fix dist-upgrade after package split rolled back (#10860)
  + thanks azol@ for noticing

* Fri Feb 16 2007 Michael Shigorin <mike@altlinux.org> 20070216:0.9.5-alt3
- fixed silly cut-n-paste bug when getting Packager: back
  (thanks ns@)

* Thu Feb 15 2007 Michael Shigorin <mike@altlinux.org> 20070215:0.9.5-alt2
- reverted 0.9.5-alt1 spec revamp (broke confuse package for wrar@)
- reverted doc installation chages from 0.9.3-alt1.2 (back to standard)
- package should work again

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 20061210:0.9.5-alt1
- 0.9.5
- minor spec cleanup
- updated Epoch: (was actually there, and it's not removable)
- buildreq
- added doc subpackage and texinfo manual
- libification

* Fri Jun 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 20051031:0.9.3-alt1.2
- NMU
- Added -fPIC to CFLAGS (bug 9652)
- Do not use %%doc in filelist because make install does the right thing

* Fri Jan 13 2006 LAKostis <lakostis at altlinux.ru> 20051031:0.9.3-alt1.1
- get rid of ugly Epoch.

* Mon Oct 31 2005 LAKostis <lakostis at altlinux.ru> 20051031:0.9.3-alt1
- 0.9.3.
- NMU.
- Updated Buildreq.

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 20031107:0.8.4-alt1
- built for ALT Linux (librapi2 build dependency)
- merged description from spec by Sven Neumann <sven@convergence.de> and 
  Arien Malec <arien_malec@yahoo.com>, but otherwise rewrote from scratch

