Name: perl-Test-Trap
Version: 0.3.4
Release: alt1

Summary: Test::Trap perl module
Group: Development/Perl
License: Perl

Url: %CPAN Test-Trap
Source: %name-%version.tar

BuildRequires: perl-devel perl-base perl-Module-Build perl-Test-Tester perl-Data-Dump

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Trap*
%doc Changes README

%changelog
* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1
- 0.2.1 -> 0.2.2
- fixed build with Carp >= 1.25

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.1-alt1
- initial build
