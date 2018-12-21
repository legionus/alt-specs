%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(Test/CPAN/Meta.pm) perl(Test/EOL.pm) perl(Test/Memory/Cycle.pm) perl(Test/NoTabs.pm) perl(Test/Differences.pm)
#
#   - HTML::Scrubber - (tar repacked manually!!!)
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       HTML::Scrubber
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module HTML-Scrubber
%define m_distro HTML-Scrubber
%define m_name HTML::Scrubber
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-Scrubber
Version: 0.17
Release: alt1

Summary: HTML-Scrubber - Perl extension for scrubbing/sanitizing html

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/N/NI/NIGELM/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Tue Jun 07 2005
BuildRequires: perl-HTML-Parser perl-devel

%description
If you wanna "scrub" or "sanitize" html input
in a reliable an flexible fashion,
then this module is for you.

I wasn't satisfied with HTML::Sanitizer because it is
based on HTML::TreeBuilder,
so I thought I'd write something similar
that works directly with HTML::Parser.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/HTML/

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Sat Oct 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt2
- fix directory ownership violation

* Tue Jun 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt1
- first build for ALT Linux Sisyphus