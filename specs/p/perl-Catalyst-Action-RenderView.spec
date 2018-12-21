#
#   - Catalyst::Action::RenderView -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Catalyst-Action-RenderView
%define m_distro Catalyst-Action-RenderView
%define m_name Catalyst::Action::RenderView
%define m_author_id unknown
%def_enable test

Name: perl-Catalyst-Action-RenderView
Version: 0.16
Release: alt1

Summary: %m_name - Sensible default end action

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Action-RenderView-0.16.tar.gz

# Automatically added by buildreq on Wed Apr 21 2010 (-bi)
BuildRequires: perl-Catalyst-Devel perl-Data-Visitor perl-Test-Pod perl-Test-Pod-Coverage

%description
This action implements a sensible default end action, which will
forward to the first available view, unless status is set to
3xx, or there is a response body.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Catalyst*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.04 -> 0.14

* Sun Dec 14 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04-alt2
- fix directory ownership violation

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus

