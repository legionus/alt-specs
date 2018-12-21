BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
Name: perl-TOML
Version: 0.97
Release: alt1

Summary: Parser for Tom's Obvious, Minimal Language.
Group: Development/Perl
License: Perl

Url: %CPAN TOML
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Text/Balanced.pm) perl(TOML/Parser.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/TOML*
%doc Changes README.md

%changelog
* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Tue Jan 14 2014 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1
- initial build for ALTLinux

