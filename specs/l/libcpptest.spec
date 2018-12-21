%define oname cpptest
Name: libcpptest
Version: 1.1.2
Release: alt1

Summary: CppTest is a unit testing framework for handling automated tests in C++

License: LGPL
Group: System/Libraries
Url: http://cpptest.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%oname/%oname-%version.tar

# Automatically added by buildreq on Sat Mar 07 2009
BuildRequires: gcc-c++

%description
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.
Several output formats are supported and new ones are easily added.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for libspiff.

%prep
%setup -n %oname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS BUGS ChangeLog NEWS README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%{oname}*
%_pkgconfigdir/*

%changelog
* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

