#
#   - Digest::Adler32 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Digest::Adler32
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Digest-Adler32
%define m_distro Digest-Adler32
%define m_name Digest::Adler32
%define m_author_id GAAS
%define _enable_test 1

Name: perl-Digest-Adler32
Version: 0.03
Release: alt1.1.1

Summary: The Adler-32 checksum

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Digest-Adler32/

Packager: Michael Bochkaryov <misha@altlinux.ru>

Source: http://search.cpan.org//CPAN/authors/id/G/GA/GAAS/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Jun 30 2008
BuildRequires: perl-devel

BuildArch: noarch

%description
The "Digest::Adler32" module implements the Adler-32 checksum as
specified in RFC 1950.  The interface provided by this module is
specified in Digest, but no functional interface is provided.

A binary digest will be 4 bytes long.  A hex digest will be 8
characters long.  A base64 digest will be 6 characters long.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Digest/Adler32.pm
%doc README Changes

%changelog
* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1.1.1
- rebuilt with perl 5.12

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
