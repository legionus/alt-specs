#
#   - Class::CGI -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug --version 0.20 Class::CGI
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-CGI
%define m_distro Class-CGI
%define m_name Class::CGI
%define m_author_id unknown
%define _enable_test 1

Name: perl-Class-CGI
Version: 0.20
Release: alt2.1

Summary: %m_name - fetch objects from your CGI object

License: Artistic and GPL
Group: Development/Perl
Url: http://search.cpan.org/dist/Class-CGI/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/O/OV/OVID/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Aug 04 2008 (-bi)
BuildRequires: perl-CGI-Simple perl-Config-Std perl-HTML-Parser perl-Module-Build perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage

%description
For small CGI scripts, it's common to get a parameter, untaint it, pass it to
an object constructor and get the object back. This module would allow one to
to build Class::CGI handler classes which take the parameter value,
automatically perform those steps and just return the object. Much grunt work
goes away and you can get back to merely pretending to work.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class*
%doc Changes README

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt2
- fix directory ownership violation

* Mon Aug 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt1
- first build for ALT Linux Sisyphus

