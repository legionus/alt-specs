#
#   - LEOCHARRE::CLI2 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' --no-depchk --url http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-CLI2-1.16.tar.gz http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-CLI2-1.16.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module LEOCHARRE-CLI2
%define m_distro LEOCHARRE-CLI2
%define m_name LEOCHARRE::CLI2
%define m_author_id unknown
%define _disable_test 1

Name: perl-LEOCHARRE-CLI2
Version: 1.16
Release: alt2

Summary: Some quick help for writing cli scripts

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-CLI2-1.16.tar.gz

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/%m_distro-%version.tar.gz
Patch: LEOCHARRE-CLI2-1.16-alt-perl522.patch

# Automatically added by buildreq on Fri Nov 18 2011
BuildRequires: perl-Devel-Symdump perl-String-ShellQuote perl-YAML perl-devel

%description
Some quick help for writing cli scripts.
Forces by default that -h triggers help, that -d triggers debug.
Automates help, debug, etc.
If you use LEOCHARRE::CLI2, we alter the OPTIONS automatically.
Also we automatically generate HELP.

%prep
%setup -n %m_distro-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/LEOCHARRE/*

%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt2
- NMU: fixed build

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- initial build for ALT Linux Sisyphus

