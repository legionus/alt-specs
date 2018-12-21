Name: perl-Lingua-JA-Regular-Unicode
Version: 0.13
Release: alt1

Summary: Lingua::JA::Regular::Unicode - convert japanese chars
Group: Development/Perl
License: Perl

Url: %CPAN Lingua-JA-Regular-Unicode
# Cloned from git://github.com/tokuhirom/p5-lingua-ja-regular-unicode.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build-Tiny perl-Test-Base perl-Test-Perl-Critic perl-Text-TestBase

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/Lingua/JA/Regular/Unicode*
%doc Changes LICENSE

%changelog
* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Tue Oct 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.09 -> 0.12

* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- 0.07 -> 0.09

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- 0.07

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
