BuildRequires: perl(Module/Build.pm)
%define dist Class-ErrorHandler
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Base class for error handling
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TO/TOKUHIROM/Class-ErrorHandler-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-devel

%description
Class::ErrorHandler provides an error-handling mechanism that's generic
enough to be used as the base class for a variety of OO classes.
Subclasses inherit its two error-handling methods, error and errstr,
to communicate error messages back to the calling program.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Class

%changelog
* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt3
- disabled build dependency on perl-Module-Install

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt2
- rebuilt

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision
