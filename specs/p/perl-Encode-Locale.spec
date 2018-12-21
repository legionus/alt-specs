%define _unpackaged_files_terminate_build 1
%define dist Encode-Locale
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: Determine the locale encoding
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GAAS/Encode-Locale-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012 (-bi)
BuildRequires: perl-Encode perl-devel

%description
The purpose of this Perl module is try determine what encodings
should be used when interfacing to various external interfaces.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Encode

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.02 -> 1.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt2
- rebuilt as plain src.rpm

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.01 -> 1.02

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision
