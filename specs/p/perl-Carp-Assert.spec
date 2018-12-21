#
#   - Carp::Assert -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Carp::Assert
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Carp-Assert
%define m_distro Carp-Assert
%define m_name Carp::Assert
%define m_author_id unknown
%define _enable_test 1

Name: perl-Carp-Assert
Version: 0.21
Release: alt1

Summary: Carp-Assert - executable comments

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Carp-Assert-%{version}.tar.gz

# Automatically added by buildreq on Sat Sep 24 2005 (-bi)
BuildRequires: perl-devel

%description
Carp::Assert is intended for a purpose like the ANSI C library
assert.h.  If you're already familiar with assert.h, then you can
probably skip this and go straight to the FUNCTIONS section.

Assertions are the explict expressions of your assumptions about the
reality your program is expected to deal with, and a declaration of
those which it is not.  They are used to prevent your program from
blissfully processing garbage inputs (garbage in, garbage out becomes
garbage in, error out) and to tell you when you've produced garbage
output.  (If I was going to be a cynic about Perl and the user nature,
I'd say there are no user inputs but garbage, and Perl produces
nothing but...)

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Carp/

%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt2
- fix directory ownership violation

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- first build for ALT Linux Sisyphus
