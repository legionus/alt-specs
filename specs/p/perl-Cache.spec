%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(Digest/SHA.pm)
#
#   - Cache -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       -U --spec-only Cache
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Cache
%define m_distro Cache
%define m_name Cache
%define m_author_id unknown
%define _disable_test 1

Name: perl-Cache
Version: 2.11
Release: alt1

Summary: Cache - the Cache interface

License: Artistic / GPL
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/S/SH/SHLOMIF/Cache-%{version}.tar.gz

# Automatically added by buildreq on Sat Jun 14 2008
BuildRequires: perl-DBM perl-Digest-SHA1 perl-File-NFSLock perl-Heap perl-IO-String perl-Log-Agent perl-Storable perl-TimeDate perl-devel

# there old build DB_File in perl-DBM
BuildPreReq: perl-DB_File

%description
The Cache modules are designed to assist a developer in persisting data for a
specified period of time.  Often these modules are used in web applications to
store data locally to save repeated and redundant expensive calls to remote
machines or databases.

The Cache interface is implemented by derived classes that store cached data
in different manners (such as as files on a filesystem, or in memory).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README TODO design.dia
%perl_vendor_privlib/Cache/
%perl_vendor_privlib/Cache.pm

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.04-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.04-alt2
- fix directory ownership violation

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.04-alt1
- new version 2.04 (with rpmrb script)

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- first build for ALT Linux Sisyphus