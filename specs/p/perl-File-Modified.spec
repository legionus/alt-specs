#
#   - File::Modified -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module File-Modified
%define m_distro File-Modified
%define m_name File::Modified
%define m_author_id unknown
%def_enable test

Name: perl-File-Modified
Version: 0.10
Release: alt1

Summary: %m_name - checks intelligently if files have changed

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/File-Modified/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/N/NE/NEILB/File-Modified-%{version}.tar.gz

# Automatically added by buildreq on Mon Sep 08 2008 (-bi)
BuildRequires: perl-Digest-MD2 perl-Digest-SHA1 perl-devel

%description
The Modified module is intended as a simple method for programs to detect
whether configuration files (or modules they rely on) have changed. There are
currently two methods of change detection implemented, "mtime" and "MD5".
The "MD5" method will fall back to use timestamps if the "Digest::MD5" module
cannot be loaded.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File*
%doc Changes README

%changelog
* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.07-alt1
- Built for Sisyphus

