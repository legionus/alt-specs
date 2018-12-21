%def_enable Werror
Name: fossil
Version: 2.7
Release: alt1

Summary: A distributed SCM with bug tracking and wiki
License: %bsdstyle
Group: Development/Other
Url: http://www.fossil-scm.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: zlib-devel libssl-devel libreadline-devel tcl
BuildRequires: libsqlite3-devel >= 3.15.0

Requires: tcllib

%define _unpackaged_files_terminate_build 1

%description
Fossil is a simple, high-reliability, distributed software configuration
management with distributed bug tracking, distributed wiki and built-in
web interface.

%package doc
Summary: Fossil documentation
Group: Development/Documentation

%description doc
Documentation in HTML format for Fossil.

%prep
%setup
%patch -p1

%build
# configure script is not generated by autoconf but by autosetup,
# so don't use %%configure macro
./configure \
	--prefix=%_usr \
	--disable-internal-sqlite \
	--with-openssl=auto
export CFLAGS='%optflags'
%make_build

%install
%makeinstall_std
install -pDm644 fossil.1 %buildroot%_man1dir/fossil.1

%files
%doc COPYRIGHT-BSD2.txt
%_bindir/fossil
%_man1dir/%name.1.*

# Don't package documentation,
# seems like something wrong with it.
#files doc
#doc www

%changelog
* Mon Sep 24 2018 Grigory Ustinov <grenka@altlinux.org> 2.7-alt1
- Updated to 2.7.

* Fri Sep 07 2018 Grigory Ustinov <grenka@altlinux.org> 2.6-alt1
- Updated to 2.6.

* Fri Dec 08 2017 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Updated to 2.4.

* Thu Nov 09 2017 Grigory Ustinov <grenka@altlinux.org> 2.3-alt2
- Add tcllib for passing 1 test, correct use -Werror flag.

* Sat Oct 28 2017 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1
- Updated to 2.3.

* Thu Oct 27 2016 Mikhail Efremov <sem@altlinux.org> 1.36-alt1
- Updated to 1.36.

* Mon Jun 20 2016 Mikhail Efremov <sem@altlinux.org> 1.35-alt1
- Updated to 1.35.

* Thu Nov 12 2015 Mikhail Efremov <sem@altlinux.org> 1.34-alt1
- Updated to 1.34.

* Wed May 27 2015 Mikhail Efremov <sem@altlinux.org> 1.33-alt1
- Updated to 1.33.

* Tue Mar 17 2015 Mikhail Efremov <sem@altlinux.org> 1.32-alt1
- Install man page.
- Updated to 1.32.

* Wed Feb 11 2015 Mikhail Efremov <sem@altlinux.org> 1.30-alt1
- Updated to 1.30.

* Tue Aug 05 2014 Mikhail Efremov <sem@altlinux.org> 1.29-alt1
- Updated to 1.29.

* Tue Feb 11 2014 Mikhail Efremov <sem@altlinux.org> 1.28-alt1
- Updated to 1.28.

* Fri Jan 10 2014 Mikhail Efremov <sem@altlinux.org> 1.27-alt1
- Initial build.

