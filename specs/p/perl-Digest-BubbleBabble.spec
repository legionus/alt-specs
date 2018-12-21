#
#   - Digest-BubbleBabble -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Digest::BubbleBabble
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Digest-BubbleBabble
%define m_distro Digest-BubbleBabble
%define m_name Digest-BubbleBabble
%define m_author_id unknown
%define _enable_test 1

Name: perl-Digest-BubbleBabble
Version: 0.02
Release: alt1

Summary: Create bubble-babble fingerprints

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Mikhail Pokidko <pma@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BT/BTROTT/Digest-BubbleBabble-0.02.tar.gz

# Automatically added by buildreq on Wed Nov 15 2006
BuildRequires: perl-devel

%description
*Digest::BubbleBabble* takes a message digest (generated by
either of the MD5 or SHA-1 message digest algorithms) and creates
a fingerprint of that digest in "bubble babble" format.
Bubble babble is a method of representing a message digest
as a string of "real" words, to make the fingerprint easier
to remember. The "words" are not necessarily real words, but
they look more like words than a string of hex characters.

Bubble babble fingerprinting is used by the SSH2 suite
(and, consequently, by *Net::SSH::Perl*, the Perl SSH
implementation) to display easy-to-remember key fingerprints.
The key (a DSA or RSA key) is converted into a textual form,
digested using *Digest::SHA1*, and run through *bubblebabble*
to create the key fingerprint.

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
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Sep 05 2008 Mikhail Pokidko <pma@altlinux.org> 0.01-alt2
- sisyphus_check fixes

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
