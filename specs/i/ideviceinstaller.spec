Name: ideviceinstaller
Version: 1.1.0
Release: alt3.git.f7988de8

Summary: A tool to manage installed apps on iOS device
Group: System/Kernel and hardware
License: GPLv2
Url: http://www.libimobiledevice.org/

Source: %name.tar

Patch0: alt-fix-build.patch

BuildRequires: libplist-devel >= 0.15
BuildRequires: libimobiledevice-devel >= 1.2.0
BuildRequires: libzip-devel >= 0.10

%description
ideviceinstaller is a tool to interact with the installation_proxy
of an iOS device allowing to install, upgrade, uninstall, archive, restore
and enumerate installed or archived apps.

%prep
%setup -n %name
%patch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/ideviceinstaller
%_man1dir/%{name}*
%doc AUTHORS README NEWS

%changelog
* Wed Jun 20 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.0-alt3.git.f7988de8
- updated to upstream commit 'f7988de8' (minor bugfixes)

* Sat Apr 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.0-alt2.git.58d359fd
- updated to upstream commit '58d359fd' (minor bugfixes)

* Tue Jan 10 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.0-alt1.git.442f670a
- first build for Sisyphus from https://github.com/libimobiledevice/ideviceinstaller
