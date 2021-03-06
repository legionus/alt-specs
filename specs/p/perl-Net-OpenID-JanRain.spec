#
#   - Net::OpenID::JanRain -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::OpenID::JanRain
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-OpenID-JanRain
%define m_distro Net-OpenID-JanRain
%define m_name Net::OpenID::JanRain
%define m_author_id unknown
%define _disable_test 1

Name: perl-Net-OpenID-JanRain
Version: 1.1.1
Release: alt3

Summary: OpenID Server and Consumer with JanRain API

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/A/AR/ARNESOND/%m_distro-%version.tar

# Automatically added by buildreq on Sat Oct 08 2011 (-bi)
# optimized out: perl-DBI perl-Digest-HMAC perl-Digest-SHA perl-HTTP-Date perl-HTTP-Message perl-IO-Socket-INET6 perl-Math-BigInt perl-Math-BigInt-FastCalc perl-Net-DNS perl-Socket6 perl-URI perl-XML-Parser perl-XML-XPath perl-libwww
BuildRequires: perl-CGI perl-Crypt-DH perl-DBD-Pg perl-Digest-SHA1 perl-LWPx-ParanoidAgent perl-Net-Yadis perl-devel perl(Digest/HMAC_SHA1.pm)

%description
To use this library, put the contents of the lib directory into your
perl path. Currently only the consumer is implemented. Extensive POD
documentation exists in the two modules,
Net/OpenID/JanRain/Consumer.pm and Net/OpenID/JanRain/Server.pm
You will also need a store from Net/OpenID/JanRain/Stores , which
all have PODs too.  We now offer a flat file store and three
different SQL database stores, SQLite, MySQL, and PostgreSQL.


%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Net/

%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3
- NMU: fixed build

* Thu Oct 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update buildreqs

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- update package version, add description
- fix directory ownership violation

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- first build for ALT Linux Sisyphus

