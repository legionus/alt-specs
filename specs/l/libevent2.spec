%define _name libevent
Name: %{_name}2
Version: 2.0.22
Release: alt2

Summary: An asynchronous event notification library
Group: System/Libraries
License: BSD-style
Url: http://www.monkey.org/~provos/libevent/

# http://www.monkey.org/~provos/libevent-%version-stable.tar.gz
Source: %name-%version.tar
Source1: Makefile.sample
Source2: README.libevent
# git://git.altlinux.org/gears/l/%name.git
Patch: %_name-%version-%release.patch

%def_disable static
BuildRequires: libssl-devel zlib-devel

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached.

libevent is meant to replace the asynchronous event loop found in
event driven network servers.  Currently, libevent supports kqueue(2),
select(2) and epoll(4).

%prep
%setup
%patch -p1

%build
%autoreconf
# force epoll and /dev/epoll support
export haveepoll=yes
%configure %{subst_enable static} --disable-libevent-regress
%make_build

%install
%makeinstall_std

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f") || continue
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%define docdir %_docdir/%name-%version
install -pD -m644 %_sourcedir/Makefile.sample \
	%buildroot%docdir/examples/Makefile
install -p -m644 sample/*.c %buildroot%docdir/examples/
install -pm644 %_sourcedir/README.libevent \
	%buildroot%docdir/README

#Install man
mkdir -p %buildroot%_man3dir
install -p -m644 *.3 %buildroot%_man3dir/

%check
make verify

%files
/%_lib/*.so.*
%dir %docdir
%docdir/README

%changelog
* Mon Sep 03 2018 Alexei Takaseev <taf@altlinux.org> 2.0.22-alt2
- Fix build with openssl 1.1.x
- Disable -devel subpackages
- Disable regress in make check

* Wed Sep 28 2016 Alexei Takaseev <taf@altlinux.org> 2.0.22-alt1
- 2.0.22

* Tue Nov 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.21-alt2
- Update from branch patches-2.0

* Thu Feb 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.21-alt1
- Updated to 2.0.21

* Wed Sep 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.20-alt1
- Updated to 2.0.20

* Mon Jun 11 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.19-alt1
- Updated to 2.0.19

* Sat Mar 31 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.18-alt1
- Updated to 2.0.18

* Sun Mar 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.17-alt1
- Updated to 2.0.17

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.16-alt1
- Updated to 2.0.16

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.15-alt1.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.15-alt1
- Updated to 2.0.15.

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.14-alt1
- Updated to 2.0.14.

* Sun Jul 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.12-alt2
- Updated patches-2.0
- Fix build for network restriction in hasher

* Tue Jun 14 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.12-alt1
- Updated to 2.0.12-12-gb031adf.
- Packaged libevent_openssl.
- Restricted list of global symbols exported by libraries.

* Sun Feb 06 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.10-alt1
- Updated to 2.0.10.
- Update spec accord SharedPolicy

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3b-alt3
- Rebuilt for soname set-versions.

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b-alt2.1
- Rebuilt with python 2.6

* Thu Nov 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1.3b-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3b-alt1
- Updated to 1.3b.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1b-alt1
- Updated to 1.1b.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1a-alt2
- Made libevent.map autogenerated based on installed header files.

* Sun Mar 25 2007 Fr. Br. George <george@altlinux.ru> 1.1a-alt1.1
- NMU: automatic map generation

* Sun Oct 30 2005 LAKostis <lakostis at altlinux.ru> 1.1a-alt1
- Updated to 1.1a.
- Updated patches.
- Force epoll and /dev/epoll support.
- Update description.

* Mon Aug 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0c-alt2
- Restricted list of global symbols exported by the library.
- Fixed typos in manual page.

* Mon Apr 04 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0c-alt1
- Updated to 1.0c.
- Updated patches.

* Tue Mar 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0b-alt2
- Relocated shared library from %_libdir to /%_lib (fixes #6156).

* Sun Feb 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0b-alt1
- Initial revision.
