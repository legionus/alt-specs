#
#   - Net::RBLClient -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net-RBLClient-0.5.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-RBLClient
%define m_distro Net-RBLClient
%define m_name Net::RBLClient
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-RBLClient
Version: 0.5
Release: alt3

Summary: Parallel RBL lookup client

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %m_distro-0.5.tar.gz
Patch: Net-RBLClient-0.5-syntaxfix.patch

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires: perl-devel perl-Net-DNS

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This module is used to discover what RBL's are listing a particular IP
address.  It parallelizes requests for fast response.

An RBL, or Realtime Blackhole List, is a list of IP addresses meeting some
criteria such as involvement in Unsolicited Bulk Email.  Each RBL has
its own criteria for addition and removal of addresses.  If you want to
block email or other traffic to/from your network based on one or more
RBL's, you should carefully study the behavior of those RBL's before and
during such blocking.

%prep
%setup -n RBLCLient-0.5
%patch -p1
%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net
%_bindir/spamalyze
%_man1dir/*

%changelog
* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3
- fixed build

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 06 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5-alt2
- Package `spamalyze' tool

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated CPAN update

* Tue Sep 02 2008 Vladimir V Kamarzin <vvk@altlinux.org> 0.4-alt2
- Fixed module packaging according to fresh sisyphus_check

* Wed Nov 22 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4-alt1
- first build for ALT Linux Sisyphus

