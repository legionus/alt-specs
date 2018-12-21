#
#   - XML::Compile::Dumper -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       XML::Compile::Dumper
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module XML-Compile-Dumper
%define m_distro XML-Compile-Dumper
%define m_name XML::Compile::Dumper
%define m_author_id MARKOV
%define _enable_test 1

Name: perl-XML-Compile-Dumper
Version: 0.14
Release: alt1

Summary: Remember precompiled XML processors

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/XML-Compile-Dumper-%{version}.tar.gz

# Automatically added by buildreq on Sun Jan 11 2009
BuildRequires: perl-Data-Dump-Streamer perl-Test-Pod perl-XML-Compile perl-XML-Compile-Tester

%description
This module simplifies the task of saving and loading pre-compiled
translators. Schema's can get huge, and when you are not creating
a daemon to do the XML communication, you may end-up compiling and
interpreting these large schemas often, just to be able to process simple
data-structures.  Based on the excellent module Data::Dump::Streamer,
this module helps you create standard Perl packages which contain the
reader and writer code references.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/XML/*

%changelog
* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- initial build for ALT Linux Sisyphus
