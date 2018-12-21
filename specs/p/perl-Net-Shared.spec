#
#   - Net::Shared -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::Shared
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-Shared
%define m_distro Net-Shared
%define m_name Net::Shared
%define m_author_id JRYAN
%define _enable_test 1

Name: perl-Net-Shared
Version: 0.30
Release: alt2

Summary: Shared variables across processes that are either local or remote.

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Net-Shared/

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/J/JR/JRYAN/%m_distro-%version.tar.gz

Patch: Net-Shared-0.30-alt-perl522.patch

# Automatically added by buildreq on Fri Sep 05 2008 (-bi)
BuildRequires: perl-Log-Agent perl-Storable perl-devel

%description
"Net::Shared" gives the ability to share variables across processes both local and remote.
"Net::Shared::Local" and "Net::Shared::Remote" objects are created and interfaced with a
"Net::Shared::Handler" object.  Please see the documentation of the object types below and
also see the examples for more info.

%prep
%setup -q -n %m_distro
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net*
%doc Changes README examples/*

%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- NMU: fixed build

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 17 2008 Michael Bochkaryov <misha@altlinux.ru> 0.30-alt1
- first build for ALT Linux Sisyphus

