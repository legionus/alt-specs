#
#   - Text::WrapI18N -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Text::WrapI18N
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-WrapI18N
%define m_distro Text-WrapI18N
%define m_name Text::WrapI18N
%define m_author_id unknown
%define _enable_test 1

Name: perl-Text-WrapI18N
Version: 0.06
Release: alt2

Summary: Line wrapping module with support for multibyte, fullwidth,

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Fri Feb 17 2006
BuildRequires: perl-Text-CharWidth perl-devel

%description
This module intends to be a better Text::Wrap module.
This module is needed to support multibyte character encodings such
as UTF-8, EUC-JP, EUC-KR, GB2312, and Big5.  This module also supports
characters with irregular widths, such as combining characters (which
occupy zero columns on terminal, like diacritical marks in UTF-8) and
fullwidth characters (which occupy two columns on terminal, like most
of east Asian characters).  Also, minimal handling of languages which
doesn't use whitespaces between words (like Chinese and Japanese) is
supported.

Like Text::Wrap, hyphenation and "kinsoku" processing are not supported,
to keep simplicity.

*wrap(firstheader, nextheader, texts)* is the main subroutine of
Text::WrapI18N module to execute the line wrapping.  Input parameters
and output data emulate Text::Wrap.  The texts have to be written in
locale encoding.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes README
%perl_vendor_privlib/Text/*

%changelog
* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt2
- fix directory ownership violation
- disable man packaging

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- first build for ALT Linux Sisyphus

