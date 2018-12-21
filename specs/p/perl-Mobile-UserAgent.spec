#
#   - Mobile::UserAgent -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug Mobile::UserAgent
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Mobile-UserAgent
%define m_distro Mobile-UserAgent
%define m_name Mobile::UserAgent
%define m_author_id unknown
%define _enable_test 1

Name: perl-Mobile-UserAgent
Version: 1.05
Release: alt1.1

Summary: Mobile user agent string parsing class

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Mobile-UserAgent/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/C/CM/CMANLEY/%m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Sep 13 2008 (-bi)
BuildRequires: perl-Class-Singleton perl-devel

%description
Parses a mobile user agent string into it's basic constituent parts, the
most important being vendor and model.

One reason for doing this would be to use this information to lookup
vendor-model specific device characteristics in a database. You can use also
use user agent profiles to do this (for which I've developed other classes),
but not all mobile phones have these, especially the older types.
Another reason would be to detect if the visiting client is a mobile handset.

Only real mobile user-agent strings can be parsed succesfully by this class.
Most WAP emulators are not supported because they usually don't use the same
user-agent strings as the devices they emulate.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mobile*
%doc Changes README etc

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.05-alt1
- first build for ALT Linux Sisyphus
