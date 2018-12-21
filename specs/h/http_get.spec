# Spec file for http_get utility

Name: http_get

Version: 20180523
Release: alt1.1

Summary: utility to fetch an HTTP/HTTPS URL

License: %bsdstyle
Group: Networking/WWW
URL: http://acme.com/software/http_get/


BuildRequires(pre): rpm-build-licenses

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-alt-20050629-enable_ssl.patch

AutoReqProv: yes

# Automatically added by buildreq on Sat May 24 2008
BuildRequires: libssl-devel

%description
Http_get fetches an HTTP URL and dumps the contents to stdout.
It can do HTTPS fetches as well.

%prep
%setup
%patch0

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_man1dir

install -m 0755 %name %buildroot%_bindir/
install -m 0644 %name.1 %buildroot%_man1dir/

%files
%doc README

%_bindir/%name
%_man1dir/*

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 20180523-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 20180523-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 20160309-alt1
- New version

* Thu Sep 18 2014 Nikolay A. Fetisov <naf@altlinux.ru> 20140814-alt1
- New version

* Wed Jun 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 20100619-alt1
- New version

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 20050629-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 20050629-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon May 26 2008 Nikolay A. Fetisov <naf@altlinux.ru> 20050629-alt1
- Initial build
