%define _unpackaged_files_terminate_build 1
#
#   - CSS::Tiny -
#   This spec file was automatically generated by cpan2rpm [ver: 1.15]
#   (ALT Linux revision)
#   The following arguments were used:
#       CSS::Tiny
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module CSS-Tiny
%define m_distro CSS-Tiny
%define m_name CSS::Tiny
%define m_author_id ADAMK
%define _enable_test 1

Name: perl-CSS-Tiny
Version: 1.20
Release: alt1

Summary: Read/Write .css files with as little code as possible

License: Artistic and GPL-1.0-only
Group: Development/Perl
Url: http://search.cpan.org/dist/CSS-Tiny/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/C/CH/CHORNY/CSS-Tiny-%{version}.tar.gz

# Automatically added by buildreq on Fri Sep 05 2008 (-bi)
BuildRequires: perl-Clone perl-devel

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as little
code as possible, reducing load time and memory overhead. CSS.pm requires about
2.6 meg or ram to load, which is a large amount of overhead if you only want to
do trivial things. Memory usage is normally scoffed at in Perl, but in my
opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and anything we
write shouldn't need to have documentation/comments. If you need something with
more power, move up to CSS.pm. With the increasing complexity of CSS, this is
becoming more common, but many situations can still live with simple CSS files.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CSS*
%doc Changes

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.15-alt2
- fix directory ownership violation

* Mon Jul 14 2008 Michael Bochkaryov <misha@altlinux.ru> 1.15-alt1
- first build for ALT Linux Sisyphus

