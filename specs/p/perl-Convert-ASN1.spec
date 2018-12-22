%define dist Convert-ASN1
Name: perl-%dist
Version: 0.27
Release: alt1

Summary: Perl ASN.1 parser module
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GB/GBARR/Convert-ASN1-%{version}.tar.gz

BuildArch: noarch

# due to Convert::ASN1::os2ip()
Requires: perl-Math-BigInt

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode perl-Math-BigInt perl-devel

%description
Convert::ASN1 will parse ASN.1 descriptions and will encode from
and decode to perl data structures using a hierarchy of references.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog
%dir	%perl_vendor_privlib/Convert
	%perl_vendor_privlib/Convert/ASN1.pm
%doc	%perl_vendor_privlib/Convert/ASN1.pod
%dir	%perl_vendor_privlib/Convert/ASN1
	%perl_vendor_privlib/Convert/ASN1/*.pm

%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.22-alt2
- disabled build dependency on perl-Module-Install

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.21 -> 0.22

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.19 -> 0.21

* Wed Apr 20 2005 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.18 -> 0.19

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 0.18-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Thu Feb 05 2004 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 1.18

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.16-alt1.1
- fix spec

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.16-alt1
- rebuild with new perl

* Thu Jan 24 2002 Grigory Milev <week@altlinux.ru> 0.15-alt1
- new version released

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 0.14-alt1
- New version released.

* Mon Sep 03 2001 Grigory Milev <week@altlinux.ru> 0.13-alt1
- New version released.

* Wed Aug 01 2001 Grigory Milev <week@altlinux.ru> 0.11-alt1
- First build for Sisyphus
