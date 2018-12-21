#
#   - Mail::CheckUser -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Mail::CheckUser
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Mail-CheckUser
%define m_distro Mail-CheckUser
%define m_name Mail::CheckUser
%define m_author_id unknown
%define _disable_test 1

Name: perl-Mail-CheckUser
Version: 1.24
Release: alt1

Summary: check email addresses for validity

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/I/IL/ILYAM/%m_distro-%version.tar

# Automatically added by buildreq on Thu Jun 14 2007 (-bi)
BuildRequires: perl-devel perl-libnet perl-Net-DNS perl-Net-Ping

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This Perl module provides routines for checking validity of email address.

If is possible to turn off some or all networking checks (items 2 and 3).
See "GLOBAL VARIABLES".

This module was designed with CGIs (or any other dynamic Web content
programmed with Perl) in mind.  Usually it is required to quickly
check e-mail addresses in forms.  If the check can't be finished in
reasonable time, the e-mail address should be treated as valid.  This
is the default policy.  By default if a timeout happens the result of
the check is treated as positive.  This behavior can be overridden -
see "GLOBAL VARIABLES".

%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README TODO
%_bindir/cufilter
%perl_vendor_privlib/Mail/
%_man1dir/*

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.21-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt3
- fix build

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt2
- fix directory ownership violation

* Thu Jun 14 2007 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- first build for ALT Linux Sisyphus
