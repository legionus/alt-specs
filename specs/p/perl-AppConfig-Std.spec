%define dist AppConfig-Std
Name: perl-%dist
Version: 1.10
Release: alt1

Summary: Subclass of AppConfig that provides standard options
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NE/NEILB/AppConfig-Std-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-AppConfig perl-Pod-Parser perl-devel

%description
AppConfig::Std is a Perl module that provides a set of standard
configuration variables and command-line switches.  It is implemented
as a subclass of AppConfig; AppConfig provides a general mechanism for
handling global configuration variables.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/AppConfig

%changelog
* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 1.07-alt2
- fixed unpackaged directory

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1.1
- rebuilt with perl 5.12

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt1
- initial build for ALT Linux Sisyphus
