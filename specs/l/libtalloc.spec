%define _unpackaged_files_terminate_build 1
%def_with check
%def_with python3

Name: libtalloc
Version: 2.1.14
Release: alt2
Epoch: 1

Summary: The talloc library

License: LGPLv3+
Group: System/Libraries
Url: http://talloc.samba.org/

Source: http://samba.org/ftp/talloc/talloc-%version.tar.gz
Patch: talloc-alt-fix-python-ldflags.patch

BuildRequires: docbook-dtds docbook-style-xsl libacl-devel libcap-devel python-devel xsltproc

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Group: Development/C
Summary: Developer tools for the Talloc library
Requires: %name = %EVR

%description devel
Header files needed to develop programs that link against the Talloc library.

%package -n python-module-talloc
Group: Development/Python
Summary: Python bindings for the Talloc library
Requires: libtalloc = %EVR

Provides: libpytalloc = %EVR
Obsoletes: libpytalloc < 2.1.14

%description -n python-module-talloc
Python libraries for creating bindings using talloc

%package -n python-module-talloc-devel
Group: Development/Python
Summary: Development libraries for python-module-talloc
Requires: python-module-talloc = %EVR

Provides: libpytalloc-devel = %EVR
Obsoletes: libpytalloc-devel < 2.1.14

%description -n python-module-talloc-devel
Development libraries for python-module-talloc

%if_with python3
%package -n python3-module-talloc
Group: Development/Python3
Summary: Python3 bindings for the Talloc library
Requires: libtalloc = %EVR

%description -n python3-module-talloc
Python 3 libraries for creating bindings using talloc

%package -n python3-module-talloc-devel
Group: Development/Python3
Summary: Development libraries for python3-module-talloc
Requires: python3-module-talloc = %EVR

%description -n python3-module-talloc-devel
Development libraries for python3-module-talloc
%endif

%prep
%setup -n talloc-%version
%patch -p1

%build
%undefine _configure_gettext
%configure	--disable-rpath \
		--disable-rpath-install \
		--bundled-libraries=NONE \
		--builtin-libraries=replace \
%if_with python3
                --extra-python=python3 \
%endif
		--disable-silent-rules
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_datadir/swig/*/talloc.i

%check
make test

%files
%_libdir/libtalloc.so.*

%files devel
%_includedir/talloc.h
%_libdir/libtalloc.so
%_pkgconfigdir/talloc.pc
%_man3dir/talloc.3.*

%files -n python-module-talloc
%_libdir/libpytalloc-util.so.*
%python_sitelibdir/talloc.so

%files -n python-module-talloc-devel
%_includedir/pytalloc.h
%_pkgconfigdir/pytalloc-util.pc
%_libdir/libpytalloc-util.so

%if_with python3
%files -n python3-module-talloc
%_libdir/libpytalloc-util.cpython*.so.*
%python3_sitelibdir/talloc.cpython*.so

%files -n python3-module-talloc-devel
%_includedir/pytalloc.h
%_pkgconfigdir/pytalloc-util.cpython-*.pc
%_libdir/libpytalloc-util.cpython*.so
%endif

%changelog
* Tue Nov 27 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:2.1.14-alt2
- Disable ubt macros due binary package identity changes

* Sun Jul 22 2018 Stanislav Levin <slev@altlinux.org> 1:2.1.14-alt1%ubt
- 2.1.12 -> 2.1.14
- Build package for Python3

* Fri Mar 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:2.1.12-alt1%ubt
- Update to latest release for samba-4.8

* Wed Mar 14 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:2.1.11-alt1%ubt
- Update to latest release for samba-4.7

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.10-alt1%ubt
- Update to release for samba-4.7.0 with tevent-0.9.33

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.9-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.9-alt1%ubt
- Update to release for samba-4.6.0

* Thu Sep 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.8-alt1
- 2.1.8

* Mon Mar 14 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1.6-alt2
- Build 2.1.6

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1.5-alt2
- Downgrade to 2.1.5

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.6-alt1
- 2.1.6

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1
- 2.1.5
- Enable tests

* Fri Oct 23 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Dec 16 2013 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Dec 21 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt2
- disable rpath

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Nov 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt2
- rebuild to gain set-provides

* Tue Jul 06 2010 Ilya Shpigor <elly@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Tue Nov 24 2009 Ilya Shpigor <elly@altlinux.org> 2.0.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep  8 2009 Simo Sorce <ssorce@redhat.com> - 2.0.0-0
- New version from upstream.
- Build also sover 1 compat library to ease packages migration

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Simo Sorce <ssorce@redhat.com> - 1.3.1-1
- Original tarballs had a screw-up, rebuild with new fixed tarballs from
  upstream.

* Tue Jun 16 2009 Simo Sorce <ssorce@redhat.com> - 1.3.1-0
- New Upstream release.

* Wed May 6 2009 Simo Sorce <ssorce@redhat.com> - 1.3.0-0
- First public independent release from upstream
