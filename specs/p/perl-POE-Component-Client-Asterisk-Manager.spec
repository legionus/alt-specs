#
#   - POE::Component::Client::Asterisk::Manager -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug POE::Component::Client::Asterisk::Manager
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module POE-Component-Client-Asterisk-Manager
%define m_distro POE-Component-Client-Asterisk-Manager
%define m_name POE::Component::Client::Asterisk::Manager
%define m_author_id unknown
%define _enable_test 1

Name: perl-POE-Component-Client-Asterisk-Manager
Version: 0.08
Release: alt1.1.1

Summary: Event-based Asterisk / Aefirion Manager Client

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/POE-Component-Client-Asterisk-Manager/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/X/XA/XANTUS/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Aug 04 2008 (-bi)
BuildRequires: perl-POE perl-Test-Pod

%description
POE::Component::Client::Asterisk::Manager is an event driven Asterisk manager
client.  This module should also work with Aefirion.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc README Changes examples
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Aug 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08-alt1
- first build for ALT Linux Sisyphus

