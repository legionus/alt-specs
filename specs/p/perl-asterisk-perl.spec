#
#   - asterisk-perl -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       asterisk-perl
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module asterisk-perl
%define m_distro asterisk-perl
%define m_name asterisk-perl
%define m_author_id unknown
%define _enable_test 1

Name: perl-asterisk-perl
Version: 1.08
Release: alt1

Summary: Asterisk Perl Interface

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Sun Aug 29 2010 (-bb)
BuildRequires: perl-devel perl(Net/Telnet.pm)

%description
None.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Ast*
%doc examples

%changelog
* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Tue Dec 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1.03-alt1
- 1.03

* Thu Dec 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.02-alt1
- 1.02

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Aug 29 2010 Denis Smirnov <mithraen@altlinux.ru> 1.01-alt2
- fix build

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Fri Jun 26 2009 Denis Smirnov <mithraen@altlinux.ru> 1.00-alt1
- version update
- package examples to %doc

* Mon Oct 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.09-alt2
- fix building

* Sun Apr 15 2007 Denis Smirnov <mithraen@altlinux.ru> 0.09-alt1
- first build for ALT Linux Sisyphus