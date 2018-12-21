%def_enable python3

Name: cracklib
Version: 2.9.6
Release: alt1.1.1

Summary: A password-checking library.
License: %lgpl2plus
Group: System/Libraries
Url: https://github.com/%name/%name

Source: https://github.com/%name/%name/releases/download/%name-%version/%name-%version.tar.gz

Requires: %name-utils = %version-%release

BuildRequires: rpm-build-licenses python-devel libX11-devel libICE-devel
BuildRequires: zlib-devel
%{?_enable_python3:BuildRequires: rpm-build-python3 python3-devel}

%package utils
Summary: The CrackLib utilities for the build dictionaries.
Group: System/Libraries
Requires: %name = %version-%release

%package devel
Summary: %name link library & header file
Group: Development/C
Requires: %name = %version-%release

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python
Requires: %name = %version-%release

%package -n python3-module-%name
Summary: Python3 module of %name
Group: Development/Python
Requires: %name = %version-%release

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop
users from choosing passwords which would be easy to guess. CrackLib
performs certain tests:

* It tries to generate words from a username and gecos entry and
  checks those words against the password;
* It checks for simplistic patterns in passwords;
* It checks for the password in a dictionary.

CrackLib is actually a library containing a particular
C function which is used to check the password, as well as
other C functions. CrackLib is not a replacement for a passwd
program; it must be used in conjunction with an existing passwd
program.

Install the %name package if you need a program to check users'
passwords to see if they are at least minimally secure. If you
install CrackLib, you'll also want to install the %name-words
package.

%description devel
The %name devel package include the needed library link and
header files for development.

%description utils
The %name-utils package includes the utilities necessary to
create new dictionaries for Cracklib.

%description -n python-module-%name
This package includes Python module for Cracklib.

%description -n python3-module-%name
This package includes Python3 module for Cracklib.

%prep
%setup -n %name-%version
%setup -D -c -n %name-%version
mv %name-%version py3build

%build
%autoreconf
%configure \
	--disable-static
%make_build

%if_enabled python3
pushd py3build
export PYTHON=python3
export am_cv_python_version=%__python3_version%_python3_abiflags
%autoreconf
%configure \
	--disable-static \
	--with-x
%make_build
popd
%endif

%install
%makeinstall_std

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_enabled python3
pushd py3build
%makeinstall_std

%ifarch x86_64
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
popd
%endif

# create words database
touch %buildroot%_datadir/%name/pw_dict.{hwm,pwd,pwi}

cat > %name.filetrigger << _EOF_
#!/bin/sh -e

dir=%_datadir/%name
grep -qs '^'\$dir'' && %_sbindir/%name-format \$dir/%{name}* | %_sbindir/%name-packer \$dir/pw_dict >/dev/null ||:
_EOF_

install -pD -m 755 %name.filetrigger %buildroot%_rpmlibdir/%name.filetrigger

%find_lang cracklib

%files -f %name.lang
%_libdir/*.so.*
%_datadir/%name/
%_rpmlibdir/%name.filetrigger
%doc AUTHORS ChangeLog NEWS README*

%files devel
%_includedir/*
%_libdir/*.so

%files utils
%_sbindir/*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*.la

%if_enabled python3
%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.la
%endif

%changelog
* Fri Mar 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9.6-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.6-alt1
- 2.9.6

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.5-alt1
- 2.9.5
- python3-module subpackage

* Sat Dec 07 2013 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- 2.9.1
- fixed filetrigger (ALT #29637)

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1
- 2.9.0

* Mon Jan 07 2013 Yuri N. Sedunov <aris@altlinux.org> 2.8.22-alt1
- 2.8.22
- prepared for build of python3-module-%%name subpackage

* Wed Jul 11 2012 Yuri N. Sedunov <aris@altlinux.org> 2.8.19-alt1
- 2.8.19
- created empty words database in %install, implemented posttrans filetrigger
  for automatic update words database (ALT #27519).

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8.18-alt1.1
- Rebuild with Python-2.7

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.18-alt1
- Version 2.8.18

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.13-alt3
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.13-alt2
- Rebuilt for soname set-versions

* Wed Dec 24 2008 Alexey Rusakov <ktirf@altlinux.org> 2.8.13-alt1
- new version (2.8.13)
- added Packager tag
- specified the license more explicitly (GPL -> %gpl2plus)
- made download URL mirror-agnostic
- removed no more needed ldconfig calls in post/postun scripts

* Sat Mar 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.8.10-alt1
- new version (2.8.10)
- fixed Url

* Wed May 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.9-alt1
- new version (2.8.9)

* Wed Mar 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- new version adopted for Sisyphus.

* Mon Sep 04 2000 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl13mdk
- RE adaptions

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.7-10mdk
- Devel package.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.7-9mdk
- Fix group.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Strip binaries.
- Add %%defattr

* Sun May  2 1999 Bernhard Rosenkr�nzer <bero@mandrakesoft.com>
- s/V'erification/Verification in french translation - I know it's a
  spelling mistake, but rpm 3.0 doesn't like accents in Summary: lines. :/

* Thu Apr 10 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- French Translation

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
- add de locale

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.7
- build shared libraries

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added -fPIC

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- basic spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

