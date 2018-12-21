Name: gnulib
Version: 0.1.1213.683b6
Release: alt2

Summary: GNU Portability Library
License: Freely distributable
Group: Development/C
BuildArch: noarch
Url: http://www.gnu.org/software/gnulib/
Source: %name-%version.tar
Patch1: gnulib-alt-utimens.patch
Patch2: gnulib-alt-mktime-internal.patch
Patch3: gnulib-upstream-parse-datetime-make-it-standalone-no-changelog.patch
AutoReqProv: no
BuildRequires: gnu-config makeinfo

%description
Gnulib is intended to be the canonical source for most of the important
"portability" and/or common files for GNU projects.  These are files
intended to be shared at the source level; Gnulib is not a typical
library meant to be installed and linked against.  Thus, unlike most
projects, Gnulib does not normally generate a source tarball
distribution; instead, developers grab modules directly from the
source repository.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

install -pm755 %_datadir/gnu-config/config.{guess,sub} build-aux/
# Thanks to USE_POSIX_THREADS_WEAK feature, we have to link
# tests with @LIBMULTITHREAD@ in --no-as-needed mode.
# Starting with commit v0.1-211-gc76f7ed, gnulib sets LIBMULTITHREAD
# to -pthread instead of -lpthread, and gcc -Wl,--no-as-needed does not apply
# to gcc -pthread.
grep -lZ '^test_.*@LIBMULTITHREAD@' modules/*-tests |
	xargs -r0 sed -i 's/^\(test_[^ +=]\+\)\(_LDADD.*\)@LIBMULTITHREAD@\(.*\)/\1\2-lpthread\3\n\1_LDFLAGS = -Wl,--no-as-needed/' --

%build
make info

%install
mkdir -p %buildroot{%_bindir,%_infodir,%_datadir/%name}
cp -a * %buildroot%_datadir/%name/
for f in check-module gnulib-tool; do
	ln -s $(relative %_datadir/%name/$f %_bindir/) %buildroot%_bindir/
done
mv %buildroot%_datadir/%name/doc/*.info %buildroot%_infodir/

%files
%_bindir/*
%_infodir/*
%_datadir/%name/

%changelog
* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1213.683b6-alt2
- Fixed includes for new toolchain

* Sun Mar 26 2017 Dmitry V. Levin <ldv@altlinux.org> 0.1.1213.683b6-alt1
- v0.1-1209-g24b3216 -> v0.1-1213-g683b607.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 0.1.1209.24b32-alt1
- v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Wed Oct 07 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.585.2fda85-alt2
- Hacked forced mktime replacement out of mktime-internal module.

* Tue Oct 06 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.585.2fda85-alt1
- Updated to gnulib snapshot v0.1-585-g2fda85e.

* Mon May 25 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.443.875ec93-alt1
- Updated to gnulib snapshot v0.1-443-g875ec93.

* Fri Feb 21 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.114.caf1b31-alt2
- Adjusted link rules to link tests with -lpthread in --no-as-needed mode.

* Wed Feb 19 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.114.caf1b31-alt1
- Updated to gnulib snapshot v0.1-114-gcaf1b31.

* Sat Jan 04 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.58.0f3a662-alt1
- Updated to gnulib snapshot v0.1-58-g0f3a662.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.8061.5191b35-alt1
- Updated to gnulib snapshot v0.0-8061-g5191b35.

* Thu Apr 11 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.7902.92f3a4c-alt1
- Updated to gnulib snapshot v0.0-7902-g92f3a4c.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.7901.076ac82-alt1
- Updated to gnulib snapshot v0.0-7901-g076ac82.

* Tue Nov 20 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7696.fd9f1ac-alt1
- Updated to gnulib snapshot v0.0-7696-gfd9f1ac.

* Mon Oct 29 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7677.4027785-alt2
- Updated to gnulib snapshot v0.0-7677-g4027785.

* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7591.898f143-alt1
- Updated to gnulib snapshot v0.0-7591-g898f143.
- Use config.{guess,sub} from gnu-config.

* Mon Aug 13 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7575.d22f151-alt1
- Updated to gnulib snapshot v0.0-7575-gd22f151.

* Fri Aug 03 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7557.ee60576-alt1
- Updated to gnulib snapshot v0.0-7557-gee60576.

* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7312.7995834-alt1
- Updated to gnulib snapshot v0.0-7312-g7995834.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.6780.bfacc22-alt1
- Updated to gnulib snapshot v0.0-6780-gbfacc22.
- Applied patches originally made for coreutils.

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6125.da1717b-alt1
- Updated to gnulib snapshot v0.0-6125-gda1717b.

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.5864.0f247f9-alt1
- Updated to gnulib snapshot v0.0-5864-g0f247f9.

* Wed Feb 02 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.4800.a036b76-alt1
- Gnulib snapshot v0.0-4800-ga036b76.
