%define apache_confdir %_sysconfdir/httpd2/conf
%define apache_moduledir %_libdir/apache2/modules

Name: apache2-mod_revocator
Version: 1.0.3
Release: alt4

Summary: Apache 2.0 module that lets the user configure remote Certificate Revocation Lists

License: Apache 2.0
Group: System/Servers
Url: http://port389.org/

Source: %name-%version.tar
Source1: revocator.conf
Source2: revocator.load
Patch: %name-include-alt.patch

# Automatically added by buildreq on Tue Jul 20 2010
BuildRequires: apache2-devel apache2-httpd-worker gcc-c++ libnss-devel-static mozldap-devel
Provides: mod_revocator

%description
This Apache module lets the user configure remote Certificate Revocation Lists (CRLs)
to be downloaded and installed automatically on a regular
basis without restarting the server. This helps ensure that the CRLs are
kept up-to-date with minimal effort. The module can also bring the server
down if the CRL expires and a new one cannot be obtained.

%prep
%setup
%patch -p1
%autoreconf

%build
./configure --with-apr-config --with-apxs=%apache2_apxs \
            --with-ldapsdk-inc=/usr/include/mozldap --with-ldapsdk-lib=%_libdir \
            --with-nss-lib=%_libdir --with-nss-inc=/usr/include/nss/
%make

%install
mkdir -p %buildroot/%apache_moduledir
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_libdir
mkdir -p %buildroot%apache_confdir/mods-available/
install -m 755 .libs/libmodrev.so %buildroot/%apache_moduledir/mod_rev.so

install -m 755 .libs/librevocation.so.*.*.* %buildroot/%_libdir/
# install missing symlink (was giving no-ldconfig-symlink rpmlint errors)
/sbin/ldconfig -n %buildroot/%_libdir/

install -m 755 ldapget %buildroot/%_bindir
install -m 644 %SOURCE1 %buildroot%apache_confdir/mods-available/
install -m 644 %SOURCE2 %buildroot%apache_confdir/mods-available/

%files
%apache_moduledir/mod_rev.so
%_bindir/ldapget
%apache_confdir/*
%_libdir/librevocation*.so.1*
%apache2_moduledir/*.so
%doc docs/mod_revocator.html README

%changelog
* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt4
- cleanup spec, fix libs packing (ALT bug 35138)

* Fri Apr 29 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.3-alt3
- rebuild with apache-2.4

* Mon Feb 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt2
- Fix build

* Tue Jul 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1
- Updated to 1.0.3

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- Updated to 1.0.2

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2
- Fedora-DS 1.1 Final release

* Tue Jul 10 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.20070710
- New CVS snapshot 20070710 of Fedora-DS (version change only for mod_revocator)
- Spec cleanup

* Mon Jun 25 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.20070625
- New Fedora DS upstream

* Thu Jun 14 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- New upstream

* Fri Jun 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt0
- Initial

* Thu Nov  3 2005 Richard Megginson <rmeggins@redhat.com> - 1.0
- Initial version
