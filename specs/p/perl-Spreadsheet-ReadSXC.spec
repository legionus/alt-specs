#
#   - Spreadsheet::ReadSXC -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       -debug Spreadsheet::ReadSXC
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Spreadsheet-ReadSXC
%define m_distro Spreadsheet-ReadSXC
%define m_name Spreadsheet::ReadSXC
%define m_author_id unknown
%define _enable_test 1

Name: perl-Spreadsheet-ReadSXC
Version: 0.20
Release: alt2

Summary: Extract OpenOffice 1.x spreadsheet data

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/T/TE/TERHECHTE/%m_distro-%version.tar.gz

# Automatically added by buildreq on Fri Nov 13 2009 (-bi)
BuildRequires: perl-Archive-Zip perl-XML-Parser perl-devel

%description
Spreadsheet::ReadSXC extracts data from OpenOffice 1.x spreadsheet
files (.sxc). It exports the function read_sxc() which takes a
filename and an optional reference to a hash of options as
arguments and returns a reference to a hash of references to
two-dimensional arrays. The hash keys correspond to the names of
worksheets in the OpenOffice workbook. The two-dimensional arrays
correspond to rows and cells in the respective spreadsheets. If
you don't like this because the order of sheets is not preserved
in a hash, read on. The 'OrderBySheet' option provides an array
of hashes instead.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Spreadsheet/*
%doc Changes README

%changelog
* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt2
- spec file cleanup

* Wed Aug 12 2009 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt1
- initial build for ALT Linux Sisyphus
