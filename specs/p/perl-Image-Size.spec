%define dist Image-Size
Name: perl-%dist
Version: 3.300
Release: alt1

Summary: Perl library for reading the dimensions of an image
License: Artistic 2.0 or LGPL-1.0-only
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJRAY/Image-Size-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-IO-Compress perl-Module-Build

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH attributes
to IMG tags.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc ChangeLog README
%_bindir/imgsize
%_man1dir/imgsize.1*
%perl_vendor_privlib/Image

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 3.300-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 3.232-alt1
- 3.230 -> 3.232

* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 3.230-alt1
- 3.2 -> 3.230

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jul 22 2009 Alexey Tourbin <at@altlinux.ru> 3.2-alt1
- 3.1.1 -> 3.2

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 3.1.1-alt1
- 3.0 -> 3.1.1
- updated License tag to `Artistic 2.0 or LGPL'

* Mon Jun 12 2006 Alexey Tourbin <at@altlinux.ru> 3.0-alt1
- 2.992 -> 3.0

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.992-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Aug 22 2003 Alexey Tourbin <at@altlinux.ru> 2.992-alt1
- initial revision
