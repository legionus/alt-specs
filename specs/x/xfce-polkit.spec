Name: xfce-polkit
Version: 0.3
Release: alt1

Summary: Simple PolicyKit authentication agent for Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://github.com/ncopa/xfce-polkit
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: https://github.com/ncopa/xfce-polkit
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libxfce4ui-gtk3-devel
BuildRequires: glib2-devel libpolkit-devel

Requires: polkit

%define _unpackaged_files_terminate_build 1

%description
%summary

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec/polkit-1 \
	--disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%_prefix/libexec/polkit-1/%name
%_sysconfdir/xdg/autostart/*.desktop

%changelog
* Wed Aug 29 2018 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Use _unpackaged_files_terminate_build.
- 0.2 -> 0.3.

* Mon Apr 11 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Patch from upstream git:
  + fix Name/Comment fields.
- Initial build.

