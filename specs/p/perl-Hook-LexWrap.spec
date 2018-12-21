%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm)
#
#   - Hook::LexWrap -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Hook::LexWrap
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Hook-LexWrap
%define m_distro Hook-LexWrap
%define m_name Hook::LexWrap
%define m_author_id unknown
%define _enable_test 1

Name: perl-Hook-LexWrap
Version: 0.26
Release: alt1

Summary: Hook-LexWrap - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Sep 02 2005
BuildRequires: perl-devel unzip

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both)
around an existing subroutine. Unlike other modules that provide this
capacity (e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap
implements wrappers in such a way that the standard `caller' function
works correctly within the wrapped subroutine.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Hook/

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt2
- fix directory ownership violation

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- first build for ALT Linux Sisyphus
