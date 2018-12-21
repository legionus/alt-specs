#
#   - HTML::TokeParser::Simple -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 3.15 HTML-TokeParser-Simple-3.15.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module HTML-TokeParser-Simple
%define m_distro HTML-TokeParser-Simple
%define m_name HTML::TokeParser::Simple
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-TokeParser-Simple
Version: 3.16
Release: alt1

Summary: HTML-TokeParser-Simple - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/O/OV/OVID/HTML-TokeParser-Simple-%{version}.tar.gz

# Automatically added by buildreq on Thu May 24 2012 (-bb)
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-YAML perl-Devel-Symdump perl-Encode perl-Encode-Locale perl-HTML-Parser perl-HTML-Tagset perl-HTTP-Date perl-HTTP-Message perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-URI perl-devel perl-podlators python-base
BuildRequires: perl-Module-Build perl-Sub-Override perl-Test-Pod perl-Test-Pod-Coverage perl-libwww

%description
None.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 3.16-alt1
- automated CPAN update

* Thu May 24 2012 Denis Smirnov <mithraen@altlinux.ru> 3.15-alt1
- initial build for ALT Linux Sisyphus

