%define _unpackaged_files_terminate_build 1
%define dist Module-Runtime
Name: perl-%dist
Version: 0.016
Release: alt1

Summary: Runtime module handling
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Module-Build perl-Params-Classify perl-Test-Pod perl-Test-Pod-Coverage perl-Math-BigInt

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module

%changelog
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Tue Oct 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt2
- added perl-Math-BigInt builddep

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt1
- 0.011 -> 0.013

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.011-alt1
- initial revision
