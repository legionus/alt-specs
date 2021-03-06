#
#   - Text::Wrapper -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only -U Text::Wrapper
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-Wrapper
%define m_distro Text-Wrapper
%define m_name Text::Wrapper
%define m_author_id unknown
%define _enable_test 1

Name: perl-Text-Wrapper
Version: 1.05
Release: alt1

Summary: Text-Wrapper - Simple word wrapping routine

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/C/CJ/CJM/Text-Wrapper-%{version}.tar.gz

# Automatically added by buildreq on Mon Jun 06 2005
BuildRequires: perl-devel perl-Module-Build

%description
Text::Wrapper provides simple word wrapping.  It breaks long lines,
but does not alter spacing or remove existing line breaks.  If you're
looking for more sophisticated text formatting, try the
Text::Format module.


%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Text/*

%changelog
* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt2
- fix directory ownership violation
- disable man packaging

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt1
- first build for ALT Linux Sisyphus
