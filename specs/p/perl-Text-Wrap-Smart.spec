%define _unpackaged_files_terminate_build 1
#
#   - Text::Wrap::Smart -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 0.6 Text::Wrap::Smart
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-Wrap-Smart
%define m_distro Text-Wrap-Smart
%define m_name Text::Wrap::Smart
%define m_author_id SCHUBIGER
%define _enable_test 1

Name: perl-Text-Wrap-Smart
Version: 0.7
Release: alt1

Summary: Wrap text into chunks of (mostly) equal length

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Text-Wrap-Smart/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/S/SC/SCHUBIGER/Text-Wrap-Smart-%{version}.tar.gz

# Automatically added by buildreq on Wed Jun 04 2008
BuildRequires: perl-Math-BigInt perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-version perl(boolean.pm) perl(Params/Validate.pm)

%description
Text::Wrap::Smart was primarly developed to split an overly long SMS message into chunks of mostly equal size. The distribution's wrap_smart() may nevertheless be suitable for other purposes.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Jun 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.6-alt1
- first build for ALT Linux Sisyphus

