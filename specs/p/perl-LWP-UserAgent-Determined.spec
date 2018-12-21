# network is disabled :(
%def_disable test
#
#   - LWP::UserAgent::Determined -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       LWP::UserAgent::Determined
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module LWP-UserAgent-Determined
%define m_distro LWP-UserAgent-Determined
%define m_name LWP::UserAgent::Determined
%define m_author_id unknown
%define _enable_test 1

Name: perl-LWP-UserAgent-Determined
Version: 1.07
Release: alt1

Summary: a virtual browser that retries errors

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AL/ALEXMV/LWP-UserAgent-Determined-%{version}.tar.gz

# Automatically added by buildreq on Sat Sep 04 2010
BuildRequires: libnss-mdns perl-devel perl-libwww

%description
This class works just like LWP::UserAgent (and is based on it, by
being a subclass of it), except that when you use it to get a web page
but run into a possibly-temporary error (like a DNS lookup timeout),
it'll wait a few seconds and retry a few times.

It also adds some methods for controlling exactly what errors are
considered retry-worthy and how many times to wait and for how many
seconds, but normally you needn't bother about these, as the default
settings are relatively sane.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/LWP/*

%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2
- fixed build (disabled tests because network is disabled)

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 1.04-alt1
- initial build for ALT Linux Sisyphus
