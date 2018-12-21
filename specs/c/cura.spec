# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global with_check 1
%add_python3_compile_include %_libexecdir/cura

Name: cura
Epoch: 1
Version: 3.4.1
Release: alt1
Summary: 3D printer control software
License: LGPLv3+

Group: Engineering
Url: https://github.com/Ultimaker/Cura
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: Uranium >= %version
# Tests
%if 0%{?with_check}
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pip
%endif

%py3_requires serial zeroconf
Requires: python3-module-savitar = %version
Requires: Uranium = %version
Requires: qt5-quickcontrols
Requires: qt5-quickcontrols2
Requires: CuraEngine = %epoch:%version
Requires: cura-fdm-materials = %version
Requires: 3dprinter-udev-rules

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

%prep
%setup

# The setup.py is only useful for py2exe, remove it, so noone is tempted to use it
rm setup.py

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
%__subst '1s=^#!%_bindir/\(python\|env python\)3*=#!%__python3=' cura_app.py

%build
%cmake -DCURA_VERSION:STRING=%version \
       -DLIB_SUFFIX:STR=
%cmake_build

# rebuild locales
pushd resources/i18n
rm *.pot
for DIR in *; do
  pushd $DIR
  for FILE in *.po; do
    msgfmt $FILE.po -o LC_MESSAGES/${FILE}mo || :
  done
  popd
done
popd

%install
%cmakeinstall_std

# Sanitize the location of locale files
pushd %buildroot%_datadir
mv cura/resources/i18n locale
ln -s ../../locale cura/resources/i18n
rm locale/*/*.po
popd

%find_lang cura fdmextruder.def.json fdmprinter.def.json --output=%name.lang

# fix directories appdata
mv %buildroot%_datadir/metainfo %buildroot%_datadir/appdata


%check
%if 0%{?with_check}
python3 -m pip freeze
python3 -m pytest -v
%endif

desktop-file-validate %buildroot%_datadir/applications/%name.desktop

%files -f %name.lang
%doc LICENSE README.md
%python3_sitelibdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/*/apps/%name-icon.png
%_datadir/mime/packages/%name.xml
%_bindir/%name
%_libexecdir/%name

%changelog
* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 07 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1
- Disable tests

* Sat Jan 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt2
- Fix fail start with nvidia proprietary driver.

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt3
- NMU: sync with fc cura-15.04.4-4

* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 15.04.4-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt1_2
- update to new release by fcimport

* Thu Nov 26 2015 Igor Vlasenko <viy@altlinux.ru> 15.02.1-alt1_4
- new version

