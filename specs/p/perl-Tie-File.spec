%define dist Tie-File
Name: perl-%dist
Version: 1.00
Release: alt1

Summary: Access the lines of a disk file via a Perl array
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TO/TODDR/Tie-File-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 27 2010
BuildRequires: perl-devel

%description
Tie::File represents a regular text file as a Perl array.
Each element in the array corresponds to a record in the file.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Tie*

%changelog
* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update
- dropped perl-Tie-File-0.96-0.97_02.patch (already upstream)

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 0.96-alt2
- updated to 0.97_02 from perl-5.12.2

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 0.96-alt1
- initial revision (split off from perl-base)
- updated to 0.97 from perl-5.8.6
