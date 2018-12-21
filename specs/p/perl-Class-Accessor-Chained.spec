#
#   - Class::Accessor::Chained -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Class-Accessor-Chained
%define m_distro Class-Accessor-Chained
%define m_name Class::Accessor::Chained
%define m_author_id unknown
%def_enable test

Name: perl-Class-Accessor-Chained
Version: 0.01
Release: alt2.1

Summary: %m_name - make chained accessors

License: Artistic and GPL
Group: Development/Perl
Url: http://search.cpan.org/dist/Class-Accessor-Chained/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Fri Mar 23 2007 (-bi)
BuildRequires: perl-Class-Accessor perl-Module-Build perl-version

%description
A chained accessor is one that always returns the object when
called with parameters (to set), and the value of the field when
called with no arguments.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class*
%doc Changes

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.01-alt2
- fix directory ownership violation
- spec file cleanup

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
