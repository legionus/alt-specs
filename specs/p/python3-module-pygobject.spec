%define major 2.28
%define oname pygobject
%define gtk_api_ver 2.0
%def_disable introspection

Name: python3-module-pygobject
Version: %major.6
Release: alt10.1.1.1
Summary: Python 3 bindings for GObject

License: LGPL
Group: Development/Python3
Url: http://www.pygtk.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/%oname/%major/%oname-%version.tar

%add_python_lib_path  %python3_sitelibdir/gtk-%gtk_api_ver
%add_findprov_lib_path %python3_sitelibdir/gtk-%gtk_api_ver/gtk
%{?_enable_introspection:%add_findprov_lib_path %python3_sitelibdir/gtk-%gtk_api_ver/gi}
%{?_enable_introspection:Requires: python-module-pygi = %version-%release}

%define glib_ver 2.28.0

BuildRequires(pre): rpm-build-python3
BuildPreReq: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildRequires: python3-devel python3-module-pycairo-devel python3-module-pycairo python-tools-2to3
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.10.2}

%requires_python3_ABI_for_files %_libdir/libpyglib-2.0-python3.so.0.0.0

%py3_provides scmexpr
# ? python-modules
%add_python_req_skip keyword scmexpr
%add_python3_req_skip _gio

%description
This package provides Python bindings for the GLib, GObject and GIO,
to be used in Python. It is a fairly complete set of bindings,
it's already rather useful, and is usable to write moderately
complex programs.  (see the examples directory for some examples
of the simpler programs you could write).

%package devel
Summary: Development files for %oname
Group: Development/Python3
Requires: %name = %version-%release
Conflicts: python-module-pygobject-devel
AutoReq: yes,nopython
%add_python_req_skip keyword scmexpr

%description devel
Development files for %oname.

%package devel-doc
Summary: Development documentation for %oname
Group: Development/Python3
BuildArch: noarch

%description devel-doc
Development documentation for %oname.

%package -n python-module-pygi
Summary: Python dynamic bindings based on GObject-Introspection
Group: Development/Python3
%{?_enable_introspection:%setup_python_module pygi}
Requires: %name = %version-%release

%description -n python-module-pygi
PyGI is a module which aims to utilize GObject Introspection to
facilitate the creation of Python bindings.

%prep
%setup -q -n %oname-%version

find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +

%build
export PYTHON=python3
%autoreconf
%configure --with-pic --disable-static \
	%{subst_enable introspection}

%make_build

%check
#%%make check

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_includedir/python%_python3_version
mv %buildroot%_includedir/pygtk-%gtk_api_ver %buildroot%_includedir/python%_python3_version/pygtk
%__subst "s|\${includedir}/pygtk-%gtk_api_ver|\${includedir}/python%_python3_version/pygtk|g" %buildroot/%_pkgconfigdir/*.pc

sed -i 's|%_bindir/env python|%_bindir/env python3|' \
	%buildroot%_datadir/pygobject/xsl/fixxref.py

find %buildroot -type f -name '*.py' -exec 2to3 -w '{}' +

%files
%_libdir/libpyglib-2.0-python3*.so.*
%python3_sitelibdir/pygtk.*
%python3_sitelibdir/__pycache__/pygtk.*
%python3_sitelibdir/gobject
%python3_sitelibdir/glib
%dir %python3_sitelibdir/gtk-%gtk_api_ver
%python3_sitelibdir/gtk-%gtk_api_ver/gio

%files devel
#_bindir/py3_pygobject-codegen-2.0
%_libdir/libpyglib-2.0-python3*.so
%_includedir/python%_python3_version/pygtk
%python3_sitelibdir/gtk-%gtk_api_ver/dsextras.*
%python3_sitelibdir/gtk-%gtk_api_ver/__pycache__/dsextras.*
%_datadir/pygobject/2.0
%_datadir/pygobject/xsl
%_pkgconfigdir/pygobject-2.0.pc
%doc README AUTHORS NEWS examples

%exclude %python3_sitelibdir/*/*.la

%files devel-doc
%_datadir/gtk-doc/html/pygobject/

%if_enabled introspection
%files -n python-module-pygi
%python3_sitelibdir/gi/
%exclude %python3_sitelibdir/gi/*.la
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.28.6-alt10.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.28.6-alt10.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Fri Apr 01 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.28.6-alt10.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 2.28.6-alt10
- Added new macro for python3.5

* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.28.6-alt9
- Python3.5 adaptations.

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 2.28.6-alt8
- Spec cleanup

* Wed Feb 24 2016 Denis Medvedev <nbr@altlinux.org> 2.28.6-alt7
- added  xargs to find  when 2to3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.6-alt6
- Don't ignore errors when 2to3 & sed run

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.6-alt5
- Fixed build

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 2.28.6-alt4.1
- Rebuild with Python-3.3

* Sat May 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.6-alt4
- Built for Python 3

* Fri Apr 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt3
- updated to latest pygobject-2-28 (42d01f0)
- no more libpython dependencies

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.28.6-alt2.1
- Rebuild with Python-2.7

* Sun Sep 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt2
- disabled introspection support

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Mon Apr 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1
- fixed link

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Mar 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Sat Feb 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- removed useless link patch

* Wed Dec 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.27.0-alt1
- 2.27.0

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- rebuild for update dependencies

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- 2.21.5

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt3
- build with libffi support

* Mon Jul 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt2
- requires python-module-pygi if introspection support enabled (closes
  #23720)

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.3-alt1
- 2.21.3

* Wed Jun 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.2-alt1
- 2.21.2

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.1-alt1
- new version
- introspection support temporarily disabled

* Fri Dec 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.0-alt1
- 2.21.0

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.20.0-alt2.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt2
- new gir{,-devel} packages

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.0-alt1
- 2.19.0
- new devel-doc noarch package

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.15.4-alt1
- 2.15.4
- updated buildreqs
- updated patch0

* Sun Jul 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.2-alt1
- new version 2.13.2 (with rpmrb script)

* Thu May 17 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.1-alt1
- new version 2.13.1 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.3-alt1
- new version 2.12.3 (with rpmrb script)

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.2-alt1
- fix linking, packing - applied patches from Valery Inozemtsev (fix bug #10771)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.2-alt0.1
- new version 2.12.2 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.4-alt0.1
- new version 2.11.4 (with rpmrb script)

* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt0.1
- new version
- remove broken TMPDIR definition from Makefile!

* Tue Jul 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt0.1
- new version 2.10.1 (with rpmrb script)

* Mon Jul 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt0.1
- new version 2.11.0 (with rpmrb script)

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1
- add conflicts to old pygtk in -devel package

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version (2.9.1)

* Sat Feb 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt0.1
- initial build for ALT Linux Sisyphus
