%define _name bytesize
# pocketlint required
%def_disable check

Name: lib%_name
Version: 1.4
Release: alt2

Summary: A library for working with sizes in bytes
Group: System/Libraries
License: LGPLv2+
Url: https://github.com/storaged-project/%name

Source: %url/releases/download/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-python rpm-build-python3

BuildRequires: gtk-doc
BuildRequires: glib2-devel libgmp-devel libmpfr-devel libpcre-devel
BuildRequires: python-devel python3-devel

%description
The %name is a C library that facilitates work with sizes in bytes.
Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files and pkg-config files needed for
development with the %name library.

%package -n python-module-%_name
Summary: Python 2 bindings for %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%_name
This package contains Python 2 bindings for %name making the use of
the library from Python 2 easier and more convenient.

%package -n python3-module-%_name
Summary: Python 3 bindings for %name
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-%_name
This package contains Python 3 bindings for %name making the use of
the library from Python 3 easier and more convenient.

%prep
%setup -n %name-%version

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags libpcre`"
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make check

%files -f %name.lang
%_libdir/%name.so.*
%doc README.md LICENSE
#%doc NEWS*

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_datadir/gtk-doc/html/%name/

%files -n python-module-%_name
%python_sitelibdir/%_name/*

%files -n python3-module-%_name
%python3_sitelibdir/%_name/*


%changelog
* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt2
- moved %%find_lang to proper section

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Fri Oct 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Thu Sep 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Thu Dec 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Mon Oct 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- first build for Sisyphus

