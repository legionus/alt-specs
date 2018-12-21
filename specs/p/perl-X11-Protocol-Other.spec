%define dist X11-Protocol-Other

Name:     perl-%dist
Version:  30
Release:  alt1

Summary:  This is some miscellaneous extras and helpers for X11::Protocol
License:  GPLv3+
Group:    Development/Perl
Packager: Sergey Vlasov <vsu@altlinux.ru>

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl-X11-Protocol
BuildRequires: perl-Encode

%description
This is some miscellaneous extras and helpers for X11::Protocol.

%prep
%setup -q -n %dist-%version

%build
# test tries to display a window
%def_without test
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/X11/*
%perl_vendor_privlib/Encode/X11.pm

%changelog
* Sun Apr 09 2017 Andrey Cherepanov <cas@altlinux.org> 30-alt1
- New version

* Tue Jan 21 2014 Andrey Cherepanov <cas@altlinux.org> 29-alt1
- New version

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 28-alt1
- New version

* Fri Oct 04 2013 Andrey Cherepanov <cas@altlinux.org> 25-alt1
- New version 25

* Tue Jan 15 2013 Andrey Cherepanov <cas@altlinux.org> 23-alt1
- Initial build in Sisyphus

