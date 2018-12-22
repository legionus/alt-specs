%define module suse-compat
Name:		rpm-build-suse-compat
Version:	0.033
Release:	alt1
Summary:	Compatibility environment to build SuSE rpms
License:	GPL-2.0-or-later
Group:		Development/Other

Source:		%name-%version.tar
Patch:		update-desktop-files-alt-%version.patch

BuildArch:	noarch
Requires:	rpm-macros-suse-compat = %version-%release
Requires:	rpm-macros-generic-compat

%description
%summary

%package -n	rpm-macros-suse-compat
Group:		Development/Other
Summary:	SuSE compatibility macros

%description -n rpm-macros-suse-compat
%summary

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_rpmlibdir
install -m0755 update-desktop-files/suse_update_desktop_file.sh update-desktop-files/map-desktop-category.sh %buildroot%_rpmlibdir/

install -m0644 -D update-desktop-files/macro %buildroot%_rpmmacrosdir/%module-update-desktop-files
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
for ext in cmake; do
    install -D -m644 macros.$ext -p %buildroot%_rpmmacrosdir/%module-$ext
done



%files
%_rpmlibdir/*.sh

%files -n rpm-macros-suse-compat
%_rpmmacrosdir/%{module}*

%changelog
* Tue Apr 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- new version

* Tue Apr 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- added %%lang_package

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- added Requires: rpm-macros-generic-compat

* Sun Oct 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added %%__cmake

* Sat Oct 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added cmake support

* Mon Jan 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- build for Sisyphus

