%define _unpackaged_files_terminate_build 1
%define dist Class-C3-Adopt-NEXT
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: Make NEXT suck less
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Class-C3-Adopt-NEXT-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 14 2010
BuildRequires: perl-Class-C3-XS perl-List-MoreUtils perl-MRO-Compat perl-Module-Install perl-NEXT perl-Test-Exception

%description
This module is intended as a drop-in replacement for NEXT, supporting
the same interface, but using Class::C3 to do the hard work.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision, for Catalyst
