#
#   - Convert::Wiki -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Convert::Wiki
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Convert-Wiki
%define m_distro Convert-Wiki
%define m_name Convert::Wiki
%define m_author_id unknown
%define _enable_test 1

Name: perl-Convert-Wiki
Version: 0.05
Release: alt2.1

Summary: Convert HTML/POD/txt from/to Wiki code

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Sep 10 2005
BuildRequires: perl-Algorithm-Diff perl-Test-Differences perl-Text-Diff perl-Text-Format perl-YAML perl-devel

%description
"Convert::Wiki" converts from various formats to various Wiki formats.

Input can come as HTML, POD or plain TXT (like it is written in many READMEs).
The data will be converted to an internal, node based format and can then be
converted to Wikicode as used by many wikis like the Wikipedia.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README TODO CHANGES
%perl_vendor_privlib/Convert/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt2
- fix directory ownership violation

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

