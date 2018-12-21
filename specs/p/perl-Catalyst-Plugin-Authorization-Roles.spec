#
#   - Catalyst::Plugin::Authorization::Roles -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Catalyst-Plugin-Authorization-Roles
%define m_distro Catalyst-Plugin-Authorization-Roles
%define m_name Catalyst::Plugin::Authorization::Roles
%define m_author_id NUFFIN
%def_enable test

Name: perl-Catalyst-Plugin-Authorization-Roles
Version: 0.09
Release: alt1

Summary: %m_name - Role based authorization for Catalyst

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Catalyst-Plugin-Authorization-Roles/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Authorization-Roles-0.09.tar.gz

# Automatically added by buildreq on Tue Apr 20 2010 (-bi)
BuildRequires: perl-Catalyst-Plugin-Authentication perl-Module-Install perl-Set-Object perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-UNIVERSAL-isa

%description
Role based access control is very simple: every user has a list
of roles, which that user is allowed to assume, and every
restricted part of the app makes an assertion about the
necessary roles.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Catalyst*
%doc Changes README

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.07 -> 0.08

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.07-alt1
- 0.07 version
- fix directory ownership violation

* Tue Jul 01 2008 Michael Bochkaryov <misha@altlinux.ru> 0.05-alt2
- spec file cleanup

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

