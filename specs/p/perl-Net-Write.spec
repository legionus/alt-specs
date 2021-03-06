%define _unpackaged_files_terminate_build 1
#
#   - Net::Write -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::Write
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-Write
%define m_distro Net-Write
%define m_name Net::Write
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-Write
Version: 1.10
Release: alt1

Summary: a portable interface to open and send raw data to network

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/G/GO/GOMOR/Net-Write-%{version}.tar.gz

# Automatically added by buildreq on Sat Nov 07 2009
BuildRequires: perl-Class-Gomor perl-Net-Pcap perl-Socket6 perl-Test-Pod perl-Test-Pod-Coverage perl(Module/Build.pm)

%description
Net::Write provides a portable interface to open a network interface, and be able to write raw data directly to the network. It juste provides three methods when a Net::Write object has been created for an interface: open, send, close.

It is possible to open a network interface to send frames at layer 2 (you craft a frame from link layer), or at layer 3 (you craft a frame from network layer), or at layer 4 (you craft a frame from transport layer).

NOTE: not all operating systems support all layer opening. Currently, Windows only supports opening and sending at layer 2. Other Unix systems should be able to open and send at all layers.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Net/*

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sat Nov 07 2009 Denis Smirnov <mithraen@altlinux.ru> 1.05-alt1
- initial build for ALT Linux Sisyphus

