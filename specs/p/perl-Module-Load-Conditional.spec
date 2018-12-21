%define _unpackaged_files_terminate_build 1
%define dist Module-Load-Conditional
Name: perl-%dist
Version: 0.68
Release: alt1

Summary: Looking up module information / loading at runtime
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-Conditional-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-Module-CoreList perl-Module-Load perl-Params-Check perl-devel perl(Module/Metadata.pm)

%description
Module::Load::Conditional provides simple ways to query and possibly load
any of the modules you have installed on your system during runtime.

It is able to load multiple modules at once or none at all if one of them
was not able to load. It also takes care of any error checking and so forth.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# avoid self build dependency
rm t/01_Module_Load_Conditional.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Module

%changelog
* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.26 -> 0.44

* Tue May 06 2008 Alexey Tourbin <at@altlinux.ru> 0.26-alt1
- 0.16 -> 0.26

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version 0.16 (with rpmrb script)
- update buildreq, add doc files, fix Url, fix Source URL

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt1
- first build for ALT Linux Sisyphus
