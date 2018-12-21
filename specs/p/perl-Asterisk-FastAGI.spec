#
#   - Asterisk::FastAGI -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 0.01 Asterisk-FastAGI-0.01.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Asterisk-FastAGI
%define m_distro Asterisk-FastAGI
%define m_name Asterisk::FastAGI
%define m_author_id unknown
%define _enable_test 1

Name: perl-Asterisk-FastAGI
Version: 0.02
Release: alt3.1

Summary: Asterisk-FastAGI - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: %name.tar

# Automatically added by buildreq on Sun Apr 15 2007
BuildRequires: perl-asterisk-perl perl-Module-Install perl-Net-Server

%description
None.

%prep
%setup -c
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Asterisk*
%perl_vendor_autolib/Asterisk*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Dec 10 2008 Denis Smirnov <mithraen@altlinux.ru> 0.02-alt3
- not pack %perl_vendor_archlib

* Mon Oct 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.02-alt2
- fix building

* Sat Nov 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.02-alt1
- upstream update

* Sun Apr 15 2007 Denis Smirnov <mithraen@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus

