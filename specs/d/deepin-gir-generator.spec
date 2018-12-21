Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: libgudev-gir
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global repo go-gir-generator

Name:           deepin-gir-generator
Version:        1.1.0
Release:        alt1_2
Summary:        Generate static golang bindings for GObject
License:        GPLv3
URL:            https://github.com/linuxdeepin/go-gir-generator
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         SettingsBackendLike.patch
Patch1:         launch_uris_as_manager_with_fds.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
Provides:       golang(gir/gobject-2.0)
Provides:       golang(gir/gio-2.0)
Provides:       golang(gir/glib-2.0)
Provides:       golang(gir/gudev-1.0)
Source44: import.info

%description
Generate static golang bindings for GObject

%prep
%setup -q -n %{repo}-%{version}

GIO_VER=$(v=$(rpm -q --qf %{RPMTAG_VERSION} gobject-introspection); echo ${v//./})
if [ $GIO_VER -ge 1521 ]; then
# Our gobject-introspection is too new
# https://cr.deepin.io/#/c/16880/
%patch0 -p1
%patch1 -p1
fi

%build
export GOPATH="%{go_path}"
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc --no-dereference LICENSE
%{_bindir}/gir-generator
%{go_path}/src/gir/

%changelog
* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- update to new release by fcimport

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- new version

