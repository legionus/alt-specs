# TODO: there is exist driver registration utility, add some macros?
# odbcinst -i -d -f template

Name: mysql-connector-odbc
Version: 5.3.11
Release: alt1

Summary: MySQL Connector/ODBC - ODBC driver for MySQL

# exceptions allow library to be linked with most open source SW,
# not only GPL code.
License: %gpl2only
Group: System/Libraries
Url: https://github.com/mysql/mysql-connector-odbc
# https://dev.mysql.com/doc/connector-odbc/en/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: odbc.ini
Source2: odbcinst.ini

Patch1: %name-5.3.11-alt-rpath.patch
Patch2: %name-5.3.11-fix_build.patch
Patch3: %name-5.3.11-alt-aarch64.patch


BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Aug 08 2018
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libncurses-devel libstdc++-devel libtinfo-devel libunixODBC-devel-compat python-base python-modules python3 python3-base python3-dev ruby
BuildRequires: cmake gcc-c++ glibc-devel-static libmysqlclient20-devel libsasl2-devel libssl-devel libunixODBC-devel

%description
MySQL Connector/ODBC   allows you to connect to MySQL database
servers using ODBC, the Open Database Connectivity abstraction
layer which is understood by a variety of database tools that
cannot talk to MySQL databases directly.

Connector/ODBC documentation for detailed installation and
setup instructions can be found at 
  https://dev.mysql.com/doc/connector-odbc/en/


%prep
%setup
%patch0 -p1

%patch1
%patch2 -p1
%patch3

%build
cmake -G "Unix Makefiles" \
    -DWITH_UNIXODBC=1 \
    -DBUNDLE_DEPENDENCIES=false \
    -DHAVE_STRUCT_TIMESPEC=1 \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DDISABLE_GUI=1 \
    -DRPM_BUILD=1

%make_build

%install
%makeinstall_std

install -m 0644 %SOURCE1 odbc.ini
install -m 0644 %SOURCE2 odbcinst.ini
sed -e 's#@@lib@@#%{_libdir}#g' -i odbcinst.ini

rm -f %buildroot/%_prefix/{ChangeLog,README.txt,LICENSE.txt}

%files
%doc ChangeLog README.txt LICENSE.txt odbcinst.ini odbc.ini
%_bindir/myodbc-installer
%_libdir/lib*
%exclude %_prefix/test

%changelog
* Wed Aug 15 2018 Nikolay A. Fetisov <naf@altlinux.org> 5.3.11-alt1
- New version
- Restored from orphaned

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.8-alt1.1
- Fixed build

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.8-alt1
- 5.1.8

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt2
- fix build

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt1
- new version

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.4r1107-alt1
- new version 5.1.4

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt1
- rebuild with libMySQL 5.0
- add libssl-devel to build requires

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt0.1
- initial build for ALT Linux Sisyphus
- disable GUI
- build without MULTI_RESULTS support

