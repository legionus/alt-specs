%define _unpackaged_files_terminate_build 1
%define dist Test-Class
Name: perl-%dist
Version: 0.50
Release: alt1

Summary: Easily create test classes in an xUnit/JUnit style
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Test-Class-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Attribute-Handlers perl-MRO-Compat perl-Module-Build perl-Test-Exception perl(Try/Tiny.pm) perl(Module/Runtime.pm)

%description
Test::Class provides a simple way of creating classes and objects
to test your code in an xUnit style.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.33 -> 0.36

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.33-alt1
- initial build for ALT Linux Sisyphus
