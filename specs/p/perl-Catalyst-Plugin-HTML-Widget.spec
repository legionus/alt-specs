#
#   - Catalyst-Plugin-HTML-Widget -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Catalyst::Plugin::HTML::Widget
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Catalyst-Plugin-HTML-Widget
%define m_distro Catalyst-Plugin-HTML-Widget
%define m_name Catalyst-Plugin-HTML-Widget
%define m_author_id SRI
%define _enable_test 1

Name: perl-Catalyst-Plugin-HTML-Widget
Version: 1.1
Release: alt2.2

Summary: HTML Widget Catalyst Plugin

License: Artistic and GPL-1.0-only
Group: Development/Perl
Url: http://search.cpan.org/dist/Catalyst-Plugin-HTML-Widget/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/S/SR/SRI/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Sep 08 2008 (-bi)
BuildRequires: perl-Catalyst-Runtime perl-HTML-Widget perl-Log-Agent perl-Test-Pod perl-Test-Pod-Coverage perl(Cpanel/JSON/XS.pm)

%description
Catalyst::Plugin::HTML::Widget - HTML Widget And Validation Framework

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Catalyst*

%changelog
* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.2
- fixed build

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 1.1-alt2
- fix directory ownership violation

* Tue Jul 01 2008 Michael Bochkaryov <misha@altlinux.ru> 1.1-alt1
- first build for ALT Linux Sisyphus

