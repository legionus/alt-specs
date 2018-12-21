%define m_distro Check-ISA
Name: perl-Check-ISA
Version: 0.09
Release: alt1
Summary: Check::ISA perl module

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nuffin/Check-ISA/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Sub-Exporter perl-Test-use-ok

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Check/ISA*
%doc Changes 

%changelog
* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
