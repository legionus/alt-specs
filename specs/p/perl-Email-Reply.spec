%define _unpackaged_files_terminate_build 1
#
#   - Email::Reply -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Email::Reply
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Email-Reply
%define m_distro Email-Reply
%define m_name Email::Reply
%define m_author_id unknown
%define _disable_test 1

Name: perl-Email-Reply
Version: 1.204
Release: alt3

Summary: Reply to a Message

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Email-Reply-%{version}.tar.gz

# Automatically added by buildreq on Sat Nov 29 2008
BuildRequires: perl-Email-Abstract perl-Email-Address perl-Email-MIME-Creator perl-Encode perl-devel

%description
This software takes the hard out of generating replies to email messages.

%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc README Changes
%perl_vendor_privlib/Email/

%changelog
* Sat Feb 03 2018 Michael Shigorin <mike@altlinux.org> 1.204-alt3
- dropped obviously wrong BRs

* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.204-alt2
- fix missing buildreq

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.204-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.203-alt1
- automated CPAN update

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.202-alt1
- new version 1.202 (with rpmrb script)
- update buildreqs, remove man pages

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.201-alt2
- fix directory ownership violation

* Sat Jun 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.201-alt1
- new version 1.201 (with rpmrb script)

* Tue Dec 26 2006 Vitaly Lipatov <lav@altlinux.ru> 1.200-alt1
- first build for ALT Linux Sisyphus
