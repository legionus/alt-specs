%define _unpackaged_files_terminate_build 1
#
#   - Biblio::EndnoteStyle -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Biblio-EndnoteStyle-0.05.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Biblio-EndnoteStyle
%define m_distro Biblio-EndnoteStyle
%define m_name Biblio::EndnoteStyle
%define m_author_id unknown
%define _enable_test 1

Name: perl-Biblio-EndnoteStyle
Version: 0.06
Release: alt1

Summary: reference formatting using Endnote-like templates

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vladimir A. Svyatoshenko <svyt@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/M/MI/MIRK/Biblio-EndnoteStyle-%{version}.tar.gz

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: perl-devel

%description
This small module provides a way of formatting bibliographic
references using style templates similar to those used by the popular
reference management software Endnote (http://www.endnote.com/).  The
API is embarrassingly simple: a formatter object is made using the
class's constructor, the "new()" method; "format()" may then be
repeatedly called on this object, using the same or different
templates.

(The sole purpose of the object is to cache compiled templates so that
multiple "format()" invocations are more efficient than they would
otherwise be.  Apart from that, the API might just as well have been a
single function.)

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/endnote-format
%perl_vendor_privlib/Biblio*

%changelog
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.05-alt2
- fixed build

* Thu Jul 03 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus
