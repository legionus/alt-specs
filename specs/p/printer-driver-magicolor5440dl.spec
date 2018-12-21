%define rname magicolor5440dl

Summary: Cups Driver for KONICA MINOLTA magicolor 5440 DL
Name: printer-driver-%rname
Version: 1.2.1
Release: alt1
License: GPLv2
Group: System/Configuration/Printing
Url: http://printer.konicaminolta.net/

Source: %rname-%version.tar
Patch1: magicolor2430DL-shared_system_libs.patch
Patch2: magicolor5440DL-1.2.1-cups-2.2.patch

BuildRequires: automake libcups-devel libjbig-devel liblcms-devel
Requires: cups

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm5440dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 5440 DL printer

%prep
%setup -n %rname-%version
%patch1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/cups/filter/rastertokm5440dl
%_datadir/KONICA_MINOLTA/mc5440DL
%_datadir/cups/model/KONICA_MINOLTA/km5440dl.ppd*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.2.1-alt1
- Initial build for ALT

