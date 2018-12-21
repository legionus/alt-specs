%define _unpackaged_files_terminate_build 1
%define dist Module-Pluggable
Name: perl-%dist
Version: 5.2
Release: alt1

Summary: Automatically give your module the ability to have plugins
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-devel perl-Module-Build

%description
Provides a simple but, hopefully, extensible way of having 'plugins'
for your module.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module
%perl_vendor_privlib/Devel

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.8-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 4.3-alt1
- 3.9 -> 4.3

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 3.9-alt2
- noarch

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.9-alt1.1
- rebuilt with perl 5.12

* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9 (with rpmrb script)
- build as noarch, fix spec

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.97-alt1
- fix directory ownership violation

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.97-alt0.1
- new version 2.97 (with rpmrb script)

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.95-alt1
- new version

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- first build for ALT Linux Sisyphus
