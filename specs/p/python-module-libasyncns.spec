Name: python-module-libasyncns
Version: 0.7.1
Release: alt1

Summary: libasyncns bindings for Python
License: LGPLv2.1
Group: Development/Python
Url: http://launchpad.net/libasyncns-python/

Source: libasyncns-python-%version.tar
Patch1: %name-%version-alt-glibc.patch

BuildRequires: python-devel libasyncns-devel >= 0.4

%description
Python binding for the libasyncns asynchronous name service query.

%prep
%setup -n libasyncns-python-%version
%patch1 -p2
subst '/CFLAGS.*PYTHON_CONFIG/s,=.*,=-isystem %python_includedir,' Makefile
subst '/LDFLAGS.*PYTHON_CONFIG/s,=.*,=-lpython%__python_version,' Makefile

%build
%make
%make doc

%install
install -D libasyncns.so %buildroot%python_sitelibdir/libasyncns.so

%files
%python_sitelibdir/libasyncns.so
%doc README test doc/libasyncns.html

%changelog
* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1
- Updated to upstream version 0.7.1.
- Fixed build with modern glibc.

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.1
- Rebuilt with python 2.6

* Thu Jan 01 2009 Alexander Myltsev <avm@altlinux.org> 0.7-alt1
- New version.

* Sun Aug 03 2008 Alexander Myltsev <avm@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
