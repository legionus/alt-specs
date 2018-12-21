#
#   - Template::Provider::Encoding -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Template::Provider::Encoding
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Template-Provider-Encoding
%define m_distro Template-Provider-Encoding
%define m_name Template::Provider::Encoding
%define m_author_id MIYAGAWA
%define _enable_test 1

Name: perl-Template-Provider-Encoding
Version: 0.10
Release: alt1.1.1

Summary: Explicitly declare encodings of your templates

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Template-Provider-Encoding/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/M/MI/MIYAGAWA/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Jun 30 2008
BuildRequires: perl-Encode-JP perl-Template perl-devel

%description
Template::Provider::Encoding is a Template Provider subclass to decode
template using its declaration. You have to declare encoding of the
template in the head (1st line) of template using (fake) encoding TT
plugin. Otherwise the template is handled as utf-8.

  [%% USE encoding 'utf-8' %%]
  Here comes utf-8 strings with [%% variable %%].

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc Changes 
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus
