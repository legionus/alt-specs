%def_without test
#
#   - Net::Google -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 1.0 Net-Google-1.0.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-Google
%define m_distro Net-Google
%define m_name Net::Google
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-Google
Version: 1.0
Release: alt1

Summary: Net-Google - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Thu May 24 2012 (-bb)
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-YAML perl-Class-Inspector perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-URI perl-devel perl-libwww perl-podlators python-base
BuildRequires: perl-Module-Build perl-SOAP-Lite

%description
None.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Thu May 24 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

