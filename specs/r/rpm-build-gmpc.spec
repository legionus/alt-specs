# Required parameters:
#   %func - the plugin name
#   %builddeps - this line will be appended to BuildRequires (gmpc-devel is
#     already there)

# Using this meta-spec:
# - %define the required parameters,
# - put correct Name:, Version:, and License: tags
# - put BuildRequires(pre): rpm-build-gmpc
# - %include this file;
# - append %files section;
# - append %changelog section.
# That's all folks!

%define _unpackaged_files_terminate_build 1

%define prog_name gmpc
%define part plugin

Summary: %func %part for %prog_name
License: %gpl2plus
Group: Sound

Url: http://www.sarine.nl/gmpc-plugins

Source: %prog_name-%part-%func-%version.tar

#Requires:	%prog_name
BuildRequires(pre): rpm-build-licenses
BuildRequires: libmpd-devel gmpc-devel %builddeps

%description
%func %part for %prog_name.

%prep
%setup -q -n %prog_name-%part-%func-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%define _name gmpc

Name: rpm-build-%_name
Version: 0.1.2
Release: alt1

Summary: RPM macros for building GMPC plugins
License: %gpl2plus
Group: Development/Other

Source1: gmpc-plugin.inc.spec

Packager: Alexey Rusakov <ktirf@altlinux.ru>

BuildArch: noarch

Requires: common-licenses
BuildRequires(pre): rpm-build-licenses

%description
This package contains RPM macros and a spec file template that helps
building GMPC plugins.

%define gmpc_plugin_incspec %_datadir/gmpc/gmpc-plugin.inc.spec

%prep
ln -sf %_licensedir/GPL-2 COPYING

%install
install -D -m644 %SOURCE1 %buildroot%gmpc_plugin_incspec
cat <<__EOF__ >%_name.rpmmacros
%%gmpc_plugin_incspec %gmpc_plugin_incspec
%%gmpc_plugin_libdir %%_libdir/gmpc/plugins
%%gmpc_plugin_datadir %%_datadir/gmpc/plugins
__EOF__
install -D -m644 %_name.rpmmacros %buildroot/%_sysconfdir/rpm/macros.d/%_name

%files
%dir %_datadir/gmpc
%gmpc_plugin_incspec
%_sysconfdir/rpm/macros.d/%_name
%doc --no-dereference COPYING

%changelog
* Tue Apr 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.1.2-alt1
- Escape macros properly, fixing ALT Bug 19613.

* Fri Mar 13 2009 Alexey Rusakov <ktirf@altlinux.org> 0.1.1-alt1
- Initial Sisyphus build.

